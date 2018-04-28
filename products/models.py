from __future__ import unicode_literals

from django.db import models
import json
from pprint import pprint




# Create your models here.




class Product(models.Model):  #Product Category
    category    = models.CharField(max_length=120 , blank = True , null = True)
    courseUrl   = models.CharField(max_length=220,default="NotExist")
    duration    = models.CharField(max_length=120,default="10 weeks")
    image       = models.TextField(default="NotExist")
    name        = models.CharField(max_length=120, default="defaultCourse")
    price       = models.CharField(max_length=120 , default="10 AUD")
    promoMediaUrl       = models.TextField( default="NotExist")
    startDate           = models.CharField(max_length=120, default="15 Dec 2017" , null = True)
    summary             = models.TextField(default="NotExist")
    type                = models.CharField(max_length=120, default="free")
    instructorFullName  = models.CharField(max_length=120 , default="NotExist")
    instructorImageUrl  = models.CharField(max_length=220 ,default="NotExist")
    instructorProfileUrl = models.CharField(max_length=220,default="NotExist")


    def get_absolute_url(self):
        return reverse('products:detail', kwargs={
            'pk': self.pk
            })



    def __str__(self):
        return self.name



class Document(models.Model):
    title = models.CharField(max_length=120)
    filetype = models.CharField(max_length=120)
    data = models.FileField(null=True , blank=True)
    course_id = models.ForeignKey(Product, on_delete=models.CASCADE , default= 850 , null=True , blank = True)

    def __str__(self):
        return self.title


def parser():
    with open( 'F:\Design\Fonts\CoursesWebsite\Courses\products\courseData.json') as data_file:
        data = json.load(data_file)
    # pprint(data)
    # line=line.decode('utf-8','ignore').encode("utf-8")
    return data

# 'F:\DevReal\eCommerce\src\courseData.json'
