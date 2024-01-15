from django.shortcuts import render
from hr_app.models import JobPost, CandidateApplication, SelectedCandidateJob

# Create your views here.
def hrHome_views(request):
    return render(request, 'hr/hrdashbordh.html')


def post_job_views(request):
    msg = None
    # uploading job to database 
    if request.method == 'POST':
        job_title = request.POST.get('job-title')
        address = request.POST.get('address')
        company_name = request.POST.get('company-name')
        salary_low = request.POST.get('salary-low')
        salary_high = request.POST.get('salary-high')
        last_date  = request.POST.get('last-date')

        # puting to database variable
        jobpost = JobPost(user=request.user,title=job_title,address=address,campanyName=company_name,salaryLow=salary_low,salaryHigh=salary_high,lastDateToApply=last_date)
        jobpost.save()
        msg = 'Job Upload Done..'
    return render(request, 'hr/postjob.html',{'msg':msg})


def candidate_views(request,pk):
    
    return render(request, 'hr/candidate.html')
