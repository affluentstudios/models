from pydantic import BaseModel
from .ChannelConfigV1 import ChannelConfigV1
from .ChannelQuotaV1 import ChannelQuotaV1


class UpdateChannelConfigsRequestV1(BaseModel):
    channel_config: ChannelConfigV1
    channel_quota: ChannelQuotaV1
