from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from resumesender.forms import ResumeprofileForm
from .models import Resumeprofile

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import datetime
from datetime import date

def index(request):
	"""View function for home page of site."""

	num_resumes = Resumeprofile.objects.all().count()  
	num_resumes_applied = Resumeprofile.objects.filter(resume_status__exact='Applied').count()
	num_resumes_viewed = Resumeprofile.objects.filter(resume_status__exact='Viewed').count()
	num_resumes_accepted = Resumeprofile.objects.filter(resume_status__exact='Accepted').count()
	num_resumes_rejected = Resumeprofile.objects.filter(resume_status__exact='Rejected').count()	

	contxt = {
		'num_resumes': num_resumes,
		'num_resumes_applied': num_resumes_applied,
		'num_resumes_viewed': num_resumes_viewed,
		'num_resumes_accepted': num_resumes_accepted,
		'num_resumes_rejected': num_resumes_rejected,	
	}

	# Render the HTML template index.html with the data in the context variable
	return render(request, 'index.html', context=contxt)

def hello(request):
   text = """<h1>Welcome to ABC consultant company - Resume Site!</h1>"""
   return HttpResponse(text)

def SaveProfile(request):
	saved = False

	if request.method == "POST":
		#Get the posted form
		MyProfileForm = ResumeprofileForm(request.POST, request.FILES)

		if MyProfileForm.is_valid():
			 profile = Resumeprofile()
			 profile.candidate_name = MyProfileForm.cleaned_data["candidate_name"]
			 profile.candidate_mail = MyProfileForm.cleaned_data["candidate_mail"]
			 profile.resume_file = MyProfileForm.cleaned_data["resume_file"]
			 profile.resume_date = date.today()#MyProfileForm.cleaned_data["resume_date"]
			 profile.resume_status = MyProfileForm.cleaned_data["resume_status"]
			 profile.save()
			 saved = True
	else:
		MyProfileForm = ResumeprofileForm()

	return render(request, 'profilesaved.html', locals())
	
#CRUD
def prof(request):  
    if request.method == "POST":  
        form = ResumeprofileForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('showall')  
            except:  
                pass  
    else:  
        form = ResumeprofileForm()  
    return render(request,'profilesaved.html',{'form':form})  

@login_required
def show(request):  
    profiles= Resumeprofile.objects.all()  
    return render(request,"show.html",{'profiles':profiles})  

@login_required
def edit(request, id):  
    profile = Resumeprofile.objects.get(id=id)  
    return render(request,'edit.html', {'profile':profile})  
	
@login_required	
def update(request, id):  
    profile = Resumeprofile.objects.get(id=id)  
    form = ResumeprofileForm(request.POST, instance = profile)  
    if form.is_valid():  
        form.save()  
        return redirect("showall")  
    return render(request, 'edit.html', {'profile': profile})  

@login_required	
def destroy(request, id):  
    profile = Resumeprofile.objects.get(id=id)  
    profile.delete()  
    return redirect("showall")