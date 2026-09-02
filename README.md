# Assignment completed 
> LangChain + OpenAI + LangSmith

### What we built
> A simple Python application using LangChain to send a prompt to an OpenAI model, print the response, and trace the execution in LangSmith.

### Flow
Prompt → LangChain → OpenAI Model → Output
                  ↘
                   LangSmith Trace
### What we learned:
- LangChain connects and manages the Prompt → Model → Output flow. 
- Chain (|) joins the individual steps into a pipeline. 
- .invoke() executes the chain. 
- OpenAI API Key gives the application permission to use the OpenAI model. 
- LangSmith API Key allows the application to send traces to our LangSmith account. 
- LangSmith lets us see the input, output and execution/timing information. 
- .env keeps API keys outside the Python code.

### Prompt
![Alt text](https://github.com/learn-genai-labs/LangChain-OpenAI-LangSmith/blob/5a63d2fac1648681d026c503e1f49ff401252e67/Assets/Prompt.png)

### LangSmith Tracing
![Alt text](https://github.com/learn-genai-labs/LangChain-OpenAI-LangSmith/blob/40ed625206dea4155dc10a50738b09562a44754e/Assets/LangSmith.png)




### Other concepts learned today
- foundation for RAG
> These were learned today but NOT used in this assignment:
- Concept	Easy meaning
- Data Ingestion	Load our own documents/data
- Text Splitter	Break large documents into smaller chunks
- Chunks	Small pieces of the original document
- Embeddings	Convert text/chunks into numerical vectors
- Vector Store / FAISS	Store vectors and search them by meaning
- Retriever	Fetch the most relevant chunks for a question
- RAG	Give retrieved information to the AI so it can answer using our data
- This follows the sequence in your session notes: ingestion → splitting → embedding → vector store → retriever. 

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

### Understanding Gained from Today’s Questions
- Why OpenAI API Key? → Gives our Python application permission to access and use the OpenAI model.
- What if OpenAI API Key is removed? → The OpenAI model cannot be accessed, so the application cannot generate the answer, unless the key is available from another environment source.
- Why LangSmith API Key? → Authenticates our application with our LangSmith account so traces can be sent there.
- OpenAI Key vs LangSmith Key → They have different jobs: OpenAI Key = use the model; LangSmith Key = send traces to LangSmith. Today's notes configure both separately.
- Why .env? → Keeps API keys outside main.py instead of hard-coding secrets into the program. Your notes specifically covered loading keys from .env.
- Why LANGSMITH_TRACING=true? → Turns LangSmith tracing ON.
- Why LANGSMITH_PROJECT? → Tells LangSmith which project should contain the application's traces.
- Why LangChain when we can call OpenAI directly? → A simple prompt can go directly to a model. LangChain becomes useful for connecting multiple application steps such as Prompt → Model → Output and, later, RAG components

### Easy Memory

🔑 OpenAI Key = ACCESS AI
🔑 LangSmith Key = ACCESS TRACING
🔗 LangChain = CONNECT STEPS
🤖 OpenAI = GENERATE ANSWER
🔍 LangSmith = TRACE / MONITOR
🔒 .env = KEEP KEYS OUT OF CODE

## Key distinction
Today's assignment was mainly a LangChain fundamentals + LangSmith tracing exercise. The other concepts you learned today prepare you for the next stage: building a RAG application using your own data.
