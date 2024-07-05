from pydantic import BaseModel
from .RecordData import RecordData
from .Platform import Platform
from .Language import Language


class ChannelV1(BaseModel, RecordData):
    channel_name: str
    channel_link: str
    channel_id: str
    platform: Platform
    language: Language

    class Config:
        # NOTE: All domain models need this so that db models can gracefully map to this
        from_attributes = True
