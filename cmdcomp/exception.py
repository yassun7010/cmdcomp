from typing import Never


class NeverReach(Exception):
    def __init__(self, value: Never) -> None:
        self._value = value

    def __str__(self) -> str:
        return f"never reach: {self._value}"
