from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .models import Profile
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
import io


def dashboard(request):
    resumes = Profile.objects.all()
    return render(request,'myapp/modern-dashboard.html',{'resumes':resumes})


def save_profile(request):
    if request.method=="POST":
        # Step1: Get the data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        degree = request.POST.get('degree')
        school = request.POST.get('school')
        university = request.POST.get('university')
        summary = request.POST.get('summary')
        previous_work = request.POST.get('previous_work')
        skills = request.POST.get('skills')
        # Step 2: Save data into database
        profile = Profile(name=name,email=email,phone=phone,degree=degree,school=school,university=university,summary=summary,previous_work=previous_work,skills=skills)
        profile.save()
        return redirect('dashboard')

    return render(request,'myapp/modern_create_profile.html')


def resume(request,id):
    user_profile = Profile.objects.get(id=id)
    return render(request,'myapp/modern-resume.html',{'user_profile':user_profile})


def edit_profile(request,id):
    user_profile = get_object_or_404(Profile,id=id)
    if request.method=="POST":
        user_profile.name = request.POST.get('name')
        user_profile.email = request.POST.get('email')
        user_profile.phone = request.POST.get('phone')
        user_profile.degree = request.POST.get('degree')
        user_profile.school = request.POST.get('school')
        user_profile.university = request.POST.get('university')
        user_profile.summary = request.POST.get('summary')
        user_profile.previous_work = request.POST.get('previous_work')
        user_profile.skills = request.POST.get('skills')
        user_profile.save()
        return redirect('dashboard')
    return render(request,'myapp/modern_create_profile.html',{'user_profile':user_profile})


@require_POST
def delete_profile(request,id):
    user_profile = get_object_or_404(Profile,id=id)
    user_profile.delete()
    return redirect('dashboard')


def download_resume(request,id):
    user_profile = get_object_or_404(Profile,id=id)
    template_path = 'myapp/download_resume.html'
    context=  {'profile':user_profile}
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= f'attachment; filename={user_profile.name}_CV.pdf'
    pisa_status = pisa.CreatePDF(io.BytesIO(html.encode('UTF-8')),dest=response,encoding='UTF-8')
    if pisa_status.err:
        return HttpResponse('Error generating PDF',status=500)
    return response
