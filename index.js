const { ChatOpenAI } = require("@langchain/openai");
const { StringOutputParser } = require("@langchain/core/output_parsers");
const { promptTemplate } = require("./prompt");
require("dotenv").config();

// specify the model
const model = new ChatOpenAI({
  model: "gpt-4",
  openAIApiKey: process.env.OPENAI_API_KEY,
});

// specify the parser
const parser = new StringOutputParser();

// build the llm chain
const llmChain = promptTemplate.pipe(model).pipe(parser);

(async () => {
  const response = await llmChain.invoke({
    language: "Bengali",
    text: "Hello, how are you?",
  });
  console.log(response);
})();
