from rest_framework import serializers

from core.models import TokenModel


class TokenModelSerializer(serializers.ModelSerializer):
    """Serializer for Token Model"""

    class Meta:
        model = TokenModel
        fields = "__all__"
        read_only_fields = ("id",)

