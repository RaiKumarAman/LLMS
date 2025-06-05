# LLMS – LangChain LLM Examples and Demos

**LLMS** is a showcase of Large Language Model (LLM) applications built with LangChain. It provides hands-on examples of working with chat models, chains, prompts, and structured outputs. The repository includes demo scripts and notebooks illustrating how to use LangChain with Google Gemini (PaLM) and Hugging Face models, apply different chain workflows (conditional, parallel, sequential, etc.), and enforce structured JSON outputs using Pydantic output parsers. The main goal is to help developers learn and compare LLM techniques by providing concrete code samples and patterns.

This project is ideal for developers, researchers, and AI enthusiasts looking to:

* Learn how to build applications using LangChain
* Explore multi-model and multi-step processing with LLMs
* Understand prompt engineering and chaining mechanisms
* Validate and enforce structured outputs from language models

## Features

### 1. Chatbot Interfaces

Chatbot interfaces demonstrate the core use of chat-based LLMs in both open and closed model ecosystems.

* **Definition:** A chatbot is a software application that uses natural language processing (NLP) to simulate human conversation.
* **Example:** `Google_Chat_Model.py` uses Gemini for generating responses to user inputs. `HuggingFace_Chat_Model.py` queries a Hugging Face model using `HuggingFaceHub` integration.

### 2. LangChain Chains

Chains allow combining multiple LLM calls or operations into one logical flow.

* **Definition:** A chain is a pipeline of LLM calls and transformations that work together to produce a final result.
* **Example:**

  * `simple_chain.py`: A single-step LLM call.
  * `Sequential_Chain.py`: Chains multiple prompts in order.
  * `Parallel_Chain.py`: Executes multiple prompts concurrently and merges outputs.
  * `Conditional_Chain.py`: Selects chain logic based on a condition (e.g., input type).

### 3. Prompt Engineering

Crafting effective prompts is essential to get desirable results from LLMs.

* **Definition:** Prompt engineering is the art of structuring input instructions to LLMs to generate accurate and relevant outputs.
* **Example:** `prompt_dynamic.py` lets users input a research topic and select tone and length to generate a styled summary. `chatbot.py` enables a conversation loop with Gemini using custom message formatting.

### 4. Structured Output

Ensures LLM outputs are in predefined formats like JSON.

* **Definition:** Structured output parsing uses schemas (e.g., via Pydantic) to enforce data integrity and parseability.
* **Example:** `Structured_Output/output_parsers.ipynb` validates responses that match a "Student" JSON schema using `PydanticOutputParser`.

### 5. Interactive UI Demos

Interactive frontends built with Streamlit provide user-friendly LLM interaction.

* **Definition:** Streamlit is a Python framework for quickly building interactive web apps.
* **Example:** `prompt_ui.py` launches a GUI for writing prompts and viewing LLM results live.

### 6. Multi-model Support

The codebase supports integration with both proprietary and open-source LLMs.

* **Definition:** Multi-model support allows using different LLM providers within the same workflow.
* **Example:** The system supports Google Gemini via `langchain_google_genai` and Hugging Face models via `langchain_huggingface`.

## Tech Stack

* **Programming Language:** Python
* **LLM Framework:** LangChain
* **LLMs and APIs:** Google Gemini (via `langchain_google_genai`), Hugging Face (via `langchain_huggingface`)
* **Prompting:** LangChain prompt templates, chat message formatting
* **Output Parsing:** Pydantic models with `PydanticOutputParser`
* **UI:** Streamlit
* **Other Libraries:**

  * `dotenv` for loading environment variables
  * `transformers` and `huggingface-hub` for Hugging Face integration
  * `openai`, `scikit-learn`, `numpy` for extended capabilities

## Installation

1. **Clone the repo:**

   ```bash
   git clone https://github.com/RaiKumarAman/LLMS.git
   cd LLMS
   ```

2. **Install requirements:**

   ```bash
   pip install -r "Langchain models/requirements.txt"
   ```

3. **Set environment variables:**
   Create a `.env` file and include your API keys:

   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Verify installation:**

   ```bash
   python "Langchain models/test.py"
   ```

## Usage

* **Chat Models:**

  ```bash
  python "Langchain models/ChatModels/Google_Chat_Model.py"
  python "Langchain models/ChatModels/HuggingFace_Chat_Model.py"
  ```

* **Chains:**

  ```bash
  python Langchain_Chains/simple_chain.py
  python Langchain_Chains/Sequential_Chain.py
  python Langchain_Chains/Parallel_Chain.py
  python Langchain_Chains/Conditional_Chain.py
  ```

* **Prompt Apps:**

  ```bash
  streamlit run Langchain_prompts/prompt_dynamic.py
  streamlit run Langchain_prompts/prompt_ui.py
  ```

* **Structured Output:**
  Open `Structured_Output/output_parsers.ipynb` or `with_structured_outpu.ipynb` in Jupyter.

## Project Structure

```
LLMS/
├── Langchain models/
│   ├── ChatModels/
│   ├── requirements.txt
│   └── test.py
├── Langchain_Chains/
├── Langchain_prompts/
├── Structured_Output/
```

## Contributing

Feel free to fork the project, open issues, and submit pull requests for new features, fixes, or improvements.

Guidelines:

* Follow PEP8 code style
* Document your code
* Add meaningful commit messages
* Include test examples for new scripts

## License

This project does not include a LICENSE file and is not explicitly licensed. By default, all rights are reserved. If you wish to reuse any code, please contact the author or assume it is proprietary until a license is added.

## Author and Contact

**Author:** RaiKumarAman
**GitHub:** [github.com/RaiKumarAman](https://github.com/RaiKumarAman)
---
