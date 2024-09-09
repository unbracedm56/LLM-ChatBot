# ChatBot

This is a chatbot application built using Streamlit and Langchain. The bot leverages the Groq API and the Llama 3 model to engage in conversational AI. Users can interact with the bot, and the conversation history is stored using an in-memory chat history.

## Features

- Chat interface with a helpful assistant
- Supports language customization during interaction
- In-memory message history for chat sessions
- Configurable model and chat prompt

## Requirements

To run this project, you will need to install the following dependencies:

- Python 3.7 or higher
- Streamlit
- Langchain
- Groq API

You can install the required packages using `pip`:

```bash
pip install streamlit langchain langchain_groq
```

## Getting Started

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```
### 2. Set up your environment:

Create a `.env` file or set the `GROQ_API_KEY` environment variable with your Groq API key.

Example `.env` file:

```bash
GROQ_API_KEY=your_api_key_here
```

### 3. Run the chatbot application
```bash
streamlit run ChatBot.py
```

## Configuration

- The chatbot is initialized with the `Llama 3` model.
- Users can change the language during the chat session via the sidebar input.

## Example Usage

1. Start the chatbot by running the `ChatBot.py` file.
2. Interact with the chatbot by typing messages.
3. You can change the language of the assistant by entering a new language in the sidebar input.
