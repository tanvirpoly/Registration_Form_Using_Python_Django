from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import ResumeForm
from .models import Resume
from django.views import View

class HomeView(View):
 def get(self, request):
  form = ResumeForm()
  candidates = Resume.objects.all()
  return render(request, 'myapp/home.html', { 'candidates':candidates, 'form':form})

 def post(self, request):
  form = ResumeForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   
   # return render(request, 'myapp/home.html', {'form':form})
  return redirect(request.META['HTTP_REFERER'])

class CandidateView(View):
 def get(self, request, pk):
  candidate = Resume.objects.get(pk=pk)
  return render(request, 'myapp/candidate.html', {'candidate':candidate})
 


 

 def HomeView(request, id):
    if request.method == 'POST':
     pi = Resume.object.get(pk=id)
     pi.delete()
    return HttpResponseRedirect('/')
 


    
     

