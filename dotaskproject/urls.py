"""
URL configuration for dotaskproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from dotaskapp import views
from dotaskproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.Dolistview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.Dodetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.Doupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.Dodeleteview.as_view(), name="cbvdelete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)