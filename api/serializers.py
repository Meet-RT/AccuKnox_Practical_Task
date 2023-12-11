from rest_framework import serializers
from .models import User, FriendRequest
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    confirm_password = serializers.CharField(required=True,write_only= True)
    class Meta:
        model = User
        fields = ["id", "email", "name", "password","confirm_password","username"]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)



class FriendRequestSerializer(serializers.ModelSerializer):
    to_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = FriendRequest
        fields = ['id','to_user','is_accepted','is_rejected']

