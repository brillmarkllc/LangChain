const { ChatPromptTemplate } = require("@langchain/core/prompts");

const systemTemplate = "You are an AI chatbot. Your goal";
const userTemplate = "{text}";

const promptTemplate = ChatPromptTemplate.fromMessages([
  ["system", systemTemplate],
  ["user", userTemplate],
]);

module.exports = { promptTemplate };
