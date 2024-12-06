from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)

# System message to set the role of the model
system_message = """
You are an entertaining {context}. Your goal is to answer a user's query in a concise, yet sarcastic tone.
"""

# Human message for similarity detection
human_message = "{text}"


# Define the system message template (to specify the role of the model)
system_message_template = SystemMessagePromptTemplate.from_template(
    system_message)

# Define the human message prompt template (which takes input variables)
human_message_template = HumanMessagePromptTemplate.from_template(
    human_message)

# Combine both the system and human messages in one prompt
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_template, human_message_template])