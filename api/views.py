import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from api.models import User


@csrf_exempt
def get_and_post(request):
    if request.method == "GET":
        return JsonResponse({"method": "GET"})
    elif request.method == "POST":
        return redirect("redirected", permanent=True)

def redirected(request):
    return JsonResponse({"text": "redirected"})

def all_users(request):
    return JsonResponse({"users": serializers.serialize('python', User.objects.all())})

@csrf_exempt
def update_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        if request.method == "POST":
            data = json.loads(request.body)
            if "name" in data:
                user.name = data["name"]
            if "age" in data:
                user.age = data["age"]
            user.save()
            return JsonResponse({"success": True,
                                 "updated_user": serializers.serialize('python', [user, ])})
        else:
            return HttpResponse("<b> Method not allowed, use POST </b>", status=400)
    except User.DoesNotExist:
        return JsonResponse({"success": False, "error": "User not found"}, status=404)

def delete_user(request, pk):
    try:
        person = User.objects.get(pk=pk)
        person.delete()
        return JsonResponse({"success": True})
    except User.DoesNotExist:
        return JsonResponse({"success": False, "error": "User not found"}, status=404)

@csrf_exempt
def add_user(request):
    if request.method == "POST":
        user = User()
        data = json.loads(request.body)
        user.name = data["name"]
        user.age = data["age"]
        user.save()
        return JsonResponse({"user": serializers.serialize('python', [user, ])})
    return HttpResponse("<b> Method not allowed, use POST </b>", status=400)