from django.urls import path

from . import views
app_name = 'landingpage'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('estimate/new/', views.estimate_new, name = 'estimate_new'),
    path('estimate/<int:estimate_id>/request/new/', views.request_new, name='request_new'),
]