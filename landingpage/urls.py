from django.urls import path

from . import views
app_name = 'landingpage'

urlpatterns = [
    path('new/purpose', views.purpose_new, name='purpose_new'),
    path('<int:estimate_id>/new/type', views.type_of_product_new, name='type_of_product_new'),
    path('<int:estimate_id>/new/photo', views.photo_new, name='photo_new'),
    path('<int:estimate_id>/new/request_content', views.request_content_new, name='request_content_new'),
    path('<int:estimate_id>/new/', views.basic_information_new, name = 'basic_information'),
    path('<int:estimate_id>/new/add_information', views.add_information_new, name = 'add_information'),
    path('new/privacy', views.privacy, name = 'privacy'),
    path('new/privacy/pop', views.privacy_pop, name = 'privacy_pop'),
    path('new/result', views.result, name = 'result'),
    #path('<int:question_id>/', views.detail),
]