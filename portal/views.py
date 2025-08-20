from django.shortcuts import render, redirect , get_object_or_404
from .models import Teacher, Student , Audit_Log
from .forms import LoginForm, StudentForm, RegisterForm
from .utils import verify_password, hash_password, create_session, delete_session, get_session_user
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def calculate_new_marks(old_marks , new_marks):
    return int(old_marks) + int(new_marks)

def login_req(func):
    def wrapper(request, *args, **kwargs):
        token = request.COOKIES.get("session_token")
        if not token or not get_session_user(token):
            return redirect("login")
        return func(request, *args, **kwargs)
    return wrapper


def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        try:
            teacher = Teacher.objects.get(username=username)
            if verify_password(teacher.password, teacher.salt, password):
                token = create_session(teacher.id)
                response = redirect("home")
                response.set_cookie(
                    "session_token",
                    token,
                    max_age=3600,
                    httponly=True,
                    samesite="Strict"
                )
                return response
            else:
                messages.error(request, "Login and password mismatch")
        except Teacher.DoesNotExist:
            messages.error(request, "Login and password mismatch")

    return render(request, "login.html", {"form": form})


def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data["name"]
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        password, salt  = hash_password(password)
        new_teacher = Teacher(
            name=name,
            username=username,
            password=password,
            salt=salt
        )
        new_teacher.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect("login")

    return render(request, "register.html", {"form": form})

@login_req
def homeview(request):
    data = Student.objects.all()
    
    return render(request, "dashboard.html" ,{'data' : data})


def add_student_view(request):
    
    form= StudentForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        
        data = form.cleaned_data
        name = data['name'].lower()
        subject = data['subject'].lower()
        marks = data['marks']
        
        try:
            student = Student.objects.get(name = name , subject = subject)
            old_marks = student.marks
            new_marks = calculate_new_marks(old_marks= old_marks , new_marks=marks)
            
            student.marks = new_marks
            student.save()
            audit = Audit_Log(student = student , subject = data['subject'].lower() , old_marks =old_marks , new_marks = new_marks )
            audit.save()
            messages.success(request , "Student Updated succesfully ")
            return redirect('home')
        
        except ValueError : 
            messages.error(request , "marks are exceeding 100")
            return redirect('edit_student' ,stu_id = student.id)

        except ObjectDoesNotExist:

            new_student = Student(name = name , subject = subject , marks = marks)
            new_student.save()
            messages.success(request , "Student added succesfully ")
            return redirect('home')
       
    return render(request , 'add_student.html' , {'form' : form})

@login_req
def edit_student_view(request , stu_id):
       
    student_to_update = get_object_or_404(Student , id = stu_id)
    old_marks = student_to_update.marks
    if request.method == 'GET':
        form = StudentForm(initial={
            'name' : student_to_update.name,
            'subject' : student_to_update.subject,
            'marks' : old_marks,
        })

    else:
        form= StudentForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        student_to_update.name = data['name'].lower()
        student_to_update.subject = data['subject'].lower()
        student_to_update.marks = data['marks']
        student_to_update.save()

        # saving audit in database
        audit = Audit_Log(student = student_to_update , subject = data['subject'].lower() , old_marks =old_marks , new_marks = data['marks'] )
        audit.save()

        messages.success(request , 'Student Updated Successfully')
        return redirect('home')
        

    

    return  render(request , 'add_student.html' , {'form' : form})

@login_req
def del_student_view(request , stu_id):
    
    student_to_delete = get_object_or_404(Student , id = stu_id)
    student_to_delete.delete()

    return redirect('home')
