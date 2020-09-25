from django.db import models

# Create your models here.


'''
    import from moodle for :
    -htmal widget
    -validation
    - db size 

'''

Job_Type=(
    ("Full Time","Full Time"),
    ("Part Time","Part Time")

)


class Job(models.Model):  #tabdle
    title=models.CharField(max_length=100) #column
# we do make migration after create table and coulmn to let django check the table and coulmn able to creat and add to DB and after that we do migrate
    #location
    job_type=models.CharField(max_length=20 , choices= Job_Type)
    descripyion=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    Vacancy =models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)


    #return name of job in admin panal
    def __str__(self):
        return self.title

       