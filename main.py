from langchain_chroma import Chroma
from langchain.chains.retrieval_qa.base import RetrievalQA
from config import llm, embedding_function  # Assuming llm is defined and configured in your config file

# Static mapping of keywords to URLs
KEYWORD_URL_MAPPING = {
    "brillmark": "https://www.brillmark.com",
    "about us": "https://www.brillmark.com/about-us/",
    "services": "https://www.brillmark.com/services/",
    "a/b test": "https://www.brillmark.com/hire-ab-test-developer/",
    "shopify": "https://www.brillmark.com/hire-shopify-developer/",
    "wordpress": "https://www.brillmark.com/wordpress-development-services/"
}

def initialize_rag_chain(db_dir="chroma_db"):
    """Initialize the RAG (Retrieval Augmented Generation) chain."""
    vectorstore = Chroma(persist_directory=db_dir, embedding_function=embedding_function)
    retriever = vectorstore.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

def query_with_sources(query, qa_chain, chat_history):
    """Make a query to the RAG chain with chat history and return the result with sources."""
    # Combine chat history with the current query
    full_context = "\n".join([f"User: {q}\nAssistant: {r}" for q, r in chat_history]) + f"\nUser: {query}"
    result = qa_chain({"query": full_context})
    response = result.get("result", "")
    sources = result.get("source_documents", [])
    source_urls = [source.metadata["source"] for source in sources]
    return response, sources, source_urls

def get_static_sources(query):
    """Match keywords in the query to static URLs."""
    matched_sources = []
    for keyword, url in KEYWORD_URL_MAPPING.items():
        if keyword.lower() in query.lower():
            matched_sources.append(url)
    return matched_sources

def save_to_file(query, response, all_sources, filename="chat_history.txt"):
    """Save query, response, and sources to a file in real-time."""
    with open(filename, "a") as file:
        file.write(f"Query: {query}\n")
        file.write(f"Response: {response}\n")
        file.write(f"Sources: {', '.join(all_sources) if all_sources else 'No sources found.'}\n")
        file.write("\n")  # Newline between different sessions

def main():
    # Initialize RAG chain
    qa_chain = initialize_rag_chain()
    chat_history = []  # To maintain chat history

    print("Welcome to the Chat Session! (Press CTRL+C to exit)\n")

    try:
        while True:
            # Take user input for the query
            query = input("User: ")

            # Get contextually accurate response with sources from the RAG chain
            response, sources, rag_urls = query_with_sources(query, qa_chain, chat_history)

            # Check if any static sources are matched based on the query
            static_sources = get_static_sources(query)

            # Combine both RAG and static sources
            all_sources = set(rag_urls + static_sources)

            # Print the response with citations
            print(f"\AI: {response}")
            if all_sources:
                print("\nLLM Sources:")
                for source in rag_urls:
                    print(f"- {source}")
                print("Static Sources:")
                for source in static_sources:
                    print(f"- {source}")
            else:
                print("\nNo sources found.")

            # Save the interaction to a file in real-time
            save_to_file(query, response, all_sources)
            print("\nChat session saved. Continue asking...\n")

            # Update chat history
            chat_history.append((query, response))
    except KeyboardInterrupt:
        print("\nExiting chat session. Goodbye!")

if __name__ == "__main__":
    main()
