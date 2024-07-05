from pydantic import BaseModel
from typing import Optional


class UpdateScriptRequestV1(BaseModel):
    s3_link: Optional[str] = None
    script_data: Optional[dict] = None
