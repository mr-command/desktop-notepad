from django.shortcuts import render,redirect
from .models import Note
from django.conf import settings
from .forms import AddNote 
import os

def save_note_to_desktop(title , content):
    desktop_path = os.path.join(os.path.expanduser("~") , "Desktop")
    file_path = os.path.join(desktop_path , f'{title}.txt')

    with open(file_path , 'w') as file:
        file.write(content)

    return file_path


def myfiles(request):
    all_notes = Note.objects.all()
    return render(request,'myfiles.html',{'notes':all_notes})


def newfile(request):
    all_notes = Note.objects.all()
    return render(request,'newfile.html',{'notes':all_notes})

def newfile2(request):
    if request.method == "POST":
        form = AddNote(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            file_path = save_note_to_desktop(title ,content)

            form.save()
            return redirect('myfile')
    else:
        form = AddNote()
    return render(request,'newfile2.html',{'form':form})

def note(request,nk):
    if request.method == "POST":
        content = request.POST['txt']
    all_notes = Note.objects.get(id=nk)
    return render(request , 'index.html' , {'note':all_notes})
