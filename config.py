from langchain_openai import ChatOpenAI
from prompt import chat_prompt
from dotenv import load_dotenv
import os


# get OpenAI API key from env file
load_dotenv()
API_KEY = os.environ.get('OPENAI_API_KEY')


# Initialize the OpenAI LLM with GPT-4o
llm = ChatOpenAI(model="gpt-4o", 
                 temperature=0, 
                 openai_api_key=API_KEY)


# Create an LLMChain with the prompt template
chain = chat_prompt | llm