from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse


def dashboard(request):
    resumes = Profile.objects.all()
    return render(
        request,
        "myapp/modern_dashboard.html",
        {"resumes": resumes}
    )


def save_profile(request):

    if request.method == "GET":
        return render(
            request,
            "myapp/accept.html"
        )

    if request.method == "POST":

        profile = Profile(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            degree=request.POST.get("degree"),
            school=request.POST.get("school"),
            university=request.POST.get("university"),
            summary=request.POST.get("summary"),
            previous_work=request.POST.get("previous_work"),
            skills=request.POST.get("skills"),
        )

        profile.save()

        return redirect("dashboard")


def resume(request, id):

    user_profile = get_object_or_404(
        Profile,
        id=id
    )

    return render(
        request,
        "myapp/resume.html",
        {"user_profile": user_profile}
    )


def downloadresume(request, id):

    profile = get_object_or_404(
        Profile,
        id=id
    )

    template = get_template(
        "myapp/downloadresume.html"
    )

    html = template.render({
        "profile": profile
    })

    response = HttpResponse(
        content_type="application/pdf"
    )

    response["Content-Disposition"] = (
        f'attachment; filename="{profile.name}_Resume.pdf"'
    )

    pisa_status = pisa.CreatePDF(
        html,
        dest=response
    )

    if pisa_status.err:
        return HttpResponse(
            "Error generating PDF"
        )

    return response