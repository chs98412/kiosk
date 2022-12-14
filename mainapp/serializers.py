from rest_framework import serializers
from .models import cart,order

class cartSerial(serializers.ModelSerializer):
    class Meta:
        model=cart
        fields=['hp','category','option','ice','cardorSamsung']


class orderSerial(serializers.ModelSerializer):
    class Meta:
        model=order
        fields=['hp','category','name','result','reason']

