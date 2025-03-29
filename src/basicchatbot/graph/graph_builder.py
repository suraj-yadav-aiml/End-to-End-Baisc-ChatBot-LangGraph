import streamlit as st
from typing import Optional
from langgraph.graph import START, END, StateGraph
from src.basicchatbot.nodes.basic_chatbot_node import BasicChatBotNode
from src.basicchatbot.state.state import BasicChatBotState


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.workflow = StateGraph(BasicChatBotState)
    
    def basic_chatbot_build_graph(self):

        self.workflow.add_node("chatbot", BasicChatBotNode(model=self.llm).node)
        
        self.workflow.add_edge(START, "chatbot")
        self.workflow.add_edge("chatbot", END)
    
    def chatbot_with_tools_build_graph(self):
        """Builds a graph for a chatbot with external tool integrations (to be implemented)."""
        pass  # Placeholder for future implementation

    def setup_graph(self, usecase: str) -> Optional[StateGraph]:

        usecase_mapping = {
            "Basic Chatbot": self.basic_chatbot_build_graph,
            "Chatbot with Tools": self.chatbot_with_tools_build_graph,
        }

        build_graph = usecase_mapping.get(usecase)

        if build_graph:
            build_graph()
            return self.workflow.compile()
        else:
            st.error(f"Invalid use case: {usecase}. Choose from {list(usecase_mapping.keys())}.")
