#-*- coding: utf-8 -*-
from django import forms
from resumesender.models import Resumeprofile

	
class ResumeprofileForm(forms.ModelForm):  

    class Meta:  
        model = Resumeprofile  
        fields = "__all__"  
		
