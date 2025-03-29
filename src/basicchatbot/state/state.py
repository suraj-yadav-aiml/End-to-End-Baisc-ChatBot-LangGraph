from typing import Annotated, List, Any
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class BasicChatBotState(TypedDict):
    messages: Annotated[List[Any], add_messages]

