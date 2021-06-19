
from rest_framework import serializers
from .models import User



class RegestrationSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'passwords'}, write_only=True)
    class Meta:
        model = User
        fields = [
                'username',
                'email',
                'password',
                'password2',
                'full_name',
                'number',
                'code_agency',
            ]
        extra_kwargs = {
                'password' : {'write_only' : True} 
        }
    
    def save(self):
        account = User(
            email    = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'پسوورد ها باید یکسان باشد'})
        account.set_password(password)
        account.save()
        return account