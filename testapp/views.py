from django.shortcuts import render

def hello(request):

    d1={
        'name':'anu',
        'email':'anu2gmail.com',
        'l1':[1,2,3,4,5,'Sri'],
        'd2':{'city': 'Bangalore','address':'Btm'}
    }
    return render(request, 'hello.html', d1)

def hellopython(request):
    return render(request, 'hello_python.html')

def djangoclass(request):
    return render(request, 'djangoclass.html')


