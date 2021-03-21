from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Job
from django.core.paginator import Paginator
from .form import applyform ,JobForm
from django.contrib.auth.decorators import login_required
from .filters import JobFilters


    
# Create your views here.


def job_list(request):
    job_list = Job.objects.all()


    myfilter = JobFilters(request.GET,queryset=job_list)
    job_list = myfilter.qs

    paginator = Paginator(job_list, 5) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'jobs': page_obj ,'myfilter':myfilter}
    return render(request,'job/job_list.html',context)

   


def job_detail(request , id):
    job_detail = Job.objects.get(id=id)

    if request.method=='POST':
      form = applyform(request.POST ,request.FILES)
      if form.is_valid():
          myform =form.save(commit=False)
          myform.job= job_detail
          myform.save()


    else:
        form = applyform()
    context={'job': job_detail ,'form':form}
    return render(request,'job/job_detail.html',context)


@login_required
def add_job(request):
   if request.method=='POST':
       form = JobForm(request.POST ,request.FILES)
       if form.is_valid():
          myform =form.save(commit=False)
          myform.onwer= request.user
          myform.save()
          return redirect(reverse('joburl:job_list'))
   else:
       form =JobForm()
   

   return render(request,'job/add_job.html',{'form':form})

        


