from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Course, Webinar, Video, Profile


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'start_date', 'end_date', 'is_active']


class WebinarForm(forms.ModelForm):
    class Meta:
        model = Webinar
        fields = ['title', 'description', 'price', 'date', 'is_active']


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'price', 'video_file', 'is_active']


class CustomUserCreationForm(UserCreationForm):
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Введите вашу фамилию'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Введите ваш email'})
    )

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise ValidationError("Фамилия должна содержать только буквы.")
        return last_name

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.create(user=user, last_name=self.cleaned_data['last_name'])
        return user

    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}),
        }