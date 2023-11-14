from django.urls import path

from timetable import views

app_name="timetable"
urlpatterns = [
    path('save_schedule/', views.save_schedule, name='save_schedule'),
    path('list/', views.save_schedule, name='save_schedule'),
]