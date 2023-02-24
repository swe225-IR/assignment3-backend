from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

# Create your views here.


from rest_framework import viewsets

from bckend.common.UniResponse import UniResponse, UniResponseEncoder, Result
import json


# /api_v2/query?q=xxxx
@require_http_methods(["GET"])
def get_results(request: WSGIRequest):
    results = [Result("a"), Result("b"), Result("c")]
    status_code = 200
    query_string = request.GET.get("q")

    # search results
    # results.append()

    print(request)
    res = UniResponse(results)
    return JsonResponse(UniResponseEncoder().encode(res), safe=False)
