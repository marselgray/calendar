from django.shortcuts import render, get_object_or_404, redirect
from .models import Entry 
from .forms import EntryForm 
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'myapp/index.html')

@login_required
def calendar(request):
    entries = Entry.objects.filter(author=request.user)
    return render(request, 'myapp/calendar.html',
        {'entries': entries})

@login_required
def details(request, pk):
    Entry= entry.objects.get(id=pk)
    return render(request, "calenderproject/details.html", {"Entry":Entry})

# add an event
@login_required
def add(request):
    #if statement Alpha
    if request.method == 'POST':
        
        form = EntryForm(request.POST)
        #if statement Beta (no else)
        if form.is_valid():
            #
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            
            Entry.objects.create(
                name=name,
                author=request.user,
                date=date,
                description=description
            ).save()

            return HttpResponseRedirect('/')
            
    #else statement Alpha
    else: 
        form = EntryForm()

    #returns the form 
    return render(request, 'myapp/form.html', {'form': form})

# delete an event
@login_required
def delete(request, pk):
    
    #if statement Charlie (no else)
    if request.method == 'DELETE':
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()

    return HttpResponseRedirect('/')


def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/calendar')

    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})