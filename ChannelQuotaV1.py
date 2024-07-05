from pydantic import BaseModel


class ChannelQuotaV1(BaseModel):
    reddit_quota: int
