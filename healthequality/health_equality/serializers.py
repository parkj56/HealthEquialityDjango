from rest_framework import serializers
from .models import BodyData 

class BDSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyData
        fields = ['age', 'height', 'weight', 'dose', 'start_date', 'med_date']