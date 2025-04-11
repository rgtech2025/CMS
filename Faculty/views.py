from django.shortcuts import render, redirect

# Create your views here.
from .models import Register
from Student.models import Register as StudentRegister

def faculty_reg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        mno = request.POST.get('mobile')
        addr = request.POST.get('addr')
        
        # Create a new Register object and save it to the database
        register = Register(name=name, email=email, psw=psw, mno=mno, addr=addr)
        register.save()
        
        return render(request,'faculty_login.html',{'msg':'Registration Successful'})
    return render(request,'faculty_reg.html')

def faculty_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        data = Register.objects.get(email=email,psw=psw)
        request.session['uid']=data.email
        
        # Check if the user exists in the database
        try:
            register = Register.objects.get(email=email, psw=psw)
            return redirect(faculty_home) #it is used for redirecting to another page based on the lozical execution
        except Register.DoesNotExist:
            return render(request,'faculty_login.html',{'msg':'Invalid Credentials'})
    return render(request,'faculty_login.html')

def faculty_home(request):
    # This view can be used to display faculty-specific information or dashboard
    email = request.session['uid']
    print(email)
    data = Register.objects.get(email=email)
    print(data.email)

    return render(request,'faculty_home.html',{'id':data})

def attendance(request):
    # Logic for attendance view
    students = StudentRegister.objects.all() # Fetch all students from the database
    
    if request.method == 'POST':
        # Handle attendance submission logic here
        attendance_data = request.POST.getlist('attendance')
        for student_id in attendance_data:
            # Process each student's attendance
            pass  # Replace with actual logic
    return render(request,'attendance.html')

def marks(request):
    # Logic for marks view
    return render(request,'marks.html')

def feedback(request):
    # Logic for feedback view
    return render(request,'feedback.html')

def logout(request):
    # Clear the session and redirect to login page
    request.session.flush() # it is used to clear the session 
    return redirect(faculty_login)