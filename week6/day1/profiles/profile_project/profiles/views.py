from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Profile


@csrf_exempt
def create_profile(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        if name and email:
            profile = Profile.objects.create(name=name, email=email)
            return JsonResponse(
                {"success": True, "message": "Profile created successfully"}
            )
        else:
            return JsonResponse(
                {"success": False, "message": "Name and email are required"}
            )
    else:
        return JsonResponse(
            {"success": False, "message": "Only POST requests are allowed"}
        )


@csrf_exempt
def delete_profile(request, id):
    try:
        profile = Profile.objects.get(id=id)
        profile.delete()
        return JsonResponse(
            {"success": True, "message": "Profile deleted successfully"}
        )
    except Profile.DoesNotExist:
        return JsonResponse({"success": False, "message": "Profile not found"})
