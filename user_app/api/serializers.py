from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self, **kwargs):
        password = self.validated_data.get('password')
        password2 = self.validated_data.get('password2')
        email = self.validated_data.get('email')
        username = self.validated_data.get('username')

        if password != password2:
            raise serializers.ValidationError({
                'error': 'Both the password should be same!'
            })

        user = User.objects.filter(email=email)

        if user.exists():
            raise serializers.ValidationError({
                "error": "The email is already exist!"
            })

        account = User(email=email, username=username)
        account.set_password(password)
        account.save()

        return account

