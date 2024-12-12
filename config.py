from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.callbacks import StreamingStdOutCallbackHandler
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os


# get OpenAI API key from env file
load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# Initialize pinecone
pc = Pinecone(api_key=os.environ.get('PINECONE_API_KEY'))

# Pinecone index name
PINECONE_INDEX = os.environ.get('PINECONE_INDEX')
if PINECONE_INDEX not in pc.list_indexes().names():
    pc.create_index(
        name=PINECONE_INDEX, 
        dimension=1536, 
        metric='euclidean',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-west-2'
        )
    )
pc_index = pc.Index(PINECONE_INDEX)


# Initialize OpenAI Embeddings
embedding_function = OpenAIEmbeddings(model="text-embedding-ada-002", 
                                   api_key=OPENAI_API_KEY)

# Initialize the OpenAI LLM with GPT-4o
llm = ChatOpenAI(temperature=0,
             api_key=OPENAI_API_KEY,
             model='gpt-4o',
             callbacks=[StreamingStdOutCallbackHandler()],
             streaming=True)