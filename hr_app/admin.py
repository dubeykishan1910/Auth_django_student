from django.contrib import admin
from hr_app import models 
# Register your models here.

@admin.register(models.Hr)
class HrAdmin(admin.ModelAdmin):
    list_display = ('id','user')


@admin.register(models.JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('id','user','title','address','campanyName','salaryLow','salaryHigh','lastDateToApply','applycount')



@admin.register(models.CandidateApplication)
class CandidateApplication(admin.ModelAdmin):
    list_display = ('id','user','job')



@admin.register(models.SelectedCandidateJob)
class SelectedCandidateJob(admin.ModelAdmin):
    list_display = ('id','job','candidate')