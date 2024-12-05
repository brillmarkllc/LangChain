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
  const stream = await llmChain.stream({
    context: "AI chatbot",
    text: "What does brain rot mean?",
  });
  for await (const chunk of stream) {
    process.stdout.write(chunk);
  }
  console.log();
})();
