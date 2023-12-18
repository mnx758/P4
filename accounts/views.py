from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import Formsingup
from django.urls import reverse_lazy
class Usercreate(CreateView):
    form_class = Formsingup
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'