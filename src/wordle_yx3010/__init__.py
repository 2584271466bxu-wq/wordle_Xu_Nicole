try:
    from importlib.metadata import version
    __version__ = version("wordle_yx3010")
except Exception:
    __version__ = "0.1.0"

from .wordle_yx3010 import (
    validate_guess,
    check_guess,
    is_valid_word,
    calculate_game_score,
)

__all__ = [
    "validate_guess",
    "check_guess",
    "is_valid_word",
    "calculate_game_score",
]
