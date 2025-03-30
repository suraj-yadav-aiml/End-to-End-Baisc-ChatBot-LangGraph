from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
from typing import List, Any


class ToolManager:
    """Manages tools for the chatbot, allowing dynamic addition of multiple tools."""

    def __init__(self, tools: List[Any] = None):
        """
        Initialize the ToolManager with an optional list of tools.

        Args:
            tools (List[Any], optional): A list of initial tools. Defaults to None.
        """
        self.tools: List[Any] = tools if tools else []

    def add_tool(self, tool: Any) -> None:
        """
        Add a single tool to the tool list.

        Args:
            tool (Any): A tool instance that implements the required API.
        """
        if tool is not None:
            self.tools.append(tool)
        else:
            raise ValueError("Tool cannot be None.")

    def add_tools(self, *new_tools: Any) -> None:
        """
        Add multiple tools at once.

        Args:
            *new_tools (Any): Variable-length argument list of tools.
        """
        if not new_tools:
            raise ValueError("No tools provided. Please add at least one tool.")
        self.tools.extend(new_tools)

    def get_tools(self) -> List[Any]:
        """
        Retrieve the list of registered tools.

        Returns:
            List[Any]: A list of initialized tool instances.
        """
        return self.tools

    def create_tool_node(self) -> ToolNode:
        """
        Creates and returns a ToolNode for the graph using registered tools.

        Returns:
            ToolNode: A LangGraph ToolNode containing all registered tools.
        """
        if not self.tools:
            raise ValueError("No tools registered. Please add tools before creating a ToolNode.")
        return ToolNode(tools=self.tools)

