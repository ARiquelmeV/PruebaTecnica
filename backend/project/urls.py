"""project URL Configuration

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include ('catalogo.urls')),
]



"""
Bitacora del editor:
    INSTALACION:
    - Se realizo un startproject llamado "project", pero se le hizo el cambio de nombre a la carpeta mayor a "backend"
    - Se instalo vue con npm install -g @vue/cli
    - Se realizo el comando vue create frontend y se selecciono default vue 3
    - Tanto back (django:8000) y front (vue.js:8080) funcionaron correctamente

    PRO TIP:  Para correr el servidor frontend, se necesita el comando npm run serve
    
    Creacion de app catalogo:
    - Creacion de archivo urls.py en catalogo

    Creacion super usuario:
    - alvaro - alvaro@gmail.com - 1234


"""