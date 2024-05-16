from functools import reduce
import hashlib
import json
from typing import Any, Dict, TypeVar, Type

import dataclasses as dataclasses


_T = TypeVar("_T")


def get_path(obj, path, default=None):
    result = reduce(lambda d, key: d.get(key) if d else None, __build_keys(path), obj)
    return result if result else default


def set_nested(dic, path, value):
    keys = __build_keys(path)
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


def __build_keys(path):
    if isinstance(path, list):
        return path
    else:
        return path.split(".")


def dataclass_from_dict(cls: Type[_T], d) -> _T:
    if dataclasses.is_dataclass(cls):
        fieldtypes = {f.name: f.type for f in dataclasses.fields(cls)}
        return cls(
            **{
                f: dataclass_from_dict(fieldtypes[f], d[f])
                for f in d
                if f in fieldtypes
            }
        )
    elif type(d) is list:
        return [dataclass_from_dict(cls.__args__[0], x) for x in d]
    else:
        return d
