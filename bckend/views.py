import time

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from bckend.model.UniResponse import UniResponse, UniResponseEncoder
from bckend.server.utils.indexer import Indexer


# /api_v2/query?q=xxxx
@require_http_methods(["GET"])
def get_results(request: WSGIRequest):
    global res
    try:
        query_string = request.GET.get("q")
        offset = int(request.GET.get("offset"))
        limit = int(request.GET.get("limit"))
        start = time.time()
        indexer = Indexer(query=query_string)
        results = indexer.rank(tf_idf_weight=0.95, page_rank_weight=0.05)
        q = time.time() - start
        t = len(results)
        res = UniResponse({'query_time': q, 'total_number': t, "hits": results[offset:offset + limit]})
    except Exception as e:
        print(e)
        res = UniResponse({'query_time': 0, 'total_number': 0, "hits": []}, msg='exception', code=500)
    finally:
        return JsonResponse(UniResponseEncoder().encode(res), safe=False)
