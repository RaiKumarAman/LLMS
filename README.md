# LLMS – LangChain LLM Examples and Demos

**LLMS** is a showcase of Large Language Model (LLM) applications built with LangChain. It provides hands-on examples of working with chat models, chains, prompts, and structured outputs. The repository includes demo scripts and notebooks illustrating how to use LangChain with Google Gemini (PaLM) and Hugging Face models, apply different chain workflows (conditional, parallel, sequential, etc.), and enforce structured JSON outputs using Pydantic output parsers. The main goal is to help developers learn and compare LLM techniques by providing concrete code samples and patterns.

## Features

* **Chatbot Interfaces:** Sample chat programs using `ChatGoogleGenerativeAI` (Gemini) and Hugging Face endpoints. For example, `Langchain models/ChatModels/Google_Chat_Model.py` shows a simple prompt to Gemini, and `HuggingFace_Chat_Model.py` invokes a Hugging Face LLM.
* **LangChain Chains:** Four example chain scripts under `Langchain_Chains` demonstrate different workflows: `simple_chain.py`, `Sequential_Chain.py`, `Parallel_Chain.py`, and `Conditional_Chain.py`. These show how to compose prompts and models into pipelines, including branching and parallel execution. For instance, the conditional chain combines a sentiment-classifier chain with a response-generator chain using LangChain’s `RunnableParallel` and `RunnableBranch`.
* **Prompt Engineering:** Multiple prompt templates are provided under `Langchain_prompts`. These include dynamic chat templates, message placeholders, and Streamlit UIs. Notable examples are `prompt_dynamic.py` (a Streamlit app that generates research paper summaries based on user-selected style and length) and `chatbot.py` (a REPL loop using Gemini). The prompts illustrate using system/human/AI messages, placeholders (e.g. loading past chat history), and interactive inputs.
* **Structured Output:** The `Structured_Output` folder contains examples of enforcing JSON structures in LLM outputs. A JSON schema (`json__schema.json`) defines a "Student" object, and accompanying notebooks (`output_parsers.ipynb`, `with_structured_outpu.ipynb`) demonstrate using LangChain’s `PydanticOutputParser` to validate and parse LLM responses into that schema. This shows how to guarantee well-structured answers from the model.

These key functionalities are supported by code and documentation within the repo, making LLMS a practical reference for learning LangChain techniques.

## Tech Stack

* **Programming Language:** Python (with Jupyter notebooks).
* **LLM Framework:** [LangChain](https://github.com/langchain-ai/langchain) and **langchain-core** for building chains and prompts.
* **LLMs and APIs:** Google Gemini via `langchain_google_genai` (PaLM API) and Hugging Face (`langchain_huggingface`). Example imports: `ChatGoogleGenerativeAI` and `ChatHuggingFace`.
* **Prompting:** LangChain prompt templates (`PromptTemplate`, `ChatPromptTemplate`), placeholders (`MessagesPlaceholder`), and message classes (`SystemMessage`, `HumanMessage`, `AIMessage`).
* **Output Parsing:** [Pydantic](https://pydantic-docs.helpmanual.io/) models with `PydanticOutputParser` to enforce structured JSON responses.
* **Utilities:** `dotenv` for environment variables, plus optional libraries like `streamlit` for UIs. The provided `requirements.txt` lists core dependencies (langchain, transformers, python-dotenv, etc.).

Together, these tools allow running LLM calls (to Gemini or HF models) and composing complex pipelines of LLM calls and logic.

## Installation

To run this project locally, you’ll need Python 3.8+ and the listed dependencies. For example:

1. **Clone the repo:**

   ```bash
   git clone https://github.com/RaiKumarAman/LLMS.git
   cd LLMS
   ```

2. **Install requirements:**
   Install the required packages. You can use `pip` and the provided requirements snippet:

   ```bash
   pip install langchain langchain-core langchain-openai openai \
               langchain-google-genai google-generativeai \
               langchain-huggingface transformers huggingface-hub \
               python-dotenv numpy scikit-learn
   ```

   (Or use `requirements.txt` in `Langchain models/requirements.txt` which lists these libraries.)

3. **Set environment variables:**
   Create a `.env` file in the project root and add your API keys (e.g. `GOOGLE_API_KEY` or `GOOGLE_PROJECT_ID` for Gemini). Example (using a placeholder):

   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

   Ensure the .env file is loaded (the code calls `load_dotenv()`).

4. **Verify installation:**
   You can run `test.py` to check the LangChain version:

   ```bash
   python "Langchain models/test.py"
   ```

   which prints the installed LangChain version.

## Usage

Each folder contains example scripts or notebooks. You can run them to see the demos in action:

* **Chat Models:**

  * Run `Langchain models/ChatModels/Google_Chat_Model.py` to invoke Gemini on a query.
  * Run `Langchain models/ChatModels/HuggingFace_Chat_Model.py` to query a Hugging Face model via API.

* **Chains:**

  * Execute any chain file (e.g. `Langchain_Chains/Conditional_Chain.py`) with Python to see combined LLM calls. Each script defines prompts and chains them; for example, the conditional chain classifies feedback and then generates an appropriate response.

* **Prompt Examples (UI):**

  * Use Streamlit for the UI scripts. For instance:

    ```bash
    streamlit run "Langchain_prompts/prompt_dynamic.py"
    ```

    This launches a web app where you can select a research paper and ask the LLM to summarize it according to specified style and length.
  * Similarly, `prompt_ui.py` provides a simple text-input interface.

* **Structured Output:**

  * Open the notebooks in `Structured_Output` with Jupyter. They demonstrate how to use LangChain’s output parsers with the provided JSON schema. The code shows creating a Pydantic model (`Feedback`) and using `PydanticOutputParser` to parse LLM output into that model. Run the cells to see LLM responses formatted as JSON.

## Project Structure

```
LLMS/
├── Langchain models/
│   ├── ChatModels/
│   │   ├── Google_Chat_Model.py        # Example using Google Gemini (PaLM):contentReference[oaicite:29]{index=29}
│   │   ├── HuggingFace_Chat_Model.py  # Example using Hugging Face LLM API:contentReference[oaicite:30]{index=30}
│   │   └── HuggingFace_Local.py       # (Commented-out code for local HF pipeline)
│   ├── requirements.txt               # List of pip dependencies:contentReference[oaicite:31]{index=31}
│   └── test.py                        # Simple test script (prints langchain version):contentReference[oaicite:32]{index=32}
│
├── Langchain_Chains/
│   ├── simple_chain.py       # Basic single-prompt LLM example
│   ├── Sequential_Chain.py   # Serially passes output through multiple LLM calls
│   ├── Parallel_Chain.py     # Runs multiple LLM calls in parallel (RunnableParallel)
│   ├── Conditional_Chain.py  # Branching logic based on LLM result (RunnableBranch)
│
├── Langchain_prompts/
│   ├── chatbot.py             # Console chat loop using Gemini:contentReference[oaicite:33]{index=33}
│   ├── chat_history.txt       # Sample conversation history file:contentReference[oaicite:34]{index=34}
│   ├── message_dynamic.py     # ChatPromptTemplate with dynamic variables:contentReference[oaicite:35]{index=35}
│   ├── message_placeholder.py # ChatPromptTemplate using MessagesPlaceholder for history:contentReference[oaicite:36]{index=36}:contentReference[oaicite:37]{index=37}
│   ├── messages.py            # Building message list and invoking LLM:contentReference[oaicite:38]{index=38}
│   ├── prompt_dynamic.py      # Streamlit app for research paper summarization:contentReference[oaicite:39]{index=39}
│   └── prompt_ui.py           # Simple Streamlit interface for LLM queries:contentReference[oaicite:40]{index=40}
│
└── Structured_Output/
    ├── json__schema.json      # JSON Schema defining a "Student" object:contentReference[oaicite:41]{index=41}
    ├── output_parsers.ipynb   # Notebook demonstrating PydanticOutputParser usage:contentReference[oaicite:42]{index=42}
    └── with_structured_outpu.ipynb  # Similar structured output demo notebook
```

Each directory is organized by concept (models, chains, prompts, output parsing) and contains sample code as described above.

## Contributing

Contributions are welcome! If you find issues or have ideas for improvements, please open an issue or submit a pull request. You can fork the repository, make changes (e.g. adding new LLM examples or improving docs), and send a PR. Be sure to follow Python best practices and include clear descriptions of any new features. Discussions on GitHub are open for general questions about extending LLMS.

## License

This project does not include a LICENSE file and is not explicitly licensed. By default, all rights are reserved. If you wish to reuse any code, please contact the author or assume it is proprietary until a license is added.

## Author and Contact

**Author:** *RaiKumarAman* (GitHub username).

For more projects or inquiries, you can find the author’s GitHub profile at [github.com/RaiKumarAman](https://github.com/RaiKumarAman) or open an issue in this repository.
