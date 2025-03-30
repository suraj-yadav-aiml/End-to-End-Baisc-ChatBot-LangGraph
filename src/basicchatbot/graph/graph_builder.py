import streamlit as st
from typing import Optional
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph import START, END, StateGraph
from langgraph.prebuilt import tools_condition
from src.basicchatbot.nodes import BasicChatBotNode, ChatbotWithToolsNode
from src.basicchatbot.state.state import BasicChatBotState
from src.basicchatbot.tools import ToolInitializer


class GraphBuilder:
    """Builds different chatbot workflows based on the selected use case."""

    def __init__(self, model):
        self.llm = model
        self.workflow = StateGraph(BasicChatBotState)
        self.tool_initializer = ToolInitializer()

    def _basic_chatbot_build_graph(self) -> None:
        """Builds a simple chatbot graph without external tools."""
        try:
            self.workflow.add_node("chatbot", BasicChatBotNode(model=self.llm).node)
            self.workflow.add_edge(START, "chatbot")
            self.workflow.add_edge("chatbot", END)
        except Exception as e:
            st.error(f"Error in Basic Chatbot Graph: {str(e)}")

    def _chatbot_with_tools_build_graph(self) -> None:
        """Builds a chatbot graph with external tool integrations."""
        try:
            self.tool_initializer.tool_manager.add_tools(  # add comma seperated tools
                TavilySearchResults(max_results=5)
            )
            tools = self.tool_initializer.get_all_tools()
            if not tools:
                st.warning("No tools available. The chatbot may not function as expected.")
            
            tool_node = self.tool_initializer.create_tool_node()

            self.workflow.add_node("chatbot", ChatbotWithToolsNode(model=self.llm, tools=tools).node)
            self.workflow.add_node("tools", tool_node)

            self.workflow.add_edge(START, "chatbot")
            self.workflow.add_conditional_edges(
                "chatbot",
                tools_condition,
                {
                    "tools": "tools",
                    "__end__": END
                }
            )
            self.workflow.add_edge("tools", "chatbot")
        except Exception as e:
            st.error(f"Error in Chatbot with Tools Graph: {str(e)}")

    def setup_graph(self, usecase: str) -> Optional[StateGraph]:
        """
        Sets up the appropriate chatbot graph based on the selected use case.

        Args:
            usecase (str): The chatbot type ("Basic Chatbot" or "Chatbot with Tools").

        Returns:
            Optional[StateGraph]: The compiled chatbot workflow or None if an error occurs.
        """
        usecase_mapping = {
            "Basic Chatbot": self._basic_chatbot_build_graph,
            "Chatbot with Tools": self._chatbot_with_tools_build_graph,
        }

        build_graph = usecase_mapping.get(usecase)

        if build_graph:
            try:
                build_graph()
                return self.workflow.compile()
            except Exception as e:
                st.error(f"Error compiling the graph: {str(e)}")
                return None
        else:
            st.error(f"Invalid use case: {usecase}. Choose from {list(usecase_mapping.keys())}.")
            return None
