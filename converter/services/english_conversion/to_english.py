from typing import List

from converter.services.english_conversion.constants import (
    EN_CONVERSION_LIMIT,
    EN_LARGER_UNITS,
    EN_TEENS,
    EN_TENS,
    EN_UNITS,
    EN_ZERO,
)
from converter.services.english_conversion.exceptions import ConversionLimitExceeded


def _assign_word(number: int) -> str:
    if number == 0:
        return ""
    elif number < 10:
        return EN_UNITS[number]
    elif number < 20 and number != 10:
        return EN_TEENS[number - 10]
    elif number < 100:
        return (f"{EN_TENS[number // 10]} {EN_UNITS[number % 10]}").strip()
    else:
        return (
            f"{EN_UNITS[number // 100]} hundred " + _assign_word(number=number % 100)
        ).strip()


def _split_digits(number: int) -> List[int]:
    digits: List[int] = []
    while number > 0:
        digits.append(number % 1000)
        number //= 1000
    digits.reverse()
    return digits


def convert_number_to_english(number: int):
    if number > EN_CONVERSION_LIMIT:
        raise ConversionLimitExceeded
    if number == 0:
        return EN_ZERO

    digits = _split_digits(number)
    words = []
    for idx, n in enumerate(digits):
        word_to_assign = _assign_word(n)
        if idx + 1 < len(digits) and n != 0:
            words.append(
                word_to_assign + " " + EN_LARGER_UNITS[len(digits) - (idx + 1)]
            )
        else:
            words.append(word_to_assign)
    words = filter(lambda w: w != "", words)
    return " ".join(list(words))
