import time

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from bckend.common.UniResponse import UniResponse, UniResponseEncoder, Result


# /api_v2/query?q=xxxx
@require_http_methods(["GET"])
def get_results(request: WSGIRequest):
    results = [Result("1", 0.545, {"url": "http://www.a.b.c/path/t"}),
               Result("2", 0.643, {"url": "http://www.a.b.c/path/to"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"})]
    status_code = 200
    query_string = request.GET.get("q")
    print(query_string)
    start = time.time()
    # search results
    # results.append()
    q = time.time() - start
    t = len(results)
    res = UniResponse({'query_time': q, 'total_number': t, "hits": results})
    return JsonResponse(UniResponseEncoder().encode(res), safe=False)
