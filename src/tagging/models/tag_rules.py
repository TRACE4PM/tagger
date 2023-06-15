from .base import Base_Model
from .condition import Condition_Model

class Tag_Rules_Model(Base_Model):
    tag_name: str
    conditions: list[Condition_Model] = []