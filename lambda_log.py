import inspect
import logging

__all__ = ["Logger"]


def __line_numb():
    """Returns the current line number in our program"""
    return inspect.currentframe().f_back.f_back.f_lineno


class Logger:
    def __init__(self, name: str) -> None:
        self._setup_logger()
        self.__name = name

    def _setup_logger(self) -> logging.Logger:
        if len(logging.getLogger().handlers) > 0:
            # The Lambda environment pre-configures a handler logging to stderr. If a handler is already configured,
            # `.basicConfig` does not execute. Thus we set the level directly.
            logging.getLogger().setLevel(logging.INFO)
        else:
            logging.basicConfig(level=logging.INFO)

    def info(self, message: str) -> None:
        logging.info(f"[{self.__name}:{__line_numb()}] -{message}")

    def error(self, message: str) -> None:
        logging.error(f"[{self.__name}:{__line_numb()}] -{message}")

    def warning(self, message: str) -> None:
        logging.warning(f"[{self.__name}:{__line_numb()}] -{message}")

    def debug(self, message: str) -> None:
        logging.debug(f"[{self.__name}:{__line_numb()}] -{message}")

    def critical(self, message: str) -> None:
        logging.critical(f"[{self.__name}:{__line_numb()}] -{message}")

    def exception(self, message: str) -> None:
        logging.exception(f"[{self.__name}:{__line_numb()}] -{message}")

    def log(self, level: int, message: str) -> None:
        logging.log(level, f"[{self.__name}:{__line_numb()}] -{message}")
