import streamlit as st
from typing import Literal
from langgraph.graph.state import CompiledStateGraph
from langchain_core.messages import AIMessage


class DisplayResultStreamlit:
    """Displays chatbot interaction results in Streamlit UI."""

    def __init__(self, usecase: str, graph: CompiledStateGraph, user_message: str):

        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

        # Initialize message history if not in session state
        if "message_history" not in st.session_state:
            st.session_state.message_history = []
    
    def _display_message(self,role:Literal["user","assistant"], message:str) -> None:
        with st.chat_message(role):
            st.markdown(message)

    def _display_chat_history(self) -> None:
        for chat in st.session_state.message_history:
            self._display_message(chat["role"], chat["message"])
    
    def _handle_basic_chatbot(self) -> None:

        # Display existing chat history before processing new input
        self._display_chat_history()

        st.session_state.message_history.append({"role": "user", "message": self.user_message})
        self._display_message("user", self.user_message)
        
        try:
            for event in self.graph.stream(input={"messages": self.user_message}):
                for _, node_output in event.items():
                    ai_response = (
                        node_output["messages"].content
                        if isinstance(node_output["messages"], AIMessage)
                        else node_output["messages"]
                    )

                    st.session_state.message_history.append({"role": "assistant", "message": ai_response})
                    self._display_message("assistant", ai_response)
                

        except Exception as e:
            st.error(f"Error processing response: {str(e)}")

    def _handle_chatbot_with_tool(self) -> None:
        """Handle the tool-enhanced chatbot interaction flow."""
        pass  # Placeholder for future implementation

    def display_result_on_ui(self) -> None:
        usecase_handlers = {
            "Basic Chatbot": self._handle_basic_chatbot,
            "Chatbot with Tool": self._handle_chatbot_with_tool,
        }

        handler = usecase_handlers.get(self.usecase)
        if handler:
            handler()
        else:
            st.error(f"Unsupported usecase: {self.usecase}")
            st.info("Supported usecases: " + ", ".join(usecase_handlers.keys()))
