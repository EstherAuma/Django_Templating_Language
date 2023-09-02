from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse, HttpResponseRedirect

#Create your views here.

# def index(request):
#     #how a variable is passed from the view to the template
#     title = 'Django Templating Language'
#     author = 'Esther'
#     year_of_birth = 2002
#     current_year = 2023
#     age = current_year - year_of_birth

#     return render(request,'index.html',{'title':title, 'author':author, 'age':age ,'current_year':current_year})



def index(request):
    #how a variable is passed from the view to the template
    if request.method == 'POST':
        continent = request.POST['continent']
        return render(request,'index.html',{'continent':continent})
    else:
        return render(request,'index.html')
    # title = 'Django Templating Language'
    # author = 'Esther'
    # year_of_birth = 2002
    # current_year = 2023
    # African = 'African'
    # # Asian ='Asian'
    # # contex = [title, year_of_birth,author,current_year]
    # return render(request,'index.html')

def data_collection(request):
    if request.method == 'POST':
        name = request.POST['username']
        age = request.POST['age']
        phone = request.POST['phone']
        context = [name, age, phone]
        print(context)
        return render(request,'loop.html',{'contex':context})
    else:
        return render(request,'data_collection.html')


