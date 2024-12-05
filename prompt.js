const { ChatPromptTemplate } = require("@langchain/core/prompts");

const systemTemplate = "You are an entertaining AI chatbot. Your goal is to answer a user's query in a concise, yet sarcastic tone.";
const userTemplate = "{text}";

const promptTemplate = ChatPromptTemplate.fromMessages([
  ["system", systemTemplate],
  ["user", userTemplate],
]);

module.exports = { promptTemplate };
