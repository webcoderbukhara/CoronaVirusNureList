from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Person, Vacsina
import datetime


# Create your views here.
@login_required
def home(request):
    persons = Person.objects.filter(doctor=request.user).order_by('-date')
    vac = "Xitoy"
    user = request.user
    serti = False
    if request.method == 'POST':
        id1=(request.POST.get('step1'))
        id2=(request.POST.get('step2'))
        id3=(request.POST.get('step3'))
        search = request.POST.get('search')
       
        if id1 != None:
             person = Person.objects.filter(id=int(id1))[0]
             person.step1 = True
             person.save()
        
        if id2 != None:
             person = Person.objects.filter(id=int(id2))[0]
             person.step2 = True
             person.save()
             if person.vacsina != vac:
                 serti = True
        if id3 != None:
             person = Person.objects.filter(id=int(id3))[0]
             person.step3 = True
             serti = True
             person.save()
        
        if search != None and search != '':
            
            persons = persons.filter(first_name=search).order_by('-date')
            
      
       
   
    return render(request, 'home.html',{'persons':persons, 'user':user, 'vac':vac, 'serti': serti})


@login_required
def createPerson(request):
    vacsina = Vacsina.objects.all()
    


    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        img = request.FILES.get('img')
        vac_id = request.POST.get('vac_id')
        vacsin = Vacsina.objects.filter(id=vac_id)[0]

        person = Person(first_name=first_name,
                        last_name=last_name,
                        age=age,
                        address=address,
                        phone=phone,
                        img=img,
                        doctor=request.user,
                        vacsina=vacsin)
        person.save()

        return redirect('home')
        
    return render(request, 'create.html',{'vacsina':vacsina})


@login_required
def editPerson(request,id):
    vacsina = Vacsina.objects.all()
    person = Person.objects.filter(id=id)[0]

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        img = request.FILES.get('img')
        vac_id = request.POST.get('vac_id')
        step1 = request.POST.get('step1',False)
        step2 = request.POST.get('step2',False)
        step3 = request.POST.get('step3',False)

        vacsin = Vacsina.objects.filter(id=vac_id)[0]

        person.first_name=first_name
        person.last_name=last_name
        person.age=age
        person.address=address
        person.phone=phone
        if img != None:
            person.img=img
        person.doctor=request.user
        person.vacsina=vacsin
       

        if vacsin.name == 'Xitoy':
            person.step1 = step1
            person.step2 = step2
            person.step3 = step3
        else:
            person.step1 = step1
            person.step2 = step2





        person.save()
        return redirect('home')

    return render(request, 'edit.html',{'person':person,'vacsina':vacsina})

@login_required
def detail(request,id):
    person = Person.objects.filter(id=id)[0]



    return render(request, 'detail.html',{'person':person})

@login_required
def sertificat(request,id):
    person = Person.objects.filter(id=id)[0]
    date = datetime.datetime.now()



    return render(request, 'sertificat.html',{'person':person,'date':date})
