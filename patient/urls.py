from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:patient_id>/', views.detail, name='detail'),
    path('pulses/<int:patient_id>/', views.get_last_signals, name='get_pulses')
]