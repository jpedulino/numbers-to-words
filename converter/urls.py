from django.urls import path

from converter.views import NumberToEnglishView

app_name = "converter"

urlpatterns = [
    path("num_to_english", NumberToEnglishView.as_view(), name="number-to-english-view"),
]
