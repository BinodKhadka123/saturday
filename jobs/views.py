from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_list_or_404
from django.http import Http404
from .models import Jobs  # Importing the Jobs model

def index(request):
    #try:
        
       # jobs = Jobs.objects.all()
       # print(jobs)  

  
       # context = {
       ###     'jobs': jobs
       # }

   # except Jobs.DoesNotExist:
       
       # raise Http404("Error: does not exist")
             jobs=get_list_or_404(Jobs)
             return render(request, 'jobs/index.html',{'jobs': jobs} )
class JobList(ListView):
        model=Jobs
        context_object_name="jobs"
        template_name="jobs/index.html"
        
        def get_queryset(self):
                return Jobs.objects.order_by("vacancy")
        
class JobDetailView(DetailView):
    model = Jobs
    context_object_name="jobs"
    template_name='jobs/job_detail.html'