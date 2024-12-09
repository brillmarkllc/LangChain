from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.callbacks import StreamingStdOutCallbackHandler
from dotenv import load_dotenv
import os


# get OpenAI API key from env file
load_dotenv()
API_KEY = os.environ.get('OPENAI_API_KEY')

# Initialize OpenAI Embeddings
embedding_function = OpenAIEmbeddings(model="text-embedding-ada-002", 
                                   api_key=API_KEY)

# Initialize the OpenAI LLM with GPT-4o
llm = ChatOpenAI(temperature=0,
             api_key=API_KEY,
             model='gpt-4o',
             callbacks=[StreamingStdOutCallbackHandler()],
             streaming=True)