from converter.services.english_conversion.exceptions import ConversionLimitExceeded
import pytest
from converter.services.english_conversion.to_english import convert_number_to_english


class TestConversionToEnglish:
    @pytest.mark.parametrize(
        "number,expected_result",
        [
            (1, "one"),
            (1000, "one thousand"),
            (1337, "one thousand three hundred thirty seven"),
            (10010, "ten thousand ten"),
            (100000, "one hundred thousand"),
            (
                12345678,
                "twelve million three hundred forty five thousand six hundred seventy eight",
            ),
            (
                25432123,
                "twenty five million four hundred thirty two thousand one hundred twenty three",
            ),
            (
                999999999999999999999999,
                "nine hundred ninety nine sextillion nine hundred ninety nine quintillion nine hundred ninety nine quadrillion nine hundred ninety nine billion nine hundred ninety nine trillion nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine",
            ),
        ],
    )
    def test_valid_number_conversion(self, number, expected_result):
        words = convert_number_to_english(number=number)
        assert words == expected_result

    def test_exception_is_raised_when_number_exceeds_limit(self):
        with pytest.raises(ConversionLimitExceeded):
            convert_number_to_english(number=9999999999999999999999999)
