from django.urls import path
from .views import ceo_board_list, ceo_board_write, ceo_board_detail
app_name="ceoboards"
urlpatterns = [
    path('ceo_list/', ceo_board_list, name='ceo_board_list'),
    path('ceo_write/', ceo_board_write, name='ceo_board_write'),
    path('ceo_detail/<int:pk>/', ceo_board_detail, name='ceo_board_detail'),
]