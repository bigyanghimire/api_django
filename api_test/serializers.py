from rest_framework import serializers
from .models import MachineL
class MachineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=MachineL
        fields=('id','url','name_of_project','description_ml')