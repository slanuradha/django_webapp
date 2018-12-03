from django.shortcuts import render, redirect
from crud.forms import CollageForm
from form_example.models import Collage
from django.db.transaction import connections
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def create(request):
    form = CollageForm()

    if request.method == 'POST':
        form = CollageForm(request.POST)
        if form.is_valid():
            #form.save()
            collage = Collage()
            collage.name = form.cleaned_data['email'].split('@')[0]
            collage.email = form.cleaned_data['email']
            collage.address = form.cleaned_data['address']
            collage.city = form.cleaned_data['city']
            collage.save()
            return redirect(index)

    return render(
        request,
        'temp/create.html',
        {'form':form}
    )


def index(request):
    data = Collage.objects.all()
    #data = Collage.objects.raw("select * from collage")
    #select * from Collage
    return render(request,'temp/index.html', {'data': data})


def update(request):
    id = request.GET['id']
    data =Collage.objects.get(id=id)
    form = CollageForm(instance=data)
    if request.method == 'POST':
        form = CollageForm(request.POST, instance=data)
        if form.is_valid():
            #form.save()
            collage = Collage()
            collage.id = id
            collage.name = form.cleaned_data['email'].split('@')[0]
            collage.email = form.cleaned_data['email']
            collage.address = form.cleaned_data['address']
            collage.city = form.cleaned_data['city']
            collage.save()
            return redirect(index)

    return render(
        request,
        'temp/update.html',
        {'form': form}
    )

def view(request):
    id = request.GET['id']
    data = Collage.objects.get(id = id)
    return render(request, 'temp/view.html', {'data': data})

def delete(request):
    id = request.GET['id']
    data = Collage.objects.get(id = id)
    data.delete()
    return redirect(index)

