from typing import Optional
from pydantic import BaseModel
from .RecordData import RecordData
from .ContentSource import ContentSource
from .ScriptStatus import ScriptStatus


class ScriptV1(BaseModel, RecordData):
    script_data: dict
    content_source: ContentSource
    channel_id: str
    script_id: str
    script_status: ScriptStatus
    s3_link: Optional[str] = None

    class Config:
        # NOTE: All domain models need this so that db models can gracefully map to this
        from_attributes = True
