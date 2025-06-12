from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from .models import University, Department, Course, Paper, Comment, FavoritePaper, PaperReport
from .forms import CommentForm
from .forms import PaperUploadForm
from django.http import JsonResponse
from django.contrib import messages

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
        'current_category': 'all'
    })

def papers_by_category_view(request, department_id, course_id, category):
    department = get_object_or_404(Department, id=department_id)
    course = get_object_or_404(Course, id=course_id)
    papers = Paper.objects.filter(course=course, category=category)
    return render(request, 'papers.html', {
        'department': department,
        'course': course,
        'papers': papers,
        'current_category': category  # Optional: to highlight selected filter
    })

def paper_detail_view(request, department_id, course_id, paper_id):
    # Get the specific paper based on the paper_id
    paper = get_object_or_404(Paper, id=paper_id)
    is_favorite = FavoritePaper.objects.filter(user=request.user, paper=paper).exists()
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
        if 'favorite' in request.POST:
            if is_favorite:
                FavoritePaper.objects.filter(user=request.user, paper=paper).delete()
            else:
                FavoritePaper.objects.create(user=request.user, paper=paper)
        return redirect('paper_detail', department_id=department_id, course_id=course_id, paper_id=paper_id)
    else:
        form = CommentForm()
    comments = Comment.objects.filter(paper=paper)
    return render(request, 'paper_detail.html', {
        'department': department,
        'course': course,
        'paper': paper,
        'is_favorite': is_favorite,
        'form': form,
        'comments': comments,
        'file_url': paper.file.url
    })

@login_required
def toggle_favorite(request, paper_id):
    paper = Paper.objects.get(id=paper_id)
    user = request.user

    # Check if the paper is already favorited by the user
    favorite, created = FavoritePaper.objects.get_or_create(user=user, paper=paper)

    if not created:
        # If it's already a favorite, remove it
        favorite.delete()
        favorited = False
    else:
        # If it's not a favorite, add it
        favorited = True

    return JsonResponse({'favorited': favorited})

@login_required
def upload_paper_view(request):
    if request.method == 'POST':
        form = PaperUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Paper uploaded successfully.")
            return redirect('home')  # or anywhere else
    else:
        form = PaperUploadForm()
    return render(request, 'upload_paper.html', {'form': form})

# Report Parer View OLD VERSION!!!

#def report_paper(request, paper_id):
 #   paper = get_object_or_404(Paper, id=paper_id)

  #  if request.method == 'POST':
   #     reason = request.POST.get('reason')
    #    user = request.user if request.user.is_authenticated else None

     #   PaperReport.objects.create(paper=paper, user=user, reason=reason)

      #  return redirect(
       #     'paper_detail',
        #    department_id=paper.course.department.id,
         #   course_id=paper.course.id,
          #  paper_id=paper.id
        #)

# Report Paper View
def report_paper(request, paper_id):
    paper = get_object_or_404(Paper, id=paper_id)

    if request.method == 'POST':
        reason = request.POST.get('reason')
        user = request.user if request.user.is_authenticated else None

        PaperReport.objects.create(paper=paper, user=user, reason=reason)

        return redirect(
            'paper_detail',
            department_id=paper.course.department.id,
            course_id=paper.course.id,
            paper_id=paper.id
        )