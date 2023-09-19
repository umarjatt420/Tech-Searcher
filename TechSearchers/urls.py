"""blogsearchers URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blogs.views import Home
from blogs.views import blog_detail
from blogs.views import AI
from blogs.views import IT
from blogs.views import CN
from blogs.views import Programming
from blogs.views import OS
from blogs.views import Robotics
from blogs.views import QC
from blogs.views import DS
from blogs.views import Automation
from blogs.views import VR
from blogs.views import Blogs
from blogs.views import Contact
from blogs.views import About
from blogs.views import Terms
from blogs.views import PrivacyPolicy
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view()),
    path('blogs/<int:blog_id>', blog_detail),
    path('contact-us/', Contact.as_view()),
    path('about-us/', About.as_view()),
    path('terms&conditions/', Terms.as_view()),
    path('privacy-policy/', PrivacyPolicy.as_view()),
    path('category/artificial-intelligence/', AI.as_view()),
    path('category/information-technology/', IT.as_view()),
    path('category/computer-networks/', CN.as_view()),
    path('category/programming/', Programming.as_view()),
    path('category/operating-systems/', OS.as_view()),
    path('category/robotics/', Robotics.as_view()),
    path('category/quantum-computing/', QC.as_view()),
    path('category/data-science/', DS.as_view()),
    path('category/automation/', Automation.as_view()),
    path('category/virtual-reality/', VR.as_view()),
    path('blogs/', Blogs.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
