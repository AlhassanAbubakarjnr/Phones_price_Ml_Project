import sys
import os
import logging
from typing import Optional, Any


def error_message_detail(error: Exception, error_detail: Optional[object] = None) -> str:
    """Return a detailed error message.

    Parameters
    - error: the exception instance or message
    - error_detail: optional object providing exc_info(); when None, defaults to sys

    This function is defensive: it handles cases where exc_info() returns (None, None, None).
    """
    if error_detail is None:
        error_detail = sys

    # Try to call exc_info() on the provided object; fall back to sys.exc_info()
    exc_info_callable = getattr(error_detail, "exc_info", None)
    if callable(exc_info_callable):
        exc_info = exc_info_callable()
    else:
        exc_info = sys.exc_info()

    # Ensure exc_info is a tuple of length 3
    if not (isinstance(exc_info, tuple) and len(exc_info) == 3):
        exc_info = (None, None, None)
    _, _, exc_tb = exc_info

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "<unknown>"
        line_number = "<unknown>"

    error_message = (
        f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{error}]"
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: Optional[object] = None):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
    
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.error("An error occurred", exc_info=True)
        raise CustomException(e, sys)

    