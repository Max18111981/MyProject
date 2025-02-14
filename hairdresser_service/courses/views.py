from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from pyexpat.errors import messages
from django.contrib import messages
from .models import Course, Webinar, Video, Booking
from .forms import CourseForm, WebinarForm, VideoForm, CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.utils import timezone
from .models import Video, Course, Webinar


def home(request):
    courses = Course.objects.filter(is_active=True)
    webinars = Webinar.objects.filter(is_active=True)
    videos = Video.objects.filter(is_active=True)
    return render(request, 'courses/home.html', {
        'courses': courses,
        'webinars': webinars,
        'videos': videos,
    })


# Страница с деталями курса
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})


# Страница с деталями вебинара
def webinar_detail(request, webinar_id):
    webinar = get_object_or_404(Webinar, id=webinar_id)
    return render(request, 'courses/webinar_detail.html', {'webinar': webinar})


# Страница с деталями видео
def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'courses/video_detail.html', {'video': video})


def course_list(request):
    courses = Course.objects.filter(is_active=True)
    return render(request, 'courses/course_list.html', {'courses': courses})


def video_list(request):
    videos = Video.objects.filter(is_active=True)
    return render(request, 'courses/video_list.html', {'videos': videos})


def webinar_list(request):
    webinars = Webinar.objects.filter(is_active=True)
    return render(request, 'courses/webinar_list.html', {'webinars': webinars})


# Запись на курс (только для авторизованных пользователей)
@login_required
def book_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        # Создаём новую запись о покупке
        Booking.objects.create(
            user=request.user,
            course=course,
            is_paid=False,  # По умолчанию оплата не подтверждена
            purchase_date=timezone.now()  # Дата покупки
        )
        return redirect('user_profile')
    return render(request, 'courses/book_course.html', {'course': course})


# Запись на вебинар (только для авторизованных пользователей)
@login_required
def book_webinar(request, webinar_id):
    webinar = get_object_or_404(Webinar, id=webinar_id)
    if request.method == 'POST':
        # Создаём новую запись о покупке
        Booking.objects.create(
            user=request.user,
            webinar=webinar,
            is_paid=False,  # По умолчанию оплата не подтверждена
            purchase_date=timezone.now()  # Дата покупки
        )
        return redirect('user_profile')
    return render(request, 'courses/book_webinar.html', {'webinar': webinar})


# Покупка видео (только для авторизованных пользователей)
@login_required
def buy_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        # Создаём новую запись о покупке
        Booking.objects.create(
            user=request.user,
            video=video,
            is_paid=False,  # По умолчанию оплата не подтверждена
            purchase_date=timezone.now()  # Дата покупки
        )
        return redirect('user_profile')
    return render(request, 'courses/buy_video.html', {'video': video})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу
        else:
            # Ошибка аутентификации
            return render(request, 'courses/home.html', {'error': 'Неправильное имя пользователя или пароль'})
    return render(request, 'courses/user_profile.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'register_form': form})


@login_required
def watch_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    booking = Booking.objects.filter(user=request.user, video=video, is_paid=True).first()

    if booking and booking.is_access_active():
        return render(request, 'courses/watch_video.html', {'video': video})
    else:
        context = {
            'video': video,
            'days_remaining': (booking.purchase_date - timezone.now()).days if booking else 0,
        }
        return render(request, 'courses/access_denied.html', context)


@login_required
def watch_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    booking = Booking.objects.filter(user=request.user, course=course, is_paid=True).first()

    if booking and booking.is_access_active():
        return render(request, 'courses/watch_course.html', {'course': course})
    else:
        return render(request, 'courses/course_detail.html', {
            'course': course,
            'access_denied': True,
        })


@login_required
def watch_webinar(request, webinar_id):
    webinar = get_object_or_404(Webinar, id=webinar_id)
    booking = Booking.objects.filter(user=request.user, webinar=webinar, is_paid=True).first()

    if booking and booking.is_access_active():
        return render(request, 'courses/watch_webinar.html', {'webinar': webinar})
    else:
        return render(request, 'courses/webinar_detail.html', {
            'webinar': webinar,
            'access_denied': True,
        })


@login_required
def user_profile(request):
    # Получаем все оплаченные записи пользователя
    bookings = Booking.objects.filter(user=request.user, is_paid=True)

    # Фильтруем записи, у которых доступ ещё активен
    active_bookings = [booking for booking in bookings if booking.is_access_active() and booking.is_active]

    context = {
        'active_bookings': active_bookings,
        'current_date': timezone.now(),
    }   # Текущая дата

    return render(request, 'courses/user_profile.html', context)


@staff_member_required
def confirm_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.is_paid = True
        booking.payment_confirmed = True
        booking.purchase_date = timezone.now()
        booking.save()
        return redirect('admin_panel')
    return render(request, 'courses/confirm_payment.html', {'booking': booking})