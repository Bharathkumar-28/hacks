"""
URL configuration for djangoproject project.

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
from django.urls import path
from adminpanel import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('index1/',views.index1,name='index1'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('dyslexia/',views.dyslexia,name='dyslexia'),
    path('texttospeech',views.texttospeech,name='texttospeech'),
    path('example/',views.example,name='example'),
    path('resetpassword/<uidb64>/<token>',views.resetpassword,name='resetpassword'),
     path('logout/', views.logout, name='logout'),
     path('about/',views.about,name='about'),
    path('game/',views.game,name='game'),
    path('profiles/',views.profiles,name='profile'),
    path('createprofile/',views.createprofile,name='createprofile'),
    path('contact/',views.contact,name='contact'),
    path('graph/',views.graph,name='graph'),
    path('dinesh/',views.dinesh,name='dinesh'),
    path('speechtotext/',views.speechtotext,name='speechtotext'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
