from django.urls import path,include
from . import  views
from django.conf import  settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('store/<str:cat>/',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('store/<str:i>/product/<int:id>',views.product,name='product'),
    path('search/',views.search,name='search'),
    path('update_cart/',views.update_cart,name='update_cart'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name="signup")

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)