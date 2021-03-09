from __future__ import annotations
import argparse
from typing import Optional

TASK_NAME_PARAMETER = "task_name"


class ArgParserBuilder:

    def __init__(self):
        self.__parser: Optional[argparse.ArgumentParser] = None

    def initialize_build(self, parser_name: str) -> ArgParserBuilder:
        self.__ensure_parser_not_initialized()
        self.__parser = argparse.ArgumentParser(parser_name)
        return self

    def finish_build(self) -> argparse.ArgumentParser:
        self.__ensure_parser_initialized()
        parser = self.__parser
        self.__parser = None
        return parser

    def add_task_name_parameter(self) -> ArgParserBuilder:
        self.__ensure_parser_initialized()
        self.__parser.add_argument(
            "--task_name",
            type=str,
            required=True
        )
        return self

    def add_input_dataset_dir_parameter(self) -> ArgParserBuilder:
        self.__ensure_parser_initialized()
        self.__parser.add_argument(
            "--input_dataset_dir",
            type=str,
            required=True
        )
        return self

    def __ensure_parser_initialized(self) -> None:
        if self.__parser is None:
            raise RuntimeError("Did not initialze parser building.")

    def __ensure_parser_not_initialized(self) -> None:
        if self.__parser is not None:
            raise RuntimeError("Trying to re-initialize parser building.")
