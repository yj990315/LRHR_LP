from django.urls import path

from . import views
app_name = 'landingpage'

urlpatterns = [
    path('new/estimate', views.estimate_new, name='estimate_new'),
    path('<int:estimate_id>/new/product', views.product_new, name='product_new'),
    path('<int:estimate_id>/new/photo', views.photo_new, name='photo_new'),
    path('<int:estimate_id>/new/request_content', views.request_content_new, name='request_content_new'),
    path('<int:estimate_id>/new/', views.basic_information_new, name = 'basic_information'),
    path('<int:estimate_id>/new/add_information', views.add_information_new, name = 'add_information'),
    path('<int:estimate_id>/new/privacy', views.privacy, name = 'privacy'),
    path('new/privacy/pop', views.privacy_pop, name = 'privacy_pop'),
    path('<int:estimate_id>/new/result', views.result, name = 'result'),
    #path('<int:question_id>/', views.detail),
]