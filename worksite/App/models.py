from django.db import models

import os
import uuid
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True,label='Email',error_messages={'exists':'This mail is already exists'})

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    
    def save(self,commit=True):
        user = super(UserCreateForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class UserDetails(models.Model):
    User_name = models.CharField(max_length= 300)
    User_phone = models.BigIntegerField()
    User_address = models.CharField(max_length= 300)
    User_pic = models.FileField(upload_to = 'media/reportimages')
    def __str__(self):
        return self.User_name


class Admin(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Status(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class WebcamImage(models.Model):
    image = models.ImageField(upload_to = 'media/reportimages')

def generate_filename(instance, filename):
    original_filename, extension = os.path.splitext(filename)
    # Get the latest serial number
    latest_serial_number = Work.objects.count() + 1
    # Generate the new filename with serial number
    new_filename = f"{original_filename}_{latest_serial_number}{extension}"
    return os.path.join('media/reportimages', new_filename)

class Work(models.Model):
    
    
    admin=models.ForeignKey(Admin,on_delete=models.PROTECT,blank=True, null=True)
    status=models.ForeignKey(Status,on_delete=models.PROTECT,blank=True, null=True)
    work=models.CharField(max_length=50, null=True)
    name=models.CharField(max_length=50)
    contact=models.PositiveBigIntegerField(10)

    
    diss=models.CharField(max_length=50,blank=True, null=True)
    vils=models.CharField(max_length=50,blank=True, null=True)
    tal=models.CharField(max_length=50,blank=True, null=True)

    
    pdfname=models.CharField(max_length=50,blank=True, null=True)
    image=models.FileField(upload_to = 'media/reportimages',blank=True, null=True)

    docname=models.CharField(max_length=50,blank=True, null=True)
    document=models.FileField(upload_to = 'media/reportimages',blank=True, null=True)
    othername=models.CharField(max_length=50,blank=True, null=True)
    other=models.FileField(upload_to = 'media/reportimages',blank=True, null=True)
    othername1=models.CharField(max_length=50,blank=True, null=True)
    other1=models.FileField(upload_to = 'media/reportimages',blank=True, null=True)

    un=models.CharField(max_length=50,blank=True, null=True)
    su=models.CharField(max_length=50,blank=True, null=True)
    tp=models.CharField(max_length=50,blank=True, null=True)
    fp=models.CharField(max_length=50,blank=True, null=True)
    bl=models.CharField(max_length=50,blank=True, null=True)
    ca=models.CharField(max_length=50,blank=True, null=True)
    op=models.CharField(max_length=50,blank=True, null=True)
    wo=models.CharField(max_length=50,blank=True, null=True)
    comment =models.CharField(max_length=50,blank=True, null=True)
    


    def __str__(self):
        return self.name
    
    # class Meta:
    #     unique_together = ('image','document','other','other1',)