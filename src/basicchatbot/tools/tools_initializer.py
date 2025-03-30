from typing import List, Any
from langgraph.prebuilt import ToolNode
from src.basicchatbot.tools import ToolManager


class ToolInitializer:
    """Initializes and manages multiple tools using ToolManager."""

    def __init__(self):
        """Initialize ToolInitializer with a ToolManager instance."""
        self.tool_manager = ToolManager()

    def get_all_tools(self) -> List[Any]:
        """
        Retrieve all tools currently added to the manager.

        Returns:
            List[Any]: A list of all registered tools.
        """
        return self.tool_manager.get_tools()

    def create_tool_node(self) -> ToolNode:
        """
        Create a ToolNode with all registered tools.

        Returns:
            ToolNode: A LangGraph ToolNode containing all active tools.
        """
        return self.tool_manager.create_tool_node()

