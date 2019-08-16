from django.db import models

class Resumeprofile(models.Model):
	candidate_name = models.CharField(max_length=200)
	candidate_mail = models.EmailField()
	resume_file = models.FileField(upload_to='documents/%d%m%Y/')
	resume_date = models.DateTimeField(auto_now_add=True)
	RESUME_STATUS = (
		('Applied', 'Applied'),
		('Viewed', 'Viewed'),
		('Accepted', 'Accepted'),
		('Rejected', 'Rejected')
	)
	resume_status = models.CharField(max_length=15, choices=RESUME_STATUS, default='Applied')
	
	class Meta:
		db_table = "resumeprofile"
