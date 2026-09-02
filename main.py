from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load variables from the .env file
load_dotenv()

# Create the prompt
prompt = ChatPromptTemplate.from_template(
    "Answer the following in simple English: {question}"
)

# Connect to an OpenAI model through LangChain
model = ChatOpenAI()

# Convert the model response into normal text
output_parser = StrOutputParser()

# Create the LangChain pipeline
chain = prompt | model | output_parser

# Run the chain
response = chain.invoke(
    {"question": "Explain +M mesomeric effect."}
)

# Display the result
print(response)