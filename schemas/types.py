from typing import Annotated

from pydantic import AfterValidator


def not_empty(v: str):
    if not v.strip:
        raise ValueError("Field cannot be empty or whitespace")
    return v

NonEmpatyStr = Annotated[str, AfterValidator(not_empty)]