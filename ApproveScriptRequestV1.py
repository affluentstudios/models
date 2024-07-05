from pydantic import BaseModel


class ApproveScriptRequestV1(BaseModel):
    title: str
    description: str
