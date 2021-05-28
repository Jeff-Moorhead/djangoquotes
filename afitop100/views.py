import json

from django.shortcuts import render
from . import afi, console


def index(request):
    if not afi.check_json_exists():
        console.build_quotes_file()

    quotes_json = afi.fetch_quotes_json()
    return render(request, 'index.html', {"quotes_json": quotes_json})

