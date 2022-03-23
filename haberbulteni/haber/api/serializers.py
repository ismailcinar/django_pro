from rest_framework import serializers
from haber.models import Makale

class MakaleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField
    aciklama = serializers.CharField()
    metin = serializers.CharField()
    sehir = serializers.CharField()
    yayinlanma_tarihi = serializers.DateField()
    aktif = serializers.BooleanField()
    yaratilma_tarihi = serializers.DateTimeField(read_only=True)  # değişmez
    güncellenme_tarihi = serializers.DateTimeField(read_only=True)     # değişir


    def create(self, validated_data):
        print(validated_data)
        return Makale.objects.create(**validated_data) # ıt comes dictionary ıt opens dictionary anahtar değerleri eşleştir ve modeli oturttur ve kaydet
    def update(self, instance, validated_data):  #karşıya bir obje gönderiyoruz bunun için instance
        instance.yazar = validated_data.get('yazar', instance.yazar)
        instance.baslik = validated_data.get('baslik', instance.baslik)
        instance.aciklama = validated_data.get('aciklama', instance.aciklama)
        instance.metin = validated_data.get('metin', instance.metin)
        instance.sehir = validated_data.get('sehir', instance.sehir)
        instance.yayinlanma_tarihi = validated_data.get('yayinlanma_tarihi', instance.yayinlanma_tarihi)
        instance.aktif = validated_data.get('aktif', instance.aktif)
        instance.save()
        return instance
