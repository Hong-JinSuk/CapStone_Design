from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime
from timetable.models import Schedule

def save_schedule(request):
    now = datetime.now()

    context = {
        "now": now,
    }

    return render(request, 'ceotimetable/ceotimetable.html')
