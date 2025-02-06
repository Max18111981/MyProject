from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User



class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='courses/images/', null=True, blank=True)
    trailer_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Webinar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='webinars/images/', null=True, blank=True)
    trailer_url = models.URLField(blank=True, null=True)
    webinar_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    video_file = models.FileField(upload_to='videos/')
    is_active = models.BooleanField(default=True)
    trailer_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE, null=True, blank=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    purchase_date = models.DateTimeField(null=True, blank=True)
    payment_confirmed = models.BooleanField(default=False)

    @property
    def is_active(self):
        return self.webinar.is_active

    @property
    def days_remaining(self):
        return 20 - (timezone.now() - self.purchase_date).days

    def is_access_active(self):
        """Проверяет, активен ли доступ к контенту (20 дней с момента покупки)."""
        if self.purchase_date:
            return (timezone.now() - self.purchase_date).days <= 20
        return False

    def __str__(self):
        return f"{self.user.username} - {self.course or self.webinar or self.video}"