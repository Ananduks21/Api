from rest_framework import serializers
from . import models


class FuncSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'image', 'created_at', 'updated_at')
        model = models.Func
