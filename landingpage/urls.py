from django.urls import path

from . import views
app_name = 'landingpage'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('new/', views.estimate_new, name = 'estimate_new'),
    path('<int:estimate_id>/new/', views.request_new, name='request_new'),
    #path('<int:question_id>/', views.detail),
]