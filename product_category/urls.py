"""product_category URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.views import View
from product import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexView.as_view(),name='index'),
    path('register',views.RegisterView.as_view(),name='register'),
    path('login',views.LoginUserView.as_view(),name='login'),
    path('profile',views.ProfileView.as_view(),name='profile'),
    path('logout',views.LoginUserView.as_view(),name='logout'),
    path('addproduct',views.AddProductView.as_view(),name='addproduct'),
    path('addcategory',views.AddCategoryView.as_view(),name='addcategory'),
    path('delete/<int:id>/', views.DeleteProductView.as_view(),name='delete'),
    path('home',views.HomePageView.as_view(),name='home'),
    path('search',views.SearchProductView.as_view(),name='searchproduct'),
    path('details/<int:pk>',views.DetailProductView.as_view(),name='details'),
    path('update/<int:pk>',views.UpdateProductView.as_view(),name='update'),
    path('category/<str:category_name>',views.ShowCategoryView.as_view(),name='categorypage'),
    path('categoryprofile/<str:category_name>',views.CategoryProfileView.as_view(),name='categoryprofile'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

