from django.urls import path

from converter.views import NumberToEnglishView

app_name = "converter"

urlpatterns = [
    path("", NumberToEnglishView.as_view(), name="number-to-english-view"),
]
