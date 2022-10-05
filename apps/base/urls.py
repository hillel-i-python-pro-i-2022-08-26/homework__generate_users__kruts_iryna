from django.urls import path

from apps.base.views import index, amount_of_generator

app_name = "base"

urlpatterns = [
    path("", index, name="index"),
    path("<int:generator_length>/", amount_of_generator, name="amount"),
]
