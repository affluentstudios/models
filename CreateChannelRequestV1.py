from typing import Optional
from pydantic import BaseModel
from .Language import Language
from .Platform import Platform


class CreateChannelRequestV1(BaseModel):
    channel_name: str
    channel_link: str
    platform: Optional[Platform] = None
    language: Optional[Language] = None
    client_id: str
    client_secret: str
