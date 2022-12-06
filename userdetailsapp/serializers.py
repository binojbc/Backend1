from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields =  '__all__'
        fields = ('UserId',
                  'UserName', 
                  'FullName',
                  'IsSuperUser',
                  'Department',
                  'Designation',
                  'Password'
                 )

                
      