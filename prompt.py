from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)

# System message to set the role of the model
system_message = """
You are an AI Chatbot. You answer user's question about the business.
"""

# Human message for similarity detection
human_message = """
User's Question: {question}

Now, answer the question.
"""


# Define the system message template (to specify the role of the model)
system_message_template = SystemMessagePromptTemplate.from_template(
    system_message)

# Define the human message prompt template (which takes input variables)
human_message_template = HumanMessagePromptTemplate.from_template(
    human_message)

# Combine both the system and human messages in one prompt
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_template, human_message_template])