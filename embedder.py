from langchain_chroma import Chroma
from langchain.schema import Document
from config import embedding_function
import json


def create_vector_store(input_file="scraped_contents.json", db_dir="chroma_db"):
    # Load content from file
    with open(input_file, "r") as f:
        scraped_content = json.load(f)

    # Prepare documents with metadata
    documents = [
        Document(
            page_content=data["content"],
            metadata={"source": data["url"]}
        )
        for data in scraped_content.values()
    ]

    # Create and persist ChromaDB Vectorstore
    vectorstore = Chroma.from_documents(documents, embedding_function, persist_directory=db_dir)
    print(f"Vector embeddings stored in '{db_dir}'.")

if __name__ == "__main__":
    create_vector_store()
