from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from .models import University, Department, Course, Paper, Comment
from .forms import CommentForm

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = '/login'

# Hello View
#def hello_view(request):
    #return HttpResponse("Hello, welcome to UniTryhards!")

# Sign Up View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user without authentication
            login(request, user)  # Log the user in directly after creation
            return redirect('home')  # Redirect to the 'home' page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log in the user after successful authentication
            return redirect('home')  # Redirect to the 'home' page after successful login
        else:
            return HttpResponse("Invalid login credentials")  # Display error message for invalid login
    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the 'hello' page after logging out

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required  # Εξασφαλίζει ότι μόνο συνδεδεμένοι χρήστες έχουν πρόσβαση
def home(request):
    return render(request, 'home.html')  # Επιστρέφει το home.html template

# View for selecting university
def university_view(request):
    universities = University.objects.all()  # Fetch all universities from the database
    if request.method == 'POST':
        university_id = request.POST['university']
        return redirect('department', university_id=university_id)  # Redirect to department page
    
    return render(request, 'university.html', {'universities': universities})

# View for selecting department
def department_view(request, university_id):
    university = University.objects.get(id=university_id)
    departments = university.departments.all()  # Get all departments for the selected university
    
    if request.method == 'POST':
        department_id = request.POST['department']
        return redirect('course_selection', university_id=university.id, department_id=department_id)  # Redirect to course selection page
    
    return render(request, 'department.html', {'university': university, 'departments': departments})

def course_selection_view(request, university_id, department_id):
    university = University.objects.get(id=university_id)
    department = Department.objects.get(id=department_id)
    courses = Course.objects.filter(department=department)  # Assuming you have a 'Course' model linked to the department
    if request.method == "POST":
        selected_course_id = request.POST.get('course')  # Get the selected course ID
        return redirect('papers', department_id=department_id, course_id=selected_course_id)  # Redirect to the papers page
    return render(request, 'course_selection.html', {
        'university': university,
        'department': department,
        'courses': courses
    })

def papers_view(request, department_id, course_id):
    from .models import Paper
    department = Department.objects.get(id=department_id)
    course = Course.objects.get(id=course_id)
    papers = Paper.objects.filter(course=course)  # You can filter papers by course
    return render(request, 'papers.html', {
        'department': department,
        'course': course,
        'papers': papers,
    })


def paper_detail_view(request, department_id, course_id, paper_id):
    # Get the specific paper based on the paper_id
    paper = get_object_or_404(Paper, id=paper_id)
    # Get department and course based on the passed ids
    department = Department.objects.get(id=department_id)
    course = Course.objects.get(id=course_id)
    # Handle comment form submission
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.paper = paper  # Associate the comment with the paper
            new_comment.user = request.user  # Associate the comment with the current user
            new_comment.save()
            return redirect('paper_detail', department_id=department_id, course_id=course_id, paper_id=paper_id)
    else:
        form = CommentForm()
    comments = Comment.objects.filter(paper=paper)
    return render(request, 'paper_detail.html', {
        'department': department,
        'course': course,
        'paper': paper,
        'form': form,
        'comments': comments,
        'file_url': paper.file.url
    })