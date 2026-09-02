# Assignment completed 
> LangChain + OpenAI + LangSmith

### What we built
> A simple Python application using LangChain to send a prompt to an OpenAI model, print the response, and trace the execution in LangSmith.

### Flow
Prompt → LangChain → OpenAI Model → Output
                  ↘
                   LangSmith Trace
### What we learned:
•	LangChain connects and manages the Prompt → Model → Output flow. 
•	Chain (|) joins the individual steps into a pipeline. 
•	.invoke() executes the chain. 
•	OpenAI API Key gives the application permission to use the OpenAI model. 
•	LangSmith API Key allows the application to send traces to our LangSmith account. 
•	LangSmith lets us see the input, output and execution/timing information. 
•	.env keeps API keys outside the Python code. 

### Other concepts learned today
•	foundation for RAG
> These were learned today but NOT used in this assignment:
•	Concept	Easy meaning
•	Data Ingestion	Load our own documents/data
•	Text Splitter	Break large documents into smaller chunks
•	Chunks	Small pieces of the original document
•	Embeddings	Convert text/chunks into numerical vectors
•	Vector Store / FAISS	Store vectors and search them by meaning
•	Retriever	Fetch the most relevant chunks for a question
•	RAG	Give retrieved information to the AI so it can answer using our data
•	This follows the sequence in your session notes: ingestion → splitting → embedding → vector store → retriever. 

### Easy memory flow for today's learning
LANGCHAIN BASICS — USED TODAY
Prompt → Chain → Model → Output
                         ↓
                    LangSmith

RAG CONCEPTS — LEARNED, NOT USED YET
 Load →Chunk →Embed → FAISS
                                  ↓
                              Retrieve
                                  ↓
                              AI → Answer

## Key distinction
Today's assignment was mainly a LangChain fundamentals + LangSmith tracing exercise. The other concepts you learned today prepare you for the next stage: building a RAG application using your own data.
