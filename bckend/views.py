import time

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from bckend.model.UniResponse import UniResponse, UniResponseEncoder, Result


# /api_v2/query?q=xxxx
@require_http_methods(["GET"])
def get_results(request: WSGIRequest):
    results = [Result("1", 0.545, {"url": "http://www.a.b.c/path/t"}),
               Result("2", 0.643, {"url": "http://www.a.b.c/path/to"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),
               Result("3", 0.342, {"url": "http://www.a.b.c/path/toc"}),

               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),
               Result("4", 0.2312, {"url": "http://www.a.b.c/4/4/4"}),


               ]
    status_code = 200
    query_string = request.GET.get("q")
    # can set up a cache to store the previous searches (LRU)
    offset = int(request.GET.get("offset"))
    limit = int(request.GET.get("limit"))
    # tokenizer -> stemming ->
    start = time.time()
    time.sleep(0.2)
    # search results
    # results.append()
    q = time.time() - start
    t = len(results)
    res = UniResponse({'query_time': q, 'total_number': t, "hits": results[offset:offset+limit]})
    return JsonResponse(UniResponseEncoder().encode(res), safe=False)
