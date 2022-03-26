from argparse import ArgumentDefaultsHelpFormatter
from dataclasses import fields
from sys import addaudithook
from rest_framework import serializers
from haber.models import Makale
from datetime import datetime
from datetime import date
from django.utils.timesince import timesince

from haber.models import Gazeteci




class MakaleSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()
    #yazar = serializers.StringRelatedField()
    #yazar = GazeteciSerializer()
    class Meta:
        model = Makale
        fields = '__all__'
        #fields = ['yazar', 'baslik', 'metin']
         #exclude = ['yazar', 'baslik', 'metin']
        read_only_fields = ['id', 'yaratilma_tarihi', 'güncellenme_tarihi']
    
    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.yayinlanma_tarihi
        if object.aktif == True:
            time_delta = timesince(pub_date,now)
            return time_delta
        else:
            return 'Aktif değil'

    def validate_yayinlanma_tarihi(self, tarihDegeri):
        today = date.today()
        if tarihDegeri>today :
            raise serializers.ValidationError('Yayınlanma tarihi ileri tarih olamaz')
        return tarihDegeri


class GazeteciSerializer(serializers.ModelSerializer):
    # makaleler = MakaleSerializer(many=True, read_only=True)
    makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='makale-detay',
    )
    class Meta:
        model = Gazeteci
        fields = '__all__'

#Standart
class MakaleDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
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

    def validate(self, data): #object level
        if data['baslik'] == data['aciklama']:
            raise serializers.ValidationError('Baslik ve aciklama alanları ayni olamaz')
        return data

    def validate_baslik(self, value):
        if len(value)<20:
            raise serializers.ValidationError(f'Minimum 20 karakter olmalı baslik. Siz {len(value)} karakter girdiniz')
        return value

