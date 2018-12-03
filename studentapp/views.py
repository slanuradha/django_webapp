from django.shortcuts import render

def student(request):
    return render(request, 'student.html')

def attendence(request):
    return render(request, 'attendence.html')