from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView

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

universities = [
    "Εθνικό και Καποδιστριακό Πανεπιστήμιο Αθηνών",
    "Εθνικό Μετσόβιο Πολυτεχνείο",   
    "Οικονομικό Πανεπιστήμιο Αθηνών",
    "Γεωπονικό Πανεπιστήμιο Αθηνών",
    "Πάντειο Πανεπιστήμιο",
    "Πανεπιστήμιο Δυτικής Αττικής",
    "Χαροκόπειο Πανεπιστήμιο",
    "Πανεπιστήμιο Πειραιώς",
    "Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης",
    "Πανεπιστήμιο Μακεδονίας",
    "Πανεπιστήμιο Δυτικής Μακεδονίας",
    "Διεθνές Πανεπιστήμιο της Ελλάδος",
    "Δημοκρίτειο Πανεπιστήμιο Θράκης",
    "Πανεπιστήμιο Ιωαννίνων",
    "Πανεπιστήμιο Θεσσαλίας",
    "Πανεπιστήμιο Πελοποννήσου",
    "Πανεπιστήμιο Πατρών",
    "Πανεπιστήμιο Αιγαίου",
    "Ιόνιο Πανεπιστήμιο",
    "Πανεπιστήμιο Κρήτης",
    "Πολυτεχνείο Κρήτης",
    "Ελληνικό Μεσογειακό Πανεπιστήμιο",
    "Ελληνικό Ανοικτό Πανεπιστήμιο",
    "Ανώτατη Σχολή Καλών Τεχνών",
    "Ανώτατη Σχολή Παιδαγωγικής και Τεχνολογικής Εκπαίδευσης",
    "Ανώτατη Σχολή Τουριστικής Εκπαίδευσης",
    "Ανώτατη Εκκλησιαστική Ακαδημία Αθήνας",
    "Ανώτατη Εκκλησιαστική Ακαδημία Βελλάς Ιωαννίνων",
    "Ανώτατη Εκκλησιαστική Ακαδημία Θεσσαλονίκης",
    "Πατριαρχική Ανώτατη Εκκλησιαστική Ακαδημία Κρήτης",
    "Ακαδημία Εμπορικού Ναυτικού Μακεδονίας",
    "Μεσογειακό Αγρονομικό Ινστιτούτο Χανίων",
    "Στρατιωτική Σχολή Ευελπίδων",
    "Σχολή Ικάρων",
    "Σχολή Ναυτικών Δοκίμων"
]

# View for selecting University
def university_view(request):
    context = {'universities': universities}
    if request.method == 'POST':
        # Get the selected university from the form
        university = request.POST.get('university')
        # Redirect to the department selection page with the university selected
        return redirect('pick_department', university=university)
    return render(request, 'university.html', context)

# View for selecting Department based on the selected University
def pick_department_view(request, university):
    if request.method == 'POST':
        # Get the selected department
        department = request.POST.get('department')
        # Redirect to the papers selection page with the selected department
        return redirect('papers')
    return render(request, 'department.html', {'university': university})

def papers(request):
    return render(request, 'papers.html')