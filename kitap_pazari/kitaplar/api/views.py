from django.forms import ValidationError
from rest_framework.generics import GenericAPIView
from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from rest_framework import generics
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from kitaplar.models import Kitap, Yorum
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from kitaplar.api.permissions import IsAdminUserOrReadOnly, IsYorumSahibiOrReadOnly
from rest_framework.exceptions import ValidationError  ### HTTP 400 Döndürebilmemiz için bunu import etmeyi unutmayalım

class KitapListCreateAPIView(generics.ListCreateAPIView):  # list kullanmazsak geti getirmez
        queryset = Kitap.objects.all()
        serializer_class = KitapSerializer
        permission_classes = [IsAdminUserOrReadOnly]
class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Kitap.objects.all()
        serializer_class = KitapSerializer
        permission_classes = [IsAdminUserOrReadOnly]

class YorumCreateAPIView(generics.CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    def perform_create(self, serializer):
        #  path('kitaplar/<int:kitap_pk>/yorum_yap/', api_views.YorumCreateAPIView.as_view(), name='kitap-yorumla'),
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        yorum_sahibi = self.request.user
        #### Kullanıcıya ait, aynı kitap için yorum var mı???
        yorumlar = Yorum.objects.filter(kitap=kitap, yorum_sahibi=yorum_sahibi) 
        if yorumlar.exists():
            raise ValidationError('Bu kitaba daha önce yorum yaptınız.')

        serializer.save(kitap=kitap, yorum_sahibi = yorum_sahibi)

class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer  
    permission_classes = [IsYorumSahibiOrReadOnly]
       






# class KitapListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    
#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)