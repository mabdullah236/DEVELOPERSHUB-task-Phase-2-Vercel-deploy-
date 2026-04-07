"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.http import HttpResponse

def home(request):
    html = """
    <html>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
            <h1>📚 Welcome to Bookstore API</h1>
            <br>
            <a href="/api/books/" style="padding: 7px 20px; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 5px;">Go to Books API</a>
            <br><br>
            <a href="/admin/" style="padding: 7px 20px; background-color: #008CBA; color: white; text-decoration: none; border-radius: 5px;">Go to Admin Panel</a>
        </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('books.urls')),
    path('', home, name='home'),
]



