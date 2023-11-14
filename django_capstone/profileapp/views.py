from django.shortcuts import render,redirect
from profileapp.forms import ProfileCreateForm
from profileapp.models import Profile
from django.views.generic import CreateView
from datetime import datetime

def ProfileCreateView(request):
    now=datetime.now()
    context = {
        "now":now
    }
    model=Profile
    context_object_name='target_profile'
    form_class=ProfileCreateForm
    success_url = redirect('ceo_main')
    template_name = 'profileapp/create.html'
    return render(request,'create.html',context)
