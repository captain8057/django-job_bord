from django.forms import ModelForm
from job.models import apply ,Job



class applyform(ModelForm):
    class Meta:
        model = apply
        fields=['name','email','websit','cv','cover_leteer']        




class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__' 
        exclude =('slug','onwer')


      



