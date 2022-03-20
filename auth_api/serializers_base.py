from rest_framework import serializers
from .models import UserAccount

### ALLOWS YOU TO CREATE AND CHECK PASSWORDS
from django.contrib.auth.hashers import make_password, check_password

class UserAccountSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'username', 'password',)

    ### THIS HASHES A NEW USERS PASSWORD WHEN THEY CREATE AN ACCOUNT
    def create(self, validated_data):
        user = UserAccount.objects.create(
        username = validated_data['username'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return user

    ### THIS MAKES SURE THEIR UPDATED PASSWORDS ARE ALSO HASHED
    def update(self,instance, validated_data):
        user = UserAccount.objects.get(username=validated_data['username'])
        user.password = make_password(validated_data['password'])
        user.save()
        return user
