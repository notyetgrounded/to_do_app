from django.db import  models
# Create your models here.


# ToDo Model for our ToDo project

class ToDo(models.Model):

    options=(
        ('OPEN','OPEN'),
        ('WORKING','WORKING'),
        ('DONE','DONE'),
        ('OVERDUE','OVERDUE')
    )
    TimeStamp= models.DateTimeField(auto_now_add=True)
    Title= models.CharField(max_length=100)
    Description= models.TextField(max_length=1000)
    DueDate= models.DateField()
    Tag= models.CharField(max_length=10)
    Status= models.CharField(max_length=10,choices=options,default='OPEN')
