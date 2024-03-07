from product import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = 'product'
# from django.urls import reverse_lazy
urlpatterns = [

    path('', views.Base, name='base'),
    path('product/', views.ProductListView.as_view(), name='index'),
    path('product/detail/<int:pk>',
         views.ProductDetailView.as_view(), name='product_detail'),
    path('product/delete/<int:pk>',
         views.ProductDeleteView.as_view(), name='delete'),
    path('product/update/<int:pk>',
         views.ProductUpdateView.as_view(), name='update'),
    path('product/create/', views.ProductCreateView.as_view(), name='create'),
    path('price/list/', views.ProductPriceList.as_view(), name='price_list'),
    path('category/list/', views.CategoryList.as_view(), name='category_list'),

]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
