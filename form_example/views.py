from django.shortcuts import render
from form_example.forms import UserForm

def user_form(request):

    user = UserForm()
    #http: // localhost:8000 / user_form?name = anu & email = slanuradha888 @ gmail.com
    print(request.GET)

    if request.method == 'POST':
        user = UserForm(request.POST)

        if user.is_valid():
            pass
    return render(request, 'user_form.html', {'form': user})

def static_example(request):
    return render(request, 'static_example.html')