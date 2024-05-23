# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import CustomUser
from django import forms
from.models import Note
from.forms import NoteForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

@login_required(login_url='login')
def home_view(request):
    current_user = request.user
    users_with_same_role = CustomUser.objects.filter(role=current_user.role)
    context = {'current_user': current_user, 'users_with_same_role': users_with_same_role}
    #persons= CustomUser.objects.filter(role='admin')
    #return render(request, 'home.html', {'persons': persons})
    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


def registration_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration.html', {'form': form})



@login_required(login_url='login')
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})

@login_required(login_url='login')
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    context = {'notes': notes}
    if request.user.role == "moderator" or  request.user.role == "admin":
        context = {'notes': Note.objects.all()}
        
    return render(request, 'note_list.html', context)
