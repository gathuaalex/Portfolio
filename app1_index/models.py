from django.db import models
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile_image(models.Model):
    image=Cloudinary Field('image',null=True)
    class Meta:
       db_table="profile_photo"
class Profile(models.Model):
    prof_image= models.OneToOneField(
        Profile_image,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name=models.CharField(max_length=50)
    work=models.CharField(max_length=30)
    birthday=models.DateTimeField()
    website=models.CharField(max_length=110)
    email=models.EmailField(max_length=60)
    location=models.CharField(max_length=100)
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,15}?$',message="phone number must be entered in the format:'+2547*******'")
    phone_number=models.CharField(validators=[phone_regex],max_length=14,blank=True)
    class Meta:
       db_table="my_details"
    
    
    def __str__(self):
        return self.name
class Lang(models.Model):
    language_title=models.CharField(max_length=11,default='English')
    language_status=models.CharField(max_length=6,default='fluent')
    language=models.ForeignKey('Profile',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.language_title
class Interests(models.Model):
    interst_title = models.CharField(max_length=20,default='swimming')
    interest=models.ForeignKey('Profile',on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural="Interests"
    def __str__(self):
        return self.interst_title


class Education(models.Model):

    year_of_study=models.CharField(max_length=13)
    achievement=models.CharField(max_length=80)
    institution=models.CharField(max_length=70)
    uni_short_descript=models.TextField(max_length=200)
    profile=models.ForeignKey('Profile',on_delete=models.CASCADE)

    def __str__(self):
        return self.achievement

class Experience(models.Model):
    year_of_experience=models.CharField(max_length=13)
    task=models.CharField(max_length=30)
    company=models.CharField(max_length=30)
    exp_short_descript=models.TextField(max_length=50)
    profile=models.ForeignKey('Profile',on_delete=models.CASCADE)

    def __str__(self):
        return self.task
class Contact_me(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=70)
    message=models.TextField(max_length=700)
    sent_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Skill(models.Model):
    myskill=models.CharField(max_length=100)
    completionper=models.IntegerField()
    def __str__(self):
        return self.myskill
