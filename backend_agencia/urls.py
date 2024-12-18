"""
URL configuration for backend_agencia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('agencia_app.urls')),
    path("cliente_app/",include('cliente_app.urls')),
    path('empleado_app/',include('empleado_app.urls')),
    path('venta_app/',include('venta_app.urls')),
    path('vehiculo_app/',include('vehiculo_app.urls')),
    path('mantenimiento_app/',include('mantenimiento_app.urls')),

]  # type: ignore

