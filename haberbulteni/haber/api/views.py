import imp
from rest_framework import status 
from rest_framework.response import Response #redirect return
from rest_framework.decorators import api_view

from haber.models import Makale
from haber.api.serializers import MakaleSerializer

@api_view(['GET', 'POST'])
def makale_list_create_api_view(request):
    
    if request.method == 'GET':
        makaleler = Makale.objects.filter(aktif=True) # burada nesnelerden oluşan bir queryset var
        serializer = MakaleSerializer(makaleler, many=True) # query sett 
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = MakaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
