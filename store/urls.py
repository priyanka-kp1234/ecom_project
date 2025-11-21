from django.urls import path
from . import views
from store.controller import authview,cart,wishlist,checkout,order

urlpatterns = [
    path('', views.home, name = 'home'),
    path('collections',views.collections, name = 'collections'),
    path('collections/<str:slug>', views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview, name = "productview"),

    path('register/',authview.register, name = 'register'),
    path('login/',authview.loginpage, name = 'loginpage'),
    path('logout/',authview.logoutpage, name = 'logout'),

    path('Add-To-Cart/', cart.addtocart, name='Add-To-Cart'),
    path('cart',cart.viewcart,name = 'cart'),
    path('update_cart/',cart.updatecart,name='update_cart'),
    path('delete-cart-item',cart.deletecartitem,name='delete-cart-item'),

    path('wishlist',wishlist.index,name='wishlist'),
    path('add-to-wishlist/',wishlist.addtowishlist,name='add_to_wishlist'),
    path('delete-wishlist-item',wishlist.deletewishlistitem,name='delete_wishlist_item'),

    path('checkout', checkout.index,name = 'checkout'),
    path('place-order', checkout.placeorder,name = 'placeorder'),
    path('proceed-to-pay/', checkout.razorpaycheck, name = 'proceed-to-pay'),

    path('order/',order.order_view,name='order'),
    path('view-order/<str:t_no>/',order.view_order,name='orderview'),
]