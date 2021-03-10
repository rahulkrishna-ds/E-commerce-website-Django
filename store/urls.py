from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('',views.store,name="store"),
	path('cart/',views.cart,name="cart"),
	path('checkout/',views.checkout,name="checkout"),
	path('update_item/',views.updateItem,name="updateItem"),
	path('process_order/',views.processOrder,name="process_order"),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),	
]