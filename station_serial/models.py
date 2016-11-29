from django.db import models

# Create your models here.


class command_list(models.Model):
    key = models.CharField(db_index=True,max_length=1000) ;
    code = models.CharField(max_length=1000) ;

class value_list(models.Model):
    key = models.CharField(db_index=True,max_length=1000) ;
    code = models.CharField(max_length=1000) ;

class log(models.Model):
    datetime = models.DateTimeField(auto_now_add=True,db_index = True);
    cmd  = models.CharField(max_length=1000) ; 
    rt_value =  models.CharField(max_length=1000) ;


