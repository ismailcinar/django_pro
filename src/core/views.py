from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
          'name': 'john',
          'age' : 23
       }
        return JsonResponse(data)



# def test_view(request):
#     data = {
#         'name': 'john',
#         'age' : 23
#     }
#     return JsonResponse(data)