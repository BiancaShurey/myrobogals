from .models import RobogalsUser

from rest_framework import serializers

class RobogalsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RobogalsUser
        #fields = ('url', 'username', 'given_name', 'primary_email', 'groups', 'is_active', 'is_superuser',)
        write_only_fields = ('password',)
