import json
from .models.tag_rules import Tag_Rules_Model

def validate_json_content(file_content):
    tags_config = json.loads(file_content)
    tags = list[Tag_Rules_Model]
    for tag_config in tags_config:
        tags.append(Tag_Rules_Model(**tag_config))
    return tags
