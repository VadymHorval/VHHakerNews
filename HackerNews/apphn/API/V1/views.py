from django.shortcuts import render,HttpResponseRedirect,Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from HackerNews.apphn.models import Post
from .serializers import NewsSerializer


@csrf_exempt
def ItemsView(request):
    d = {'dict': 1, 'dictionary': 2}
    return JsonResponse(d, safe=False)

    # if request.method == 'GET':
    #     items = Post.get_all()
    #     serializer = NewsSerializer(items, many=True)
    #     #serializer = Post.serializable_value()
    #     #return JsonResponse(serializer.data, safe=False)
    #     d = {'dict': 1, 'dictionary': 2}
    #     return JsonResponse(d, safe=False)
    #
    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = NewsSerializer(data=data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)