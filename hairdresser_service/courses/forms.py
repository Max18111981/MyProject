from django import forms
from .models import Course, Webinar, Video


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


