from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
     path('become-seller/', views.become_seller, name='become_seller'),
     path('seller-dashboard/', views.seller_dashboard, name='seller_dashboard'),
     path('add-products/',views.add_product,name='add_product'),
     path('logout/',auth_views.LogoutView.as_view(),name='logout'),
     path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
     path('edit/', views.edit, name='edit'),

]
 