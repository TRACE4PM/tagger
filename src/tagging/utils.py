import json
from fastapi.encoders import jsonable_encoder
from .models.tag_rules import Tag_Rules_Model

async def validate_json_content(file_content):
    tags_config = json.loads(file_content)
    tags = []
    for tag_config in tags_config:
        tags.append(Tag_Rules_Model(**tag_config))
    return jsonable_encoder(tags)
