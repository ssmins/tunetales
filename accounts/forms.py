from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model 

class CustomUserCreationForm(UserCreationForm): 
    class Meta(UserCreationForm.Meta): 
        model = get_user_model() 
        # fields = '__all__'
        fields = (
            'username',
            'last_name',
            'first_name',
            'email',
        )

class CustomUserChangeForm(UserChangeForm): 
    class Meta(UserChangeForm.Meta): 
        model = get_user_model() 
        # fields = '__all__'
        fields = (
            'first_name',
            'last_name',
            'email',
        )