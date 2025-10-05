from django.shortcuts import render, redirect, get_object_or_404  # type:ignore
from django.contrib import messages  # type:ignore
from .models import Credential
from .forms import CredentialForm  # type:ignore

def index(request):
    return render(request, 'home.html') 
# Add record
def add_record(request):
    if request.method == "POST":
        form = CredentialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record added successfully!")
            return redirect('displayrecords')
    else:
        form = CredentialForm()
    
    return render(request, "add.html", {"form": form})

# Display all records
def display_records(request):
    credentials = Credential.objects.all()
    return render(request, "display.html", {"credentials": credentials})
    

# Update a record
def update_record(request, id):
    credential = get_object_or_404(Credential, pk=id)
    if request.method == "POST":
        form = CredentialForm(request.POST, instance=credential)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect('displayrecords')
    else:
        form = CredentialForm(instance=credential)
    return render(request, "update.html", {"form": form})


def delete_record(request, id):
    credential = get_object_or_404(Credential, pk=id)
    credential.delete()
    messages.success(request, "Record deleted successfully!")
    return redirect('displayrecords')
