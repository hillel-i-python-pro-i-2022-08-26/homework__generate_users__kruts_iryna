from django.shortcuts import render
from django.http import HttpRequest

from apps.base.services.generate_users import generate_users


def index(request):
    return render(request,
                  'index.html',
                  {
                      'result': [next(generate_users()) for _ in range(10)],
                      'title': 'Base',
                      'len': len([next(generate_users()) for _ in range(10)])
                  })

def amount_of_generator(request: HttpRequest, generator_length: int):
    return render(request,
                  'index.html',
                  {
                      'result': [next(generate_users()) for _ in range(generator_length)],
                      'title': 'Base',
                      'len': len([next(generate_users()) for _ in range(generator_length)])
                  })
