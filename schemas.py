from pydantic import BaseModel
from typing import Optional

class AgentResponse(BaseModel):
    step: str
    content: Optional[str] = None
    tool: Optional[str] = None
    input: Optional[str] = None
