"""
URL configuration for worksite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from App import views
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('captcha_image/', views.captcha_image, name='captcha_image'),

    path('',views.Homepage,name='index'),
    path('registration/signup/',views.signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('adminmain/',views.adminmain,name='adminmain'),
     path('addwork/',views.addwork,name='addwork'),
    path('viewwork/',views.viewwork,name='viewwork'),
    
    path('editwork(<int:id>)',views.editwork,name='editwork'),
    path('updatework(<int:id>)',views.updatework,name='updatework'),
  #  path('editfirstwork(<int:id>)',views.editfirstwork,name='editfirstwork'),
  #  path('updatefirstwork(<int:id>)',views.updatefirstwork,name='updatefirstwork'),
    path('editwork1(<int:id>)',views.editwork1,name='editwork1'),
    path('sendwork(<int:id>)',views.sendwork,name='sendwork'),
    path('image/',views.usersave,name='capture'),
    path('upload/',views.upload_image, name='upload_image'),
        ###whatsapp
    path('base/',views.base,name='base'),
    
    path('whatsapp/',views.whatsapp,name='whatsapp'),
    # path('whatsapp/senddata',views.senddata,name='senddata'),
    path('getinvoice1(<int:id>)',views.getinvoice1,name='getinvoice1'),
    path('editinvoice1(<int:id>)',views.editinvoice1,name='editinvoice1'),
    path('finalinvoice1/',views.finalinvoice1,name='finalinvoice1'),

    path('user_view/',views.user_view,name='user_view'),
    # path('firstuser/',views.firstuser,name='firstuser'),
    # path('seconduser/',views.seconduser,name='seconduser'),
    # path('thirduser/',views.thirduser,name='thirduser'),
    # path('fourthuser/',views.fourthuser,name='fourthuser'),
  # # # # #

##  USERS ##

# # # # # #

   
    path('user1/',views.user1,name='user1'),
    path('edituser1(<int:id>)',views.edituser1,name='edituser1'),
    path('updateuser1(<int:id>)',views.upadateuser2,name='updateuser1'),


    path('user2/',views.user2,name='user2'),
    path('edituser2(<int:id>)',views.edituser2,name='edituser2'),
    path('updateuser2(<int:id>)',views.upadateuser2,name='updateuser2'),

    path('user3/',views.user3,name='user3'),
    path('edituser3(<int:id>)',views.edituser3,name='edituser3'),
    path('updateuser3(<int:id>)',views.upadateuser3,name='updateuser3'),

    path('user4/',views.user4,name='user4'),
    path('edituser4(<int:id>)',views.edituser4,name='edituser4'),
    path('updateuser4(<int:id>)',views.upadateuser4,name='updateuser4'),

    path('user5/',views.user5,name='user5'),
    path('edituser5(<int:id>)',views.edituser5,name='edituser5'),
    path('updateuser5(<int:id>)',views.upadateuser5,name='updateuser5'),

    path('user6/',views.user6,name='user6'),
    path('edituser6(<int:id>)',views.edituser6,name='edituser6'),
    path('updateuser6(<int:id>)',views.upadateuser6,name='updateuser6'),

    path('user7/',views.user7,name='user7'),
    path('edituser7(<int:id>)',views.edituser7,name='edituser7'),
    path('updateuser7(<int:id>)',views.upadateuser7,name='updateuser7'),

    path('user8/',views.user8,name='user8'),
    path('edituser8(<int:id>)',views.edituser8,name='edituser8'),
    path('updateuser8(<int:id>)',views.upadateuser8,name='updateuser8'),

    path('user9/',views.user9,name='user9'),
    path('edituser9(<int:id>)',views.edituser9,name='edituser9'),
    path('updateuser9(<int:id>)',views.upadateuser9,name='updateuser9'),

    path('user10/',views.user10,name='user10'),
    path('edituser10(<int:id>)',views.edituser10,name='edituser10'),
    path('updateuser10(<int:id>)',views.upadateuser10,name='updateuser10'),

    path('user11/',views.user11,name='user11'),
    path('edituser11(<int:id>)',views.edituser11,name='edituser11'),
    path('updateuser11(<int:id>)',views.upadateuser11,name='updateuser11'),

# # # # #

##  USERS ##

# # # # # #

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

