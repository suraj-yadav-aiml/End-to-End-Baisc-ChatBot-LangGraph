---
title: Basic Chatbot with LangGraph
emoji: 🤖
colorFrom: blue
colorTo: yellow
sdk: streamlit
sdk_version: 1.44.0
app_file: app.py
pinned: false
license: mit
short_description: A simple chatbot created with langgraph
---

# 🤖 Basic Chatbot with LangGraph

A chatbot built with LangGraph that supports multiple LLM providers and tool integrations.

## 📋 Overview

This project provides an end-to-end implementation of a modular chatbot using LangGraph for workflow orchestration. It supports both basic conversation capabilities and enhanced functionality through tool integration. The framework is designed to be adaptable, allowing users to easily switch between different LLM providers (Groq and OpenAI) and integrate external tools as needed.

### Key Features

- 🔄 Multiple LLM provider support (Groq and OpenAI)
- 🛠️ Tool integration capability with Tavily search
- 📊 Streamlit-based user interface for easy interaction
- 📈 Extensible architecture for adding new features
- 🧩 Graph-based workflow design using LangGraph

## 🔧 Technologies Used

- **Languages**: Python
- **Frameworks**: LangGraph, LangChain
- **UI**: Streamlit
- **LLM Providers**: OpenAI, Groq
- **Tools**: Tavily Search
- **Deployment**: Hugging Face Spaces

## ⚙️ Installation

### Prerequisites

- Python 3.8+
- Git
- API keys for LLM providers (OpenAI and/or Groq)
- API key for Tavily Search (for tool-enhanced functionality)

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/suraj-yadav-aiml/End-to-End-Baisc-ChatBot-LangGraph.git
cd Basic-Chatbot-LangGraph
```

2. **Create and activate a virtual environment**

```bash
# On Windows
python -m venv agentic-ai-venv
agentic-ai-venv\Scripts\activate

# On macOS/Linux
python -m venv agentic-ai-venv
source agentic-ai-venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up API keys (optional, can also be entered in UI)**
   
Create a `.env` file in the root directory:

```bash
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## 🚀 Usage

### Running the Application

Start the Streamlit application:

```bash
python app.py
```

or directly using Streamlit:

```bash
streamlit run app.py
```

Then navigate to the URL displayed in your terminal (typically http://localhost:8501).

### Using the Chatbot

1. In the sidebar, select an LLM provider (OpenAI or Groq)
2. Enter your API key(s) for the selected provider
3. Choose a use case:
   - Basic Chatbot: Simple conversational agent
   - Chatbot with Tools: Enhanced agent with Tavily search capability
4. For "Chatbot with Tools," enter your Tavily API key
5. Enter your message in the chat input field and start the conversation

### Example Code for Integration

If you want to use the chatbot programmatically:

```python
from src.basicchatbot.llms import get_llm
from src.basicchatbot.graph.graph_builder import GraphBuilder

# Set up configuration
user_input = {
    'selected_llm': 'OpenAI',
    'selected_openai_model': 'gpt-3.5-turbo-0125',
    'OPENAI_API_KEY': 'your_api_key_here',
    'selected_usecase': 'Basic Chatbot'
}

# Initialize LLM
llm = get_llm(llm_name=user_input['selected_llm'], user_input=user_input)

# Build graph
graph_builder = GraphBuilder(model=llm)
graph = graph_builder.setup_graph(user_input['selected_usecase'])

# Use the chatbot
result = graph.invoke(input={"messages": "Hello, how can you help me today?"})
print(result["messages"].content)
```

## 📁 Project Structure

```
📂 End-to-End-Basic-Chatbot-with-LangGraph/
  📄 app.py                # Entry point for the application
  📄 requirements.txt      # Dependencies
  📂 src/
    📂 basicchatbot/
      📄 main.py           # Main application logic
      📂 graph/            # LangGraph workflow definitions
      📂 llms/             # LLM provider implementations
      📂 nodes/            # Node definitions for the graph
      📂 state/            # State management for the chatbot
      📂 tools/            # Tool integrations
      📂 ui/               # Streamlit UI components
```

### Key Components

- **graph_builder.py**: Constructs different chatbot workflows based on selected use cases
- **llms/**: Contains provider-specific implementations (OpenAI, Groq)
- **nodes/**: Defines the behavior of graph nodes
- **tools/**: Manages external tool integrations like Tavily Search
- **ui/**: Handles UI configuration and display logic

## 🔍 Architecture

The application follows a modular architecture:

1. **UI Layer**: Streamlit interface for user interaction
2. **LLM Layer**: Abstraction for different LLM providers
3. **Graph Layer**: LangGraph-based workflow orchestration
4. **Tool Layer**: External tool integration

The workflow is orchestrated using LangGraph's `StateGraph`, which manages the flow of information between different components.

## 🌐 Deployment

The project is configured for automatic deployment to Hugging Face Spaces via GitHub Actions. When changes are pushed to the main branch, the workflow in `.github/workflows/main.yaml` handles deployment.



- GitHub Repository: [https://github.com/suraj-yadav-aiml/End-to-End-Baisc-ChatBot-LangGraph](https://github.com/yourusername/Basic-Chatbot-LangGraph)
- Hugging Face Space: [https://huggingface.co/spaces/Suraj-Yadav/Basic-Chatbot-LangGraph](https://huggingface.co/spaces/Suraj-Yadav/Basic-Chatbot-LangGraph)