import json
from converter.services.english_conversion.constants import EN_CONVERSION_LIMIT
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestNumberToEnglishView:
    url = reverse("converter:number-to-english-view")

    def test_bad_request_when_missing_number_parameter(self, django_test_client):
        response = django_test_client.get(self.url)
        assert response.status_code == 400
        assert response.content == b"Please provide a 'number' parameter"

    @pytest.mark.parametrize("number_param", ["abc", "6e24", ""])
    def test_bad_request_when_number_parameter_is_not_a_valid_integer(
        self, number_param, django_test_client
    ):
        response = django_test_client.get(self.url + f"?number={number_param}")
        assert response.status_code == 400
        assert (
            response.content == b"The 'number' parameter must have be a valid integer"
        )

    def test_response_for_valid_conversion(self, django_test_client):
        response = django_test_client.get(self.url + "?number=1337")
        assert response.status_code == 200

        response_content = json.loads(response.content)
        assert response_content["status"] == "ok"
        assert (
            response_content["num_in_english"]
            == "one thousand three hundred thirty seven"
        )

    def test_response_for_conversion_that_exceeded_limit(self, django_test_client):
        response = django_test_client.get(
            self.url + f"?number={EN_CONVERSION_LIMIT + 1}"
        )
        assert response.status_code == 400

        response_content = json.loads(response.content)
        assert response_content["status"] == "error"
        assert (
            response_content["message"]
            == "Conversion limit was exceeded. Please enter a value that has 24 digits or less."
        )
