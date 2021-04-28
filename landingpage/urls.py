from django.urls import path

from . import views
app_name = 'landingpage'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('new/', views.basic_information_new, name = 'basic_information'),
    path('<int:estimate_id>/new/purpose', views.purpose_new, name='purpose_new'),
    path('<int:estimate_id>/new/type', views.type_of_product_new, name='type_of_product_new'),
    path('<int:estimate_id>/new/request', views.request_new, name='request_new'),
    path('<int:estimate_id>/new/add_information', views.add_information_new, name = 'add_information'),
    #path('<int:question_id>/', views.detail),
]