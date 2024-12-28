from django.contrib import admin
from django.urls import path
from ecommerce import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.OrderItems.as_view(), name='home'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('headphones/', views.Headphones.as_view(), name='headphones'),
    path('speakers/', views.Speakers.as_view(), name='speakers'),
    path('earphones/', views.Earphones.as_view(), name='earphones'),
    path('headphone/<int:pk>/', views.HeadphoneDetail.as_view(), name='headphone_detail'),
    path('speaker/<int:pk>/', views.SpeakerDetail.as_view(), name='speaker_detail'),
    path('earphone/<int:pk>/', views.EarphoneDetail.as_view(), name='earphone_detail'),
    path('cartquantity/', views.AddCartItemNumber.as_view(), name='cartquantity'),
    path('post/', views.AddToCart.as_view(), name='post'),
    path('checkoutinfo/', views.CheckoutDetails.as_view(), name='checkoutinfo'),
    
    # Login and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Register
    path('register/', views.register, name='register'),  # Custom register view

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
