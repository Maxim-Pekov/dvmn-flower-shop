"""flowershop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from bucketorderapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('quiz_step/', views.quiz_step_view, name='quiz_step'),
    path('result/', views.result_view, name='result'),
    path('consultation/', views.consultation_view, name='consultation'),
    path('order/', views.order_view, name='order'),
    path('order_step/', views.order_step_view, name='order_step'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
