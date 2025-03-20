from django.shortcuts import render, redirect

from .models import Employees

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


# Create your views here.
def home(request):
    emp = Employees.objects.all()
    emp_count = Employees.objects.count()
    return render(request, "index.html", {"emp": emp, "emp_count": emp_count})


def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        salary = request.POST.get("salary")
        designation = request.POST.get("designation")
        short_description = request.POST.get("short_description")

        emp = Employees(
            
            name=name,
            email=email,
            address=address,
            phone=phone,
            salary=salary,
            designation=designation,
            short_description=short_description,
            
        )
        emp.save()
        messages.success(request, f"Employee {emp.name} has been added successfully.")
        return redirect("home")
    return render(request, "index.html")


def edit(request, id):
    emp = get_object_or_404(Employees, id=id) 

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        salary = request.POST.get("salary")
        designation = request.POST.get("designation")
        short_description = request.POST.get("short_description")

        # Update fields except for `join_date`
        emp.name = name
        emp.email = email
        emp.address = address
        emp.phone = phone
        emp.salary = salary
        emp.designation = designation
        emp.short_description = short_description

        emp.save()

        messages.success(request, f"Employee {emp.name} has been updated successfully.")
        return redirect("home")

    return render(request, "index.html", {"emp": emp})


def delete(request, id):
    emp = get_object_or_404(Employees, id=id)
    emp.delete()
    messages.success(request, f"Employee {emp.name} has been deleted successfully.")
    return redirect("home")


def search(request):
    query = request.GET.get("query", "")
    if query:
        emp = Employees.objects.filter(name__icontains=query)
        count = emp.count()
    else:
        return redirect("/")

    return render(request, "index.html", {"emp": emp, "count": count})
