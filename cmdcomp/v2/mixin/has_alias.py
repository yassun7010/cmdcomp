from abc import ABCMeta
from functools import cached_property


class HasAlias(metaclass=ABCMeta):
    # @property
    # @abstractmethod
    # def alias(self) -> str | list[str] | None:
    #     ...

    @cached_property
    def aliases(self) -> list[str]:
        alias = self.alias  # type: ignore
        if alias is None:
            return []
        elif isinstance(alias, str):
            return [alias]
        else:
            return alias
