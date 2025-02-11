from django.contrib import admin
from .models import Course, Webinar, Video, Booking


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'start_date', 'end_date', 'is_active')
    search_fields = ('title', 'description')
    list_filter = ('is_active',)
    fields = ('title', 'description', 'price', 'start_date', 'end_date', 'is_active', 'image')


@admin.register(Webinar)
class WebinarAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'date', 'is_active')
    search_fields = ('title', 'description')
    list_filter = ('is_active',)
    fields = ('title', 'description', 'price', 'date', 'is_active', 'image', 'webinar_url',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active')
    search_fields = ('title', 'description')
    list_filter = ('is_active',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'webinar', 'video', 'booking_date', 'is_paid')
    list_filter = ('is_paid',)


admin.site.site_header = "Управление сервисом"
admin.site.site_title = "Админка hairdresser_service"
