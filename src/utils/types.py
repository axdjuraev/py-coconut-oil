from dataclasses import dataclass


@dataclass
class ErrorType:
    msg: str


@dataclass
class Response:
    err: ErrorType
