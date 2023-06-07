from rest_framework import serializers
from education_center_app.models import Cource

class CourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cource
        fields = "__all__"


