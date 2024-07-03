from django.shortcuts import render, get_object_or_404

from .models import Skill

# Create your views here.

def starting_page(request):
    latest_skills = Skill.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "skills": latest_skills
    })


def posts(request):
    all_skills = Skill.objects.all().order_by("-date")
    return render(request, "blog/all-skills.html", {
        "skills": all_skills
    })


def post_details(request, slug):
    indetified_skill =  get_object_or_404(Skill, slug=slug)
    return render(request, "blog/skill-detail.html", {
        "skill": indetified_skill,
        "skill_tags": indetified_skill.tags.all()
    })
