from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from Employee.models import *

# Create your views here.
def home(request):
    emp = Employees.objects.order_by('id')
    paginator = Paginator(emp, 5)
    pag_num = request.GET.get('page', 1)
    emp_page = paginator.page(pag_num)
    total_entries = emp_page.paginator.count
    positions = Position.objects.all()

    context = {
        'emp': emp_page,
        'total_entries': total_entries,
        'positions': positions,
    }
    return render(request, 'index.html', context)


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        position_id = int(request.POST.get('position'))
        position = Position.objects.get(id=position_id)
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            name=name,
            email=email,
            position=position,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('home')

    positions = Position.objects.all()
    context = {
        'positions': positions
    }
    return render(request, 'index.html', context)



def update(request, id):
    emp = Employees.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        position_id = int(request.POST.get('position'))
        position = Position.objects.get(id=position_id)
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id=id,
            name=name,
            email=email,
            position=position,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('home')

    positions = Position.objects.all()
    context = {
        'emp': emp,
        'positions': positions
    }
    return render(request, 'index.html', context)



def edit(request, id):
    emp = Employees.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        position_id = int(request.POST.get('position'))
        position = Position.objects.get(id=position_id)
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id=id,
            name=name,
            email=email,
            position=position,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('home')

    positions = Position.objects.all()
    context = {
        'emp': emp,
        'positions': positions
    }
    return render(request, 'index.html', context)

def delete(request, id):
    emp = Employees.objects.filter(id = id)
    emp.delete()
    return redirect('home')