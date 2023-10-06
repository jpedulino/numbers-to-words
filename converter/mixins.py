import json
from typing import Any, Callable, List
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse


class ConverterMixin:
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # Centralizing validation of parameter here to handle errors for both HTTP methods
        try:
            if request.method == "GET":
                number_param = request.GET.get("number")
            if request.method == "POST":
                number_param = json.loads(request.body).get("number")
            abs(int(number_param))
        except TypeError:
            return HttpResponseBadRequest("Please provide a 'number' parameter")
        except ValueError:
            return HttpResponseBadRequest(
                "The 'number' parameter must have be a valid integer"
            )

        return super().dispatch(request, *args, **kwargs)

    def convert_number_to_words(
        self, number: int, converter_func: Callable
    ) -> JsonResponse:
        try:
            words = converter_func(number=number)
            return JsonResponse({"status": "ok", "num_in_english": words})
        except Exception as exc:
            return JsonResponse({"status": "error", "message": exc.message}, status=400)
