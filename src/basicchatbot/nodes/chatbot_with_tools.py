from typing import Any, List
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage
from src.basicchatbot.state.state import BasicChatBotState


class ChatbotWithToolsNode:
    """Handles chatbot interactions using an LLM and associated tools."""

    def __init__(self, model: BaseChatModel, tools: List[Any]) -> None:
        """
        Initialize the chatbot node with a model and tools.

        Args:
            model (BaseChatModel): The language model used for processing messages.
            tools (List[Any]): A list of tools that can be used with the chatbot.
        """
        self.llm = model
        self.tools = tools

    def node(self, state: BasicChatBotState) -> dict:
        """
        Processes the chatbot state and generates a response.

        Args:
            state (BasicChatBotState): The current chatbot state containing messages.

        Returns:
            dict: A dictionary containing the chatbot's response messages.
        """
        try:
            messages = state.get("messages", [])
            if not messages:
                return {"messages": [AIMessage(content="ERROR: `messages` key is missing in the state. Contact developer to fix.")]}

            response = self.llm.bind_tools(self.tools).invoke(input=messages)

            return {"messages": [response] }

        except Exception as e:
            return {"messages": [AIMessage(content=f"Error processing request: {str(e)}")]}
