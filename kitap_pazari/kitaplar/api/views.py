from rest_framework.generics import GenericAPIView
from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from rest_framework import generics
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from kitaplar.models import Kitap, Yorum
from rest_framework.generics import get_object_or_404

class KitapListCreateAPIView(generics.ListCreateAPIView):  # list kullanmazsak geti getirmez
        queryset = Kitap.objects.all()
        serializer_class = KitapSerializer

class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Kitap.objects.all()
        serializer_class = KitapSerializer


class YorumCreateAPIView(generics.CreateAPIView):
        queryset = Yorum.objects.all()
        serializer_class = YorumSerializer

        def perform_create(self, serializer):
            kitap_pk = self.kwargs.get('kitap_pk')
            kitap = get_object_or_404(Kitap, pk=kitap_pk)
            serializer.save(kitap=kitap)

class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Yorum.objects.all()
        serializer_class = YorumSerializer






# class KitapListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    
#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)