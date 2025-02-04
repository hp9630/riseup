from django.shortcuts import render
from django.core.mail import EmailMessage
import os
import pdfkit
from django.http import HttpResponseRedirect
from urllib.parse import quote

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


from django.contrib.auth.decorators import login_required


from App.models import *
from django.http import HttpResponse
from io import BytesIO
from django.http import JsonResponse
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string

from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image,ImageDraw,ImageFont
import random
import string
# Create your views here.


# Create your views here.
def Homepage(request):

    return render(request,'index.html')

def generate_captcha():
    # Generate a random string for CAPTCHA
    captcha_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return captcha_string

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        user_input = request.POST.get('captcha_input', '').upper()
        
    else:
        form = UserCreateForm() 
        
    
    d={'form':form}
    return render(request,'registration/signup.html',d)


def captcha_image(request):
    # Generate a random CAPTCHA string
    captcha_string = generate_captcha()

    # Store the CAPTCHA string in the session for validation
    request.session['captcha_answer'] = captcha_string

    # Create an image
    width, height = 300, 90 
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)

    # Choose a font and size
    font_size = 70
    font = ImageFont.truetype("static/as1/fonts/arial.ttf", font_size)
    

    # Calculate text size and position
    text_width, text_height = draw.textsize(captcha_string, font=font)
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Draw text on the image
    draw.text((x, y), captcha_string, fill='black', font=font)

    # Save the image to a BytesIO object
    image_io = BytesIO()
    image.save(image_io, format='PNG')
    image_io.seek(0)

    # Return the image as an HTTP response
    return HttpResponse(image_io.getvalue(), content_type='image/png')




@login_required
def viewwork(request):
    
    work=Work.objects.all()
    p = {'work':work}
    return render(request,'viewwork.html',p)


@login_required
def user_view(request):
    if request.user.username == 'HARSHMADHAVANI':
        return redirect('user1')
    elif request.user.username == 'ATULBHIMANI':
        return redirect('user2')
    elif request.user.username == 'RICHAPATEL':
        return redirect('user3')
    elif request.user.username == 'MOHITTEJANI':
        return redirect('user4')
    elif request.user.username == 'MITESHDHADUK':
        return redirect('user5')
    elif request.user.username == 'NEHACHOSALA':
        return redirect('user6')
    elif request.user.username == 'STUTIDEVGANIYA':
        return redirect('user7')
    elif request.user.username == 'KARANDARJI':
        return redirect('user8')
    elif request.user.username == 'PRINCESAKARIYA':
        return redirect('user9')
    elif request.user.username == 'AKASHDHADUK':
        return redirect('user10')
    elif request.user.username == 'DHRUVTALAVIYA':
        return redirect('user11')
    else:
        work=Work.objects.all()
        p = {'work':work}
    return render(request,'viewwork.html',p)

@login_required
def firstuser(request): 
    user_work = Work.objects.filter(admin__name="user1")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'firstuser.html',context)
@login_required
def seconduser(request): 
    user_work = Work.objects.filter(admin__name="user2")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'seconduser.html',context)
@login_required
def thirduser(request): 
    user_work = Work.objects.filter(admin__name="user3")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'thirduser.html',context)
@login_required
def fourthuser(request): 
    user_work = Work.objects.filter(admin__name="user4")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'fourthuser.html',context)
@login_required 
def whatsapp(request):
    return render(request,'whatsapp.html')
@login_required
def addwork(request):
    error=""
    # place1=Place.objects.all()
    # dis1=Dis.objects.all()
    # vil1=Vil.objects.all()
    admin1=Admin.objects.all()
    
    if request.method=='POST':
     
      wo = request.POST['work']
      admin = request.POST['admin']
      na = request.POST['name'].upper()
      co = request.POST['contact']
      c = request.POST['comment']
  
      pn = request.POST['pdfname']
      tal = request.POST['tal']
      diss = request.POST['diss']
      vils = request.POST['vils']

      un = request.POST['un']
      su = request.POST['su']
      tp = request.POST['tp']
      fp = request.POST['fp']
      bl = request.POST['bl']
      ca = request.POST['ca']
      op = request.POST['op']
      wo = request.POST['wo']
      
      i=request.FILES.get('image',None)
      
      i1=request.FILES.get('other',None)
   
      admin = Admin.objects.filter(name=admin)
   
      try:
          Work.objects.create(name=na,comment=c,diss=diss,admin=admin,tal=tal,vils=vils,work=wo,contact=co,image=i,other=i1,pdfname=pn,un=un,su=su,tp=tp,fp=fp,bl=bl,ca=ca,op=op,wo=wo)
          error="no"
      except:
          error="yes"


    

    d = {'error':error,'admin':admin1}
          
    return render(request,'addwork.html',d)


@login_required
def deletework(request,aid):
    #if not request.user.is_staff:
    #    return redirect('login')
    patient = Work.objects.get(id=aid)
    patient.delete()
    return redirect('viewwork')

@login_required
def editwork(request,id):
    
    work = Work.objects.get(id=id)
    admin =Admin.objects.all()
    return render(request,'updatework.html',{'work':work,'admin':admin,'id':id})
@login_required
def editfirstwork(request,id):
    
    work = Work.objects.get(id=id)
    return render(request,'updatefirstwork.html',{'work':work,'id':id})
@login_required
def updatefirstwork(request,id):
    print(request)

    update = Work.objects.get(id=id)
    #form= DoctorModelForm(request.POST,instance=update)
    #form.save()
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
      
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      admin = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
      
      update.admin=Admin.objects.filter(name=admin).first()
      update.admin.save()
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      
      update.save()
   
    return redirect('seconduser')


@login_required
def editfourthwork(request,id):
    
    work = Work.objects.get(id=id)
    return render(request,'updatefourthwork.html',{'work':work,'id':id})
@login_required
def updatefourthwork(request,id):
    print(request)

    update = Work.objects.get(id=id)
    #form= DoctorModelForm(request.POST,instance=update)
    #form.save()
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
      
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      admin = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
      
      update.admin=Admin.objects.filter(name=admin).first()
      update.admin.save()
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      
      update.save()
   
    return redirect('fourthuser')


@login_required
def editthirdwork(request,id):
    
    work = Work.objects.get(id=id)
    return render(request,'updatethirdwork.html',{'work':work,'id':id})
@login_required
def updatethirdwork(request,id):
    print(request)

    update = Work.objects.get(id=id)
    #form= DoctorModelForm(request.POST,instance=update)
    #form.save()
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
      
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      admin = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
      
      update.admin=Admin.objects.filter(name=admin).first()
      update.admin.save()
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      
      update.save()
   
    return redirect('thirduser')




@login_required
def updatework(request,id):
    print(request)

    update = Work.objects.get(id=id)
    
    #form= DoctorModelForm(request.POST,instance=update)
    #form.save()
    if request.method=='POST':
    
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      a = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
     
      
      update.admin=Admin.objects.filter(name=a).first()
      
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      update.admin.save()
      update.save()
   
    return redirect('viewwork')
@login_required
def editwork1(request,id):
    
    work = Work.objects.get(id=id)
    admin =Admin.objects.all()
    return render(request,'sendwork.html',{'work':work,'admin':admin,'id':id})
@login_required
def sendwork(request,id):

    print(request)

    update = Work.objects.get(id=id)
    if request.method == 'POST':
        
        n = request.POST.get('name').upper()
        c = request.POST.get('contact')
        
        if c and n:
            # Define your message with placeholders for n and c
            message = f"Greetings from Riseup associates.\nFile number: RAU-{id}-2024\nClient name: {n} has been updated.\nFor more information visit: www.riseupassociates.com"
            
            # Construct the URL with the encoded message
            url = f"https://api.whatsapp.com/send?phone={c}&text={quote(message)}"
            
            
            # Redirect to WhatsApp with the pre-filled message
            return HttpResponseRedirect(url)
      

    return redirect('viewwork')
######
#work Part end
#####

def usersave(request):
 error=""
 if request.method== 'POST':        
    User_name = request.POST["Username"]
    User_phone = request.POST["Userphone"]
    User_address = request.POST["Useraddress"]
    print()
    pic = request.FILES["photo"]
    try:
        UserDetails.objects.create(User_name=User_name, User_phone=User_phone, User_address=User_address, User_pic= pic)
        error="no"
    except:
          error="yes"
 d = {'error':error}  
 return render(request, 'capture.html',d)
def upload_image(request):
    if request.method == 'POST':
        form = WebcamImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})
@login_required
def adminmain(request):
    #if not request.user.is_staff:
   #     return redirect('login')

    return render(request,'adminmain.html')

def base(request):
    return render(request,'base.html')
@login_required
def editinvoice1(request,id):
    work = Work.objects.get(id=id)
    return render(request,'getinvoice1.html',{'id':id,'work':work,})
@login_required
def getinvoice1(request,id):
    update = Work.objects.get(id=id)
    if request.method=='POST':
      id = request.POST.get('id')
      work = request.POST.get('work')
      name = request.POST.get('name')
      contact = request.POST.get('contact')

      a = request.POST.get('diss')
      b = request.POST.get('tal')
      d = request.POST.get('vils')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')

     

      update.work=work
      update.name=name
      update.contact=contact
      update.diss=a
      
      update.tal=b
     
      update.vils=d
      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
      update.save()
      
    return redirect('finalinvoice1')
@login_required
def finalinvoice1(request):
    if request.method=='POST':
      id = request.POST['id']
      work = request.POST['work']
      name = request.POST['name']
      contact = request.POST['contact']

      diss = request.POST['diss']
      vils = request.POST['vils']
      tal = request.POST['tal']

      un = request.POST['un']
      fp = request.POST['fp']
      tp = request.POST['tp']
      bl = request.POST['bl']
      wo = request.POST['wo']
      su = request.POST['su']
      ca = request.POST['ca']
      op = request.POST['op']

      request.session['id']=id
      request.session['work']=work
      request.session['name']=name
      request.session['contact']=contact

      request.session['diss']=diss
      request.session['tal']=tal
      request.session['vils']=vils

      request.session['un']=un
      request.session['fp']=fp
      request.session['tp']=tp
      request.session['op']=op
      request.session['bl']=bl
      request.session['wo']=wo
      request.session['ca']=ca
      request.session['su']=su

      
     

      request.session.save()
      
      return render(request,'finalinvoice1.html',{'id':id,'work':work,'name':name,'contact':contact,'diss':diss,'vils':vils,'tal':tal,'un':un,'fp':fp,'tp':tp,'op':op,'su':su,'bl':bl,'ca':ca,'wo':wo})
    return render(request,'viewwork.html')


#     #   ######
#     #       #
#     #   ######
#######  ######


@login_required
def user1(request): 
    user_work = Work.objects.filter(admin__name="HARSHMADHAVANI")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'user1.html',context)
@login_required
def user2(request): 
    user_work = Work.objects.filter(admin__name="ATULBHIMANI")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'user2.html',context)

@login_required
def user3(request): 
    user_work = Work.objects.filter(admin__name="RICHAPATEL")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'user3.html',context)

@login_required
def user4(request): 
    user_work = Work.objects.filter(admin__name="MOHITTEJANI")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'user4.html',context)
@login_required
def user5(request): 
    user_work = Work.objects.filter(admin__name="MITESHDHADUK")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'user5.html',context)

@login_required
def user6(request): 
    user_work = Work.objects.filter(admin__name="NEHACHOSALA")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'user6.html',context)

@login_required
def user7(request): 
    user_work = Work.objects.filter(admin__name="STUTIDEVGANIYA")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'user7.html',context)
@login_required
def user8(request): 
    user_work = Work.objects.filter(admin__name="KARANDARJI")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'user8.html',context)

@login_required
def user9(request): 
    user_work = Work.objects.filter(admin__name="PRINCESAKARIYA")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'user9.html',context)
@login_required
def user10(request): 
    user_work = Work.objects.filter(admin__name="AKASHDHADUK")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'user10.html',context)
@login_required
def user11(request): 
    user_work = Work.objects.filter(admin__name="DHRUVTALAVIYA")

    # Exclude the user_work queryset to get all other Work objects
   
    context = {
        'user_work': user_work,
        
    }
    return render(request, 'user11.html',context)


#     #   ######
#     #       #
#     #   ######
#######  ######

#     #   ######
#     #   #    #
#     #   ######
#######  
@login_required
def edituser1(request,id):
    
    work = Work.objects.get(id=id)
    admin =Admin.objects.all()
    return render(request,'upadateuser1.html',{'work':work,'admin':admin,'id':id})
@login_required
def upadateuser1(request,id):
    print(request)

    update = Work.objects.get(id=id)
    #form= DoctorModelForm(request.POST,instance=update)
    #form.save()
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
      
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      admin = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
      
      update.admin=Admin.objects.filter(name=admin).first()
      update.admin.save()
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      
      update.save()
   
    return redirect('user1')

#####user 2

@login_required
def edituser2(request,id):
    
    work = Work.objects.get(id=id)
    admin =Admin.objects.all()
    return render(request,'upadateuser2.html',{'work':work,'admin':admin,'id':id})
@login_required
def upadateuser2(request,id):
    print(request)

    update = Work.objects.get(id=id)
    #form= DoctorModelForm(request.POST,instance=update)
    #form.save()
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
      
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      admin = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
      
      update.admin=Admin.objects.filter(name=admin).first()
      update.admin.save()
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      
      update.save()
   
    return redirect('user2')
#####user2 end


#####user 3

@login_required
def edituser3(request,id):
    
    work = Work.objects.get(id=id)
    admin =Admin.objects.all()
    return render(request,'upadateuser3.html',{'work':work,'admin':admin,'id':id})
@login_required
def upadateuser3(request,id):
    print(request)

    update = Work.objects.get(id=id)
    #form= DoctorModelForm(request.POST,instance=update)
    #form.save()
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
      
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      admin = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
      
      update.admin=Admin.objects.filter(name=admin).first()
      update.admin.save()
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      
      update.save()
   
    return redirect('user3')
#####user3 end


#####user 4

@login_required
def edituser4(request,id):
    
    work = Work.objects.get(id=id)
    admin =Admin.objects.all()
    return render(request,'upadateuser4.html',{'work':work,'admin':admin,'id':id})
@login_required
def upadateuser4(request,id):
    print(request)

    update = Work.objects.get(id=id)
    
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
      
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      admin = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
      
      update.admin=Admin.objects.filter(name=admin).first()
      update.admin.save()
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      
      update.save()
   
    return redirect('user4')


#####user 5

@login_required
def edituser5(request,id):
    
    work = Work.objects.get(id=id)
    admin =Admin.objects.all()
    return render(request,'upadateuser5.html',{'work':work,'admin':admin,'id':id})
@login_required
def upadateuser5(request,id):
    print(request)

    update = Work.objects.get(id=id)
    
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
      
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      admin = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
      
      update.admin=Admin.objects.filter(name=admin).first()
      update.admin.save()
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      
      update.save()
   
    return redirect('user5')
#####user5 end
#####user 6

@login_required
def edituser6(request,id):
    
    work = Work.objects.get(id=id)
    admin =Admin.objects.all()
    return render(request,'upadateuser6.html',{'work':work,'admin':admin,'id':id})
@login_required
def upadateuser6(request,id):
    print(request)

    update = Work.objects.get(id=id)
    
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
      
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      admin = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
      
      update.admin=Admin.objects.filter(name=admin).first()
      update.admin.save()
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      
      update.save()
   
    return redirect('user6')
#####user6 end




#####user 7

@login_required
def edituser7(request,id):
    
    work = Work.objects.get(id=id)
    admin =Admin.objects.all()
    return render(request,'upadateuser7.html',{'work':work,'admin':admin,'id':id})
@login_required
def upadateuser7(request,id):
    print(request)

    update = Work.objects.get(id=id)
    
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
      
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      admin = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
      
      update.admin=Admin.objects.filter(name=admin).first()
      update.admin.save()
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      
      update.save()
   
    return redirect('user7')
#####user7 end

#####user 8

@login_required
def edituser8(request,id):
    
    work = Work.objects.get(id=id)
    admin =Admin.objects.all()
    return render(request,'upadateuser8.html',{'work':work,'admin':admin,'id':id})
@login_required
def upadateuser8(request,id):
    print(request)

    update = Work.objects.get(id=id)
    
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
      
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      admin = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
      
      update.admin=Admin.objects.filter(name=admin).first()
      update.admin.save()
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      
      update.save()
   
    return redirect('user8')
#####user8 end

#####user 9

@login_required
def edituser9(request,id):
    
    work = Work.objects.get(id=id)
    admin =Admin.objects.all()
    return render(request,'upadateuser9.html',{'work':work,'admin':admin,'id':id})
@login_required
def upadateuser9(request,id):
    print(request)

    update = Work.objects.get(id=id)
    
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
      
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      admin = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
      
      update.admin=Admin.objects.filter(name=admin).first()
      update.admin.save()
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      
      update.save()
   
    return redirect('user9')
#####user9 end


#####user 10

@login_required
def edituser10(request,id):
    
    work = Work.objects.get(id=id)
    admin =Admin.objects.all()
    return render(request,'upadateuser10.html',{'work':work,'admin':admin,'id':id})
@login_required
def upadateuser10(request,id):
    print(request)

    update = Work.objects.get(id=id)
    
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
      
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      admin = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
      
      update.admin=Admin.objects.filter(name=admin).first()
      update.admin.save()
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      
      update.save()
   
    return redirect('user10')
#####user10 end


#####user 10

@login_required
def edituser11(request,id):
    
    work = Work.objects.get(id=id)
    return render(request,'upadateuser11.html',{'work':work,'id':id})
@login_required
def upadateuser11(request,id):
    print(request)

    update = Work.objects.get(id=id)
    
    if request.method=='POST':
      if len(request.FILES) !=0:
          if len(update.image)>0:
              os.remove(update.image.path)
              update.image =request.FILES['image']
      
      wo = request.POST.get('work')        
      n = request.POST.get('name')
      c = request.POST.get('contact')
      a = request.POST.get('dis')
      b = request.POST.get('place')
      d = request.POST.get('vil')
      admin = request.POST.get('admin')
      e = request.POST.get('un')
      f = request.POST.get('su')
      g = request.POST.get('tp')
      h = request.POST.get('fp')
      i = request.POST.get('bl')
      j = request.POST.get('ca')
      k = request.POST.get('op')
      l = request.POST.get('wo')
      com = request.POST.get('comment')
      update.work=com
      update.work=wo
      update.name=n
      update.contact=c
      update.diss=a
      
      update.admin=Admin.objects.filter(name=admin).first()
      update.admin.save()
      update.tal=b
      
      update.vils=d
      
     

      update.un=e
      update.su=f
      update.tp=g
      update.fb=h
      update.bl=i
      update.ca=j
      update.op=k
      update.wo=l
    
      

      
      update.save()
   
    return redirect('user11')
#####user11 end
#     #   ######
#     #   #    #
#     #   ######
#######  