from rest_framework.serializers import ModelSerializer
from.models import Cracker
class CrackerSerializers(ModelSerializer):
    class Meta:
        model=Cracker
        fields="__all__"