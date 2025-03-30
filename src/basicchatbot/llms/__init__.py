import streamlit as st
from typing import Dict, Optional, Type, Union
from langchain_core.language_models.chat_models import BaseChatModel
from src.basicchatbot.llms.base_llm import BaseLLMProvider
from src.basicchatbot.llms.groq_llm import GroqLLM
from src.basicchatbot.llms.openai_llm import OpenAILLM


def get_llm(llm_name: str, user_input: Dict[str, str]) -> Optional[BaseChatModel]:
    """
    Function to get the appropriate LLM model instance.
    
    Args:
        llm_name: Name of the LLM provider to use
        user_input: Dictionary containing user configuration settings
        
    Returns:
        Configured LLM model instance or None if initialization fails
    """

    llm_providers: Dict[str, Type[BaseLLMProvider]] = {
        "Groq": GroqLLM,
        "OpenAI": OpenAILLM
    }

    # Get the appropriate LLM class
    llm_class = llm_providers.get(llm_name)
    
    if llm_class:
        try:
            # Initialize the LLM provider and get the model
            llm_provider = llm_class(user_input)
            llm_model = llm_provider.get_llm_model()
            
            if llm_model:
                return llm_model
            else:
                return None
                
        except Exception as e:
            error_msg = f"Error initializing {llm_name} LLM: {str(e)}"
            st.error(error_msg)
            return None
    else:
        # Handle unsupported LLM provider
        supported_providers = ', '.join(llm_providers.keys())
        error_msg = f"Unsupported LLM provider: {llm_name}"
        
        st.error(error_msg)
        st.info(f"Supported providers: {supported_providers}")
        return None