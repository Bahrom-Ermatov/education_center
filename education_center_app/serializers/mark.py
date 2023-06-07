from rest_framework import serializers
from education_center_app.models import Mark

class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields = "__all__"


