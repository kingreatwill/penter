from enum import Enum
from typing import Union

class RepoQueryParamsEnum(Enum):
    CREATED = 1
    PUSHED = 2
    FORK = 3
    FORKS = 4
    IN = 5
    LANGUAGE = 6
    LICENSE = 7
    REPO = 8
    USER = 9
    SIZE = 10
    STARS = 11
    TOPIC = 12
    ARCHIVED = 13

class RepoQueryParamsOperator(Enum):
    GREATER_THAN = '>'
    GREATER_THAN_EQUAL_TO = '>='
    LESS_THAN = '<'
    LESS_THAN_EQUAL_TO = '<='
    EQUALS = '='
    NO_OP = ''

class RepoSortParamsEnum(Enum):
    STARS = 1
    FORKS = 2
    UPDATED = 3

class RepoQueryParams:
    def __init__(self):
        self._params = dict()
        self._sort_param = None

    def add_param(self, key: RepoQueryParamsEnum, operator: RepoQueryParamsOperator, value: Union[str, int, bool]) -> 'RepoQueryParams':
        query_str = ""
        if operator is not None and operator != RepoQueryParamsOperator.EQUALS:
            query_str += operator.value
        query_str += str(value).lower()
        self._params[key.name.lower()] = query_str
        return self

    def add_range_param(self, key: RepoQueryParamsEnum, value_lower: int, value_higher: int) -> 'RepoQueryParams':
        query_str = '%d..%d' % (value_lower, value_higher)
        self._params[key.name.lower()] = query_str
        return self

    def resolve(self):
        return self._params