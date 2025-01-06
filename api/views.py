import json

from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from api.models import User, Token


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
            if "username" in data:
                user.username = data["username"]
            if "password" in data:
                user.password = data["password"]
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
        user.username = data["username"]
        user.password = data["password"]
        user.age = data["age"]
        user.save()
        return JsonResponse({"user": serializers.serialize('python', [user, ])})
    return HttpResponse("<b> Method not allowed, use POST </b>", status=400)

# Login

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists.'}, status=400)
        user = User(username=username, password=password, age=data['age'])
        user.save()
        token = Token.objects.create(user=user)
        return JsonResponse({'token': token.key}, status=201)
    return JsonResponse({'error': 'Invalid request.'}, status=405)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            token = Token.objects.get(user=user)
            return JsonResponse({'token': token.key})
        return JsonResponse({'error': 'Invalid credentials.'}, status=401)
    return JsonResponse({'error': 'Invalid request.'}, status=405)
