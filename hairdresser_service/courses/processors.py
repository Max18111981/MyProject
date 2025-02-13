from .forms import CustomUserCreationForm

def register_form(request):
    form = CustomUserCreationForm()
    return {'register_form': form}