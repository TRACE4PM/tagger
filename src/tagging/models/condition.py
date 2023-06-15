from .base import Base_Model


class Condition_Model(Base_Model):
    number: int
    first_keyword: str
    second_keyword: str | None = None
    alternate_tag: str | None = None
