from django.shortcuts import render, get_object_or_404
from .models import Entry 
from .forms import EntryForm 
from django.http import HttpResponseRedirect

def index(request):
    entries = Entry.objects.all()
    return render(request, 'myapp/index.html', 
    {'entries': entries})

def details(request, pk):
    Entry= entry.objects.get(id=pk)
    return render(request, "calenderproject/details.html", {"Entry":Entry})

def add(request):
    #if statement Alpha
    if request.method == 'POST':
        
        form = EntryForm(request.POST)
        #if statement Beta 
        if form.is_valid():
            #
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            
            Entry.objects.create(
                name=name,
                date=date,
                description=description
            ).save()

            return HttpResponseRedirect('/')
            
    #else statement Alpha
    else: 
        form = EntryForm()

    return render(request, 'myapp/form.html', {'form': form})