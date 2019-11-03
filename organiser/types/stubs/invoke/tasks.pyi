# Stubs for invoke.tasks (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Iterable, Dict, Union, Callable, Any

# pylint: disable = missing-class-docstring, too-few-public-methods, unused-argument
# pylint: disable = missing-module-docstring, missing-function-docstring, unused-import


class Task:
    ...


def task(  # type: ignore
        fun: Callable[[Any], Any], *args: Iterable[str],
        **kwargs: Dict[str, Union[str, int, float, bool]]
) -> Task:
    ...