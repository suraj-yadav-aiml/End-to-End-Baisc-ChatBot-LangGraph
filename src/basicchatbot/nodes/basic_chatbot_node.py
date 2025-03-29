
from src.basicchatbot.state.state import BasicChatBotState
from typing import Dict, Any
from langchain_core.messages import AIMessage

class BasicChatBotNode:
    """A node in a basic chatbot graph that processes user messages using an LLM model."""
    
    def __init__(self, model):
        self.llm = model

    def node(self, state: BasicChatBotState) -> Dict[str, AIMessage]:
        """
        Processes the chatbot state by invoking the LLM model with user messages.

        Args:
            state (BasicChatBotState): The current state containing chat messages.

        Returns:
            Dict[str, Any]: Updated state with the model's response.
        """
        messages = state.get('messages', [])
        
        if not messages:
            return {'messages': 'ERROR: `messages` field not found in `BasicChatBotState` class'}

        try:
            response = self.llm.invoke(input=messages)
        except Exception as e:
            return {'messages': f'Error processing request: {str(e)}'}

        return {'messages': response}
