from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('delete/<list_id>', delete, name = 'delete'),
    path('cross_off/<list_id>', cross_of, name = 'cross'),
    path('uncross/<list_id>', uncross, name = 'uncross'),
    path('edit/<list_id>', edit, name = 'edit'),
]