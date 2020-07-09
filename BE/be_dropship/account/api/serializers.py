from rest_framework import serializers

from account.models import Account

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
				'password': {'write_only': True},
		}
    
    def save(self):
        email_superuser = ['llduyll10@gmail.com', 'llduyll9@gmail.com']

        account = Account(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        email = self.validated_data['email']
        
        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        if email in email_superuser:
            account.is_superuser = True
			
        account.set_password(password)
        account.save()
        return account

class AccountPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pk', 'email', 'username', 'image']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)