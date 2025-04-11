from django.shortcuts import render ,redirect

# Create your views here.
from .models import Register

def index(request):
    return render(request,'index.html')

def std_reg(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        mno = request.POST.get('mno')
        addr = request.POST.get('addr')

        try:
            if name!='':
                data = Register.objects.create(    #Inserting the data into table
                name = name,
                email = email,
                psw = psw,
                mno = mno,
                addr = addr
                )
                data.save() #Commit the transaction
                print(data)
                print("Data inserted into table")
            else:
        # if data>0:
                print("Data Not inserted into table")
            return redirect(std_login)
        except Exception as e:
            print("Exception is :",e)
            print("Please fill the data:")

    return render(request,'std_reg.html')# This is called default Responce 

def std_login(request):
    if request.method =='POST':
        email = request.POST.get('email')
        psw   = request.POST.get('psw')
        try:
            data = Register.objects.get(email=email,psw=psw)
            request.session['uid']=data.email
            if data.email==email:
                return redirect(std_home)
            else:
                return redirect(std_login)
        except Exception as e:
            print("Exception is :",e)
            print("Wrong Credentials Please try again:")
            return redirect(std_login)
            
    return render(request,'std_login.html')

def std_home(request):
    email = request.session['uid']
    data = Register.objects.get(email=email)
    
    return render(request,'std_home.html',{'id':data})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')