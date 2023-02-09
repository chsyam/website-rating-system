from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import httplib2
from .models import WebsiteModel, Like
from .forms import LikeForm, LoginForm, WebsiteForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from django.conf import settings
import json


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()
            if User.objects.filter(username=username).exists():
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    request.session["user_id"] = user.id
                    request.session['username'] = user.username
                    request.session['password'] = user.password
                    return redirect("dashboard")
                else:
                    messages.info(request, "Invalid Credentials")
                    return redirect('login')
    return render(request, 'HTML/login.html', {'form': form})


@login_required()
def logout(request):
    auth.logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("/")


def register(request):
    if request.method == 'POST':
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(
            username=username, first_name=fname, last_name=lname, email=email, password=password)
        user.save()
        messages.success(request, "successfully registered....!!")
        return redirect("login")
    return render(request, "HTML/register.html")


@login_required
def dashboard(request):
    user_id = request.session['user_id']
    username = request.session['username']
    password = request.session['password']
    all_sites = WebsiteModel.objects.all()
    all_sites_except_current_user = WebsiteModel.objects.all().exclude(user_id=user_id)
    added_list = WebsiteModel.objects.filter(user_id=user_id)
    websites = {
        'all': all_sites,
        'added_list': added_list,
        'all_sites_except_current_user': all_sites_except_current_user,
    }
    for row in added_list:
        likes = Like.objects.filter(website_id=row.id).values()
        up, down = 0, 0
        for i in likes:
            if i['like_or_dislike'] == 1:
                up += 1
            elif i['like_or_dislike'] == -1:
                down += 1
        row.total_likes = up
        row.total_dislikes = down
        row.save()
    form = Like()
    if request.method == 'POST':
        form = LikeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("dashboard")
    return render(request, 'HTML/dashboard.html', {'websites': websites, 'form': form})


# @api_view(["POST"])
# def dictionary_api(user_id):
#     try:
#         user_id = json.loads(user_id.body)
#         # website_id = json.loads(website_id.body)
#         all_sites = WebsiteModel.objects.all()
#         all_sites_except_current_user = WebsiteModel.objects.all().exclude(user_id=user_id)
#         added_list = WebsiteModel.objects.filter(user_id=user_id)
#         for i in added_list:
#             if i.id == 54:
#                 return JsonResponse(str(i.total_likes) + " " + str(i.total_dislikes), safe=False)
#             print(i.total_likes, i.total_dislikes)
#         websites = {
#             'all': all_sites,
#             'added_list': added_list,
#             'all_sites_except_current_user': all_sites_except_current_user,
#         }
#         return JsonResponse("all_sites", safe=False)
#     except ValueError as e:
#         return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@login_required
def add_New_Website(request):
    user_id = request.session['user_id']
    user_name = request.session['username']
    password = request.session['password']
    h = httplib2.Http()
    form = WebsiteForm()
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            url = form['url'].value()
            try:
                response, content = h.request(url)
                if response.status == 200:
                    form.save()
                else:
                    return render(request, "HTML/error.html")
            except:
                return render(request, "HTML/error.html")
            return redirect("dashboard")
        return render(request, 'HTML/addNew.html', {'form': form, 'user_id': user_id})
    return render(request, 'HTML/addNew.html', {'form': form, 'user_id': user_id, 'user_name': user_name})


@login_required
def check(request):
    user_id = request.session['user_id']
    user_name = request.session['username']
    password = request.session['password']
    h = httplib2.Http()
    form = WebsiteForm()
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            url = form['url'].value()
            try:
                response, content = h.request(url)
                if response.status == 200:
                    messages.success(request, "URL is available")
                    return redirect("/dashboard/check")
                else:
                    messages.error(request, "URL is not available")
                    return render(request, "HTML/check.html")
            except:
                messages.error(request, "URL is not available")
                return render(request, "HTML/check.html")
            return redirect("dashboard/check")
        return render(request, 'HTML/check.html', {'form': form, 'user_id': user_id})
    return render(request, 'HTML/check.html', {'form': form, 'user_id': user_id, 'user_name': user_name})


def home(request):
    return render(request, "HTML/home.html")


# def check(request):
#     h = httplib2.Http()
#     form = WebsiteForm()
#     if request.method == 'POST':
#         form = WebsiteForm(request.POST)
#         if form.is_valid():
#             url = form['url'].value()
#             try:
#                 response, content = h.request(url)
#                 if response.status == 200:
#                     form.save()
#                 else:
#                     return render(request, "HTML/error.html")
#             except:
#                 return render(request, "HTML/error.html")
#             return redirect("dashboard")
#         return render(request, 'HTML/addNew.html', {'form': form, 'user_id': user_id})
#     return render(request, 'HTML/addNew.html', {'form': form, 'user_id': user_id, 'user_name': user_name})
