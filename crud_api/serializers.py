from rest_framework import serializers
from crud.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','tipo_doc', 'doc', 'name', 'surnames', 'hobbie')
        
        
    
















