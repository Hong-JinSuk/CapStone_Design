from django.urls import path
import profileapp.views

app_name="profileapp"

urlpatterns = [
    path('create/',profileapp.views.ProfileCreateView , name='create'),
]