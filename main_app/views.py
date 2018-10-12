from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import User, Skill
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class SkillCreate(CreateView):
    model = Skill
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/skills/')

# class SkillUpdate(UpdateView):
#     model = Skill
#     fields = ['name', 'description' 'level']


# class SkillDelete(DeleteView):
#     model = CatToy
#     success_url = '/cattoys'


# class CatCreate(CreateView):
#     model = Cat
#     fields = ['name', 'breed', 'description', 'age', 'cattoys']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/skills/')


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
                    return HttpResponseRedirect('/')
            else:
                print("The username and/or password is incorrect.")
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return redirect('/signup/')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def skills_index(request):
    skills = request.user.skill_set.all()
    return render(request, 'skills/index.html', {'skills': skills})


def skills_detail(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    return render(request, 'skills/detail.html', {'skill': skill})
