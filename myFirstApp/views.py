from django.shortcuts import render 
from django.http import HttpResponse,HttpResponseNotFound 
from django.template import loader 
from myFirstApp.models import User 
from django.core.exceptions import ObjectDoesNotExist

def index(request): 
    if request.method == 'POST':
        newUser = User(first_name = request.POST['first_name'])
        newUser.last_name = request.POST['last_name']
        newUser.contact = request.POST['contact']
        newUser.email = request.POST['email']
        newUser.age = request.POST['age']
        newUser.save()        
    
    
    try:
        #user = User.objects(first_name = 'Tony').get() # Get single user from DB    
        params = {'user': User.objects} # Get all users from DB                       
    except ObjectDoesNotExist:
        print('user does not exist')        

    template = loader.get_template('index.html')     
    return HttpResponse(template.render(params))
    

def update(request):  
    id = eval("request." + request.method + "['id']")
    user = User.objects(id = id).get()

    if request.method == 'POST':        
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.contact = request.POST['contact']
        user.email = request.POST['email']
        user.age = request.POST['age']
        user.save()

        template_name = 'index.html'
        params = {'user': User.objects}

    elif request.method == 'GET':         
        try:         
            params = {'user':user} 
            template_name = 'update.html'          
        except ObjectDoesNotExist:
            print('user does not exist') 
        
    template = loader.get_template(template_name)     
    return HttpResponse(template.render(params))   
     

def delete(request):     
    id = eval("request." + request.method + "['id']")    
    user = User.objects(id = id).get()    
    if request.method == 'POST':                      
        user.delete() 
        template_name = 'index.html'
        params = {'user': User.objects} 

    elif request.method == 'GET':
        template_name = 'delete.html'
        params = { 'id': id } 

    template = loader.get_template(template_name)     
    return HttpResponse(template.render(params))


     