from pydantic import BaseModel
from typing import Dict, Any

class DocResult(BaseModel):
    doc_type: str
    fields: Dict[str, Any]
    confidence: float
