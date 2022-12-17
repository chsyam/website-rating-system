from django.shortcuts import render,redirect
import httplib2
from .models import User,WebsiteModel,Like,User
from .forms import UserForm,WebsiteForm,LikeForm,LoginForm

def index(request):
    added_list = WebsiteModel.objects.all()
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
        return redirect("/")
    return render(request, 'HTML/index.html', {'list': added_list})


def user_index(request,user_id):
    added_list = WebsiteModel.objects.filter(user_id=user_id)
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
        return redirect("/")
    return render(request, 'HTML/user_index.html', {'list': added_list, 'form': form})

def add_New_Website(request):
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
                    return render(request,"HTML/error.html")
            except:
                return render(request, "HTML/error.html")
        return redirect("/")
    return render(request, 'HTML/addNew.html', {'form': form})

def check(request, url):
    h = httplib2.Http()
    url = "https://www.w3schools.com/python/python_try_except.asp"
    try:
        response, content = h.request(url)
        if response.status == 200:
            return render(request, 'HTML/index.html')
    except:
        return render(request, "HTML/error.html")
    return render(request, "HTML/error.html")

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request,"HTML/register.html",{'form':form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            mail = form['email'].value()
            password = form['password'].value()
            users = User.objects.filter(email=mail).filter(password = password)
            print(len(users))
            if len(users) > 0:
                return redirect("/")
    return render(request, 'HTML/login.html', {'form':form})
