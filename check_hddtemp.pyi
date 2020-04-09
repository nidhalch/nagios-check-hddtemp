# -*- coding: utf-8 -*-

# nagios-check-hddtemp
# check_hddtemp.pyi

from typing import List, Dict, Union, Tuple  # pylint: disable=W0611

from argparse import Namespace

__all__: List[str] = ...


VERSION: Tuple[int, int, int] = ...
__version__: str = ...


class CheckHDDTemp(object):

    HDDTEMP_SLEEPING: str = ...
    HDDTEMP_UNKNOWN: str = ...
    STATUS_CRITICAL: str = ...
    STATUS_WARNING: str = ...
    STATUS_UNKNOWN: str = ...
    STATUS_OK: str = ...
    STATUS_SLEEPING: str = ...
    PRIORITY_CRITICAL: int = ...
    PRIORITY_WARNING: int = ...
    PRIORITY_UNKNOWN: int = ...
    PRIORITY_OK: int = ...
    PRIORITY_SLEEPING: int = ...
    PRIORITY_TO_STATUS: Dict[int, str] = ...
    OUTPUT_TEMPLATES: Dict[str, Dict[str, Union[str, int]]] = ...
    DEFAULT_EXIT_CODE: int = ...
    EXIT_CODES: Dict[str, int] = ...
    PERFORMANCE_DATA_TEMPLATE: str = ...
    options: Union[None, Namespace] = ...
    def __init__(self) -> None: ...
    @staticmethod
    def _get_options() -> Namespace: ...
    def _get_data(self) -> str: ...
    def _parse_data(self, data: str) -> Dict[str, Dict[str, str]]: ...
    def _check_data(
        self, data: Dict[str, Dict[str, str]]
    ) -> Dict[str, Dict[str, Union[str, Dict[str, Union[None, int, str]]]]]: ...
    def _get_output(
        self, data: Dict[str, Dict[str, Union[str, int, Dict[str, Union[None, int, str]]]]]
    ) -> Tuple[str, int]: ...
    def check(self) -> Tuple[str, int]: ...


def main() -> None: ...
