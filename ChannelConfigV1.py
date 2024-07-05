from pydantic import BaseModel
from typing import List


class ChannelConfigV1(BaseModel):
    description_base: str
    subreddit_compile_strategy_ids: List[str]
    show_watermark: bool
