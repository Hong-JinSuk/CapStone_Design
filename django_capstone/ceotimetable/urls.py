from django.urls import path

from timetable import views

app_name="ceotimetable"
urlpatterns = [
    path('save_schedule/', views.save_schedule, name='save_schedule'),
]