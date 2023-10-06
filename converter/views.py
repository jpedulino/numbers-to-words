import json
from django.http import HttpRequest, JsonResponse
from django.views import View

from converter.mixins import ConverterMixin
from converter.services.english_conversion.to_english import convert_number_to_english


class NumberToEnglishView(ConverterMixin, View):
    http_method_names = ["get", "post"]

    def get(self, request: HttpRequest) -> JsonResponse:
        number_param = request.GET.get("number")
        return self.convert_number_to_words(
            number=abs(int(number_param)), converter_func=convert_number_to_english
        )

    def post(self, request: HttpRequest) -> JsonResponse:
        number_param = json.loads(request.body).get("number")
        return self.convert_number_to_words(
            number=abs(int(number_param)), converter_func=convert_number_to_english
        )
