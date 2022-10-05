from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from apps.base.services.generate_user import generate_user


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "index.html",
        {
            "result": [generate_user() for _ in range(10)],
            "title": "Base",
            "len": len([generate_user() for _ in range(10)]),
        },
    )


def amount_of_generator(request: HttpRequest, generator_length: int) -> HttpResponse:
    return render(
        request,
        "index.html",
        {
            "result": [generate_user() for _ in range(generator_length)],
            "title": "Base",
            "len": len([generate_user() for _ in range(generator_length)]),
        },
    )
