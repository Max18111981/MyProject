from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/confirm_payment/<int:booking_id>/', views.confirm_payment, name='confirm_payment'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', views.user_profile, name='user_profile'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('webinar/<int:webinar_id>/', views.webinar_detail, name='webinar_detail'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('courses/', views.course_list, name='course_list'),
    path('videos/', views.video_list, name='video_list'),
    path('webinars/', views.webinar_list, name='webinar_list'),
    path('book/course/<int:course_id>/', views.book_course, name='book_course'),
    path('book/webinar/<int:webinar_id>/', views.book_webinar, name='book_webinar'),
    path('buy/video/<int:video_id>/', views.buy_video, name='buy_video'),
    path('watch/video/<int:video_id>/', views.watch_video, name='watch_video'),
    path('watch/course/<int:course_id>/', views.watch_course, name='watch_course'),
    path('watch/webinar/<int:webinar_id>/', views.watch_webinar, name='watch_webinar'),
]