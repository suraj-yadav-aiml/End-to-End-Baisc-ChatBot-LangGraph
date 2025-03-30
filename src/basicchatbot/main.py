import streamlit as st

from src.basicchatbot.ui.streamlitui.loadui import StreamlitUILoader
from src.basicchatbot.ui.streamlitui.display_result import DisplayResultStreamlit
from src.basicchatbot.llms import get_llm
from src.basicchatbot.graph.graph_builder import GraphBuilder



def load_basic_chatbot():
    ui = StreamlitUILoader()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    user_message = st.chat_input(placeholder="Enter your message")

    if user_message:
        try:

            llm = get_llm(llm_name=user_input['selected_llm'], user_input=user_input)
            if not llm:
                st.error("Error: LLM model could not be initialized.")
                return
            
            usecase = user_input['selected_usecase']
            if not usecase:
                    st.error("Error: No use case selected.")
                    return
            
            
            try:
                graph_builder = GraphBuilder(model=llm)
                graph = graph_builder.setup_graph(usecase)
                if graph is None:
                    st.error("Error: Graph setup failed.")
                    return
                
                DisplayResultStreamlit(
                    usecase=usecase,
                    graph=graph,
                    user_message=user_message
                ).display_result_on_ui()

            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}")
                return
            
        except Exception as e:
              raise ValueError(f"Error Occurred with Exception : {e}")

    