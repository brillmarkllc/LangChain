from langchain_chroma import Chroma
from langchain.chains.retrieval_qa.base import RetrievalQA
from config import llm, embedding_function  # Assuming llm is defined and configured in your config file

def initialize_rag_chain(db_dir="chroma_db"):
    """Initialize the RAG (Retrieval Augmented Generation) chain."""
    # Load ChromaDB Vectorstore
    vectorstore = Chroma(persist_directory=db_dir, embedding_function=embedding_function)

    # Initialize retriever
    retriever = vectorstore.as_retriever()

    # Create RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=retriever,
        return_source_documents=True  # This ensures that sources are returned
    )
    
    return qa_chain

def query_with_sources(query, qa_chain):
    """Make a query to the RAG chain and return the result with sources."""
    # Pass the query and get contextually accurate response with sources
    result = qa_chain({"query": query})

    # Extract the result and source documents
    response = result.get("result", "")
    sources = result.get("source_documents", [])

    # Get text from response and sources
    source_urls = [source.metadata["source"] for source in sources]

    return response, source_urls

def main():
    # Initialize RAG chain
    qa_chain = initialize_rag_chain()

    # Take user input for the query
    query = input("Ask a question: ")

    # Get contextually accurate response with sources
    response, sources = query_with_sources(query, qa_chain)

    # Print the response with citations
    print(f"Answer: {response}")
    if sources:
        print("Sources:")
        for source in sources:
            print(f"- {source}")
    else:
        print("No sources found.")

if __name__ == "__main__":
    main()
