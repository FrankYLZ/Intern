from django.urls import path
from . import views

app_name = 'stocks'

urlpatterns = [
    # path('login_home/', views.home, name='home'),
    path('predict_price/', views.predict_price, name='predict_price'),
    path('clear_history/', views.clear_history, name='clear_history'),
]
