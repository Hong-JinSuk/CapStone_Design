from django.urls import path
from .views import ceo_register, ceo_login, logout
app_name="ceo_accounts"
urlpatterns = [
    path('ceo_register/', ceo_register, name='ceo_register'),
    path('ceo_login/', ceo_login, name='ceo_login'),
    path('logout/', logout, name='logout'),
]