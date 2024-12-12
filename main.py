from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_core.messages import HumanMessage, AIMessage
from langchain.chains.retrieval import create_retrieval_chain
from constants.keyword import render_buttons
from constants.prompt import SYSTEM_MESSAGE
from config import llm, embedding_function
from save_data import save_to_file
# from langsmith import Client, traceable

# client = Client()

# @traceable
def create_chain(db_dir="chroma_db"):
    vectorStore = Chroma(persist_directory=db_dir, 
                         embedding_function=embedding_function)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_MESSAGE),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}")
    ])

    chain = create_stuff_documents_chain(
        llm=llm,
        prompt=prompt
    )

    retriever = vectorStore.as_retriever(search_kwargs={"k": 1})
    
    retriever_prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
        ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
    ])

    history_aware_retriever = create_history_aware_retriever(
        llm=llm,
        retriever=retriever,
        prompt=retriever_prompt
    )

    retrieval_chain = create_retrieval_chain(
        history_aware_retriever,
        chain
    )

    return retrieval_chain


# @traceable
def process_chat(chain, question, chat_history):
    response = chain.invoke({
        "chat_history": chat_history,
        "input": question,
    })
    return response["answer"]


def main():
    # Initialize chain
    chain = create_chain()

    chat_history = []  # To maintain chat history

    print("Welcome to the Chat Session! (Press CTRL+C to exit)\n")

    try:
        while True:
            # Take user input for the query
            query = input("User: ")

            print("Agent: ", end="", flush=True)

            response = process_chat(chain, query, chat_history)
            chat_history.append(HumanMessage(content=query))
            chat_history.append(AIMessage(content=response))

            # Check if any static sources are matched based on the query
            sources = render_buttons(query)

            # Save the interaction to a file in real-time
            save_to_file(query, response, sources)
            print("\n\nChat session saved. Continue asking...\n")


    except KeyboardInterrupt:
        print("\nExiting chat session. Goodbye!")

if __name__ == "__main__":
    main()
