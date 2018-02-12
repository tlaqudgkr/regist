from django.http import HttpResponse

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

# def home(request):
#     html = "<html><body>월요일입니다.</body</html>"
#     return HttpResponse(html)

# 이방법도 있습니다.
# def home(request):
#     return HttpResponse("월요일입니다.")

class Home(TemplateView):
    template_name = 'home.html'

class UserRegister(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserRegisterDone(TemplateView):
    template_name = 'registration/register_done.html'
