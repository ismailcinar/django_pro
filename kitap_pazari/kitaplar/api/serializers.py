from rest_framework import serializers
from kitaplar.models import Kitap, Yorum

class YorumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yorum
        fields = '__all__'


class KitapSerializer(serializers.ModelSerializer):
    yorumlar = YorumSerializer(many=True, read_only=True)
    class Meta:
        model = Kitap
        fields = '__all__'


