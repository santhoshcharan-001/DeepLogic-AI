from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pdf
from django.http import JsonResponse
from .utils import extract_text

# Create your views here.
def home(request):
    return render(request, "home.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")
    return render(request, "login.html")


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password == password2:
            user = User.objects.create_user(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Account created successfully")
                return redirect("home")
            else:
                messages.error(request, "Error creating account")
                return redirect("signup")
        else:
            messages.error(request, "Passwords do not match")
            return redirect("signup")
    return render(request, "signup.html")


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required(login_url="login")
def pdfs_list(request):
    pdfs = Pdf.objects.filter(user=request.user)
    return render(request, "pdfs_list.html", {"pdfs": pdfs})


@login_required(login_url="login")
def pdf_detail(request, pk):
    pdf = Pdf.objects.get(pk=pk)
    if request.user != pdf.user:
        messages.error(request, "You do not have permission to view this pdf")
        return redirect("home")
    return render(request, "pdf_detail.html", {"pdf": pdf})


@login_required(login_url="login")
def pdf_upload(request):
    if request.method == "POST":
        pdf = request.FILES["pdf"]
        pdf_obj = Pdf.objects.create(user=request.user, pdf=pdf)
        text = extract_text(pdf_obj.pdf.path)
        pdf_obj.text = text
        pdf_obj.save()
        return JsonResponse(
            {"success": True, "redirect_url": pdf_obj.get_absolute_url()}
        )
    return render(request, "pdf_upload.html")
