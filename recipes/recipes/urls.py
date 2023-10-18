"""recipes URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))123123123123
"""

from django.urls import path
#from calculator.views import home2
from calculator.views import omlet
from calculator.views import butter
from calculator.views import pasta
from calculator.views import pastaroni

urlpatterns = [
#    path('', home1, name=home22),
    path('butter/', butter, name='butter'),
    path('omlet/', omlet, name='omlet'),
    path('pasta/', pasta, name='pasta'),
    path('pastaroni/', pastaroni, name='pastaroni'),
]
