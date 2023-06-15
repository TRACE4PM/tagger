from .base import Base_Model
from .condition import Condition_Model


class Tag_Rules_Base_Model(Base_Model):
    tag_name: str


class Tag_Rules_Model(Tag_Rules_Base_Model):
    conditions: list[Condition_Model]

    def to_json(self):
        conditions = []
        for condition in self.conditions:
            conditions.append(condition.to_json())
        return {
            "tag_name": self.tag_name,
            "conditions": conditions
        }


class Tag_Rules_Get_Model(Tag_Rules_Base_Model):
    class Config:
        schema_extra = {
            "example": {
            "tag_name": "self.tag_name",
            }
        }