from pydantic import BaseModel
from .RecordData import RecordData
from typing import List, Optional
from .ScriptStructureV1 import ScriptStructureV1
from .TextPositionV1 import TextPositionV1


class SubredditCompileStrategyV1(BaseModel, RecordData):
    subreddit_compile_strategy_id: str
    subreddit_name: str
    search_terms: List[str]
    title_fonts: List[str]
    render_title_font_all_caps: bool
    body_fonts: List[str]
    text_position: TextPositionV1
    render_body_font_all_caps: bool
    tts_voices: List[str]
    bg_footages: List[str]
    play_bg_footage_audio: bool
    play_bg_footage_at_random_start: bool
    play_bg_footage_sped_up: bool
    music: List[str]
    show_credit: bool
    label_color: Optional[str]
    watermark_color: Optional[str]
    different_tts_per_user: bool
    script_structure: ScriptStructureV1
    notes: str

    class Config:
        # NOTE: All domain models need this so that db models can gracefully map to this
        from_attributes = True
