import json
from typing import Type, TypeVar, Dict

from dataclasses import dataclass, asdict

from .dictionary_utils import dataclass_from_dict

_T = TypeVar("_T")


@dataclass
class BaseDictable:
    @classmethod
    def from_dict(cls: Type[_T], data: Dict) -> _T:
        return dataclass_from_dict(cls, data)

    def as_dict(self, to_camel_case: bool = False) -> Dict:
        if to_camel_case:
            return BaseDictable._to_dict_with_camel_case(self)
        else:
            return asdict(
                self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None}
            )

    @staticmethod
    def _to_dict_with_camel_case(obj) -> Dict:
        return json.loads(
            json.dumps(BaseDictable._serialise(obj), default=BaseDictable._serialise)
        )

    @staticmethod
    def _to_camel_case(snake_case) -> Dict:
        words = snake_case.split("_")
        return words[0] + "".join(x.title() for x in words[1:])

    @staticmethod
    def _serialise(obj) -> Dict:
        return {
            BaseDictable._to_camel_case(k): v
            for k, v in obj.__dict__.items()
            if v is not None
        }

    def __eq__(self, other):
        return self.as_dict() == other.as_dict()

    def __hash__(self):
        return hash(self.as_dict())
