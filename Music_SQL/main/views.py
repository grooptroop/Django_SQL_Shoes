from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from reportlab.lib import colors

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


#chatgpt
from django.http import JsonResponse
from django.db import connection
from reportlab.platypus import TableStyle, Paragraph, Table, SimpleDocTemplate

from .forms import *
from .models import *



def SPosition(request):
    MPosition = Position.objects.all()
    return render(request, 'main/SPosition.html', {'MPosition': MPosition})
#
def SReceipt(request):
    MReceipt = Receipt.objects.all()
    context = {
        'delete_Receipt': request.user.has_perm('main.delete_Receipt'),
        'add_Receipt': request.user.has_perm('main.add_Receipt'),
        'change_Receipt': request.user.has_perm('main.Receipt'),
        'MReceipt': MReceipt}
    return render(request, 'main/SReceipt.html', context)

def SShoes(request):
    MShoes = Shoes.objects.all()
    context = {
        'delete_Shoes': request.user.has_perm('main.delete_Shoes'),
        'add_Shoes': request.user.has_perm('main.add_Shoes'),
        'change_Shoes': request.user.has_perm('main.Shoes'),
        'MShoes': MShoes}
    return render(request, 'main/SShoes.html', context)

def SStaff(request):
    MStaff = Staff.objects.all()
    context = {
               'delete_staff': request.user.has_perm('main.delete_staff'),
               'add_staff': request.user.has_perm('main.add_staff'),
               'change_staff': request.user.has_perm('main.change_staff'),
               'MStaff': MStaff}
    return render(request, 'main/SStaff.html', context)

def SShopper(request):
    MShopper = Shopper.objects.all()
    context = {
        'delete_Shopper': request.user.has_perm('main.delete_Shopper'),
        'add_Shopper': request.user.has_perm('main.add_Shopper'),
        'change_Shopper': request.user.has_perm('main.Shopper'),
        'MShopper': MShopper}
    return render(request, 'main/SShopper.html', context)

def SSickLeave(request):
    MSickLeave = SickLeave.objects.all()
    context = {
        'delete_SickLeave': request.user.has_perm('main.delete_WorkTime'),
        'add_SickLeave': request.user.has_perm('main.add_WorkTime'),
        'change_SickLeave': request.user.has_perm('main.WorkTime'),
        'MSickLeave': MSickLeave}
    return render(request, 'main/SSickLeave.html', context)



def SVacation(request):
    MVacation = Vacation.objects.all()
    context = {
        'delete_Vacation': request.user.has_perm('main.delete_WorkTime'),
        'add_Vacation': request.user.has_perm('main.add_WorkTime'),
        'change_Vacation': request.user.has_perm('main.WorkTime'),
        'MVacation': MVacation}
    return render(request, 'main/SVacation.html', context)

def SWorkTime(request):
    MWorkTime = WorkTime.objects.all()
    context = {
        'delete_WorkTime': request.user.has_perm('main.delete_WorkTime'),
        'add_WorkTime': request.user.has_perm('main.add_WorkTime'),
        'change_WorkTime': request.user.has_perm('main.WorkTime'),
        'MWorkTime': MWorkTime}


def index(request):
    #return redirect('/login')
    return render(request, 'main/index.html')

#chatgpt

def document(request):
    return render(request, 'main/Document.html')

def get_tables(request):
    # Получение всех таблиц в базе данных PostgreSQL
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT table_name FROM information_schema.tables "
            "WHERE table_schema = 'public'"
        )
        tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    return JsonResponse(table_names, safe=False)


def get_table_data(request, table_name):
    # Получение данных из конкретной таблицы


    with connection.cursor() as cursor:
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()
        column_names = [col[0] for col in cursor.description]

    data = [dict(zip(column_names, row)) for row in rows]
    return JsonResponse(data, safe=False)

def run_query(request, query_id):
    # if not request.user.groups.filter(name='Администраторы').exists():
    #     return JsonResponse({'error': 'Access Denied'}, status=403)

    predefined_queries = {
        1: "SELECT * FROM shoes WHERE name like 'Tyrex'",
        2: "SELECT * FROM shoes WHERE size = '42'",
        3: "SELECT * FROM shopper WHERE address LIKE '%Г.Москва%';",
        4: "SELECT first_name, middle_name, last_name, telephone_staff FROM staff"
           " INNER JOIN Work_time ON staff.ID_staff = Work_time.staff_ID "
           "WHERE day_work = '30' AND month_work = '10' AND year_work = '2023';",
        5: "SELECT first_name, titels FROM type_vacation "
           "INNER JOIN vacation ON type_vacation.ID_type = vacation.type_ID "
           "INNER JOIN staff ON vacation.staff_ID = staff.ID_staff;",
        6: "select sh.name from shoes as sh "
           "inner join receipt_position as rp on rp.shoes_ID = sh.ID_shoes "
           "inner join receipt as r on r.recepit_ID = rp.ID_receipt "
           "inner join shopper as s on s.ID_client=r.client_ID "
           "WHERE first_name = 'Жукова' AND middle_name = 'Эмилия' AND last_name = 'Матвеевна';",
        7: "SELECT brand_name, name, ID_position, recepit_ID, first_name FROM brand "
           "INNER JOIN shoes ON brand.ID_brand = shoes.brand_ID "
           "INNER JOIN receipt_position ON shoes.ID_shoes = receipt_position.shoes_ID "
           "INNER JOIN receipt ON receipt_position.ID_receipt = receipt.recepit_ID  "
           "INNER JOIN shopper ON receipt.client_ID = shopper.ID_client;",
        # Добавьте другие запросы
    }

    query = predefined_queries.get(query_id)
    if not query:
        return JsonResponse({'error': 'Invalid query ID'}, status=404)

    with connection.cursor() as cursor:
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    data = [dict(zip(column_names, row)) for row in rows]
    return JsonResponse(data, safe=False)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/SStaff')
        else:
            messages.error(request, 'Логин у тебя плохой')
    return render(request, 'main/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'Ты разлогинен')
    return redirect('/')


@permission_required('main.add_Receipt', raise_exception=True)
def AddReceipt(request):
    error = ''
    if request.method == 'POST':
        form = AddReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SReceipt')
        else:
            error = 'Неправильное заполнение формы'
    form = AddReceiptForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/AddReceipt.html', data)



@permission_required('main.add_staff', raise_exception=True)
def AddStaff(request):
    error = ''
    if request.method == 'POST':
        form = AddStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SStaff')
        else:
            error = 'Неправильное заполнение формы'
    form = AddStaffForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/AddStaff.html', data)

@permission_required('main.add_WorkTime', raise_exception=True)
def AddWorkTime(request):
    error = ''
    if request.method == 'POST':
        form = AddWorkTimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SWorkTime')
        else:
            error = 'Неправильное заполнение формы'
    form = AddWorkTimeForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/AddWorkTime.html', data)

@permission_required('main.add_Vacation', raise_exception=True)
def AddVacation(request):
    error = ''
    if request.method == 'POST':
        form = AddVacationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SVacation')
        else:
            error = 'Неправильное заполнение формы'
    form = AddVacationForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/AddVacation.html', data)

@permission_required('main.add_SickLeave', raise_exception=True)
def AddSickLeave(request):
    error = ''
    if request.method == 'POST':
        form = AddSickLeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SSickLeave')
        else:
            error = 'Неправильное заполнение формы'
    form = AddSickLeaveForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/AddSickLeave.html', data)

@permission_required('main.add_Shopper', raise_exception=True)
def AddShopper(request):
    error = ''
    if request.method == 'POST':
        form = AddShopperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SShopper')
        else:
            error = 'Неправильное заполнение формы'
    form = AddShopperForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/AddShopper.html', data)

@permission_required('main.add_Shoes', raise_exception=True)
def AddShoes(request):
    error = ''
    if request.method == 'POST':
        form = AddShoesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SShoes')
        else:
            error = 'Неправильное заполнение формы'
    form = AddShoesForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/AddShoes.html', data)

@permission_required('main.add_Position', raise_exception=True)
def AddPosition(request):
    error = ''
    if request.method == 'POST':
        form = AddPositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Position')
        else:
            error = 'Неправильное заполнение формы'
    form = AddPositionForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/AddPosition.html', data)

@permission_required('main.change_Shopper', raise_exception=True)
def edit_Shopper(request, id_client):
    member = get_object_or_404(Shopper, id_client=id_client)
    if request.method == "POST":
        form = UpdateShopperForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('SShopper')
    else:
        form = UpdateShopperForm(instance=member)
    return render(request, 'main/AddShopper.html', {'form': form})


@permission_required('main.change_SickLeave', raise_exception=True)
def edit_SickLeave(request, id_leave):
    member = get_object_or_404(SickLeave, id_leave=id_leave)
    if request.method == "POST":
        form = UpdateSickLeaveForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('SSickLeave')
    else:
        form = UpdateSickLeaveForm(instance=member)
    return render(request, 'main/AddSickLeave.html', {'form': form})

@permission_required('main.change_Vacation', raise_exception=True)
def edit_Vacation(request, id_vacation):
    member = get_object_or_404(Vacation, id_vacation=id_vacation)
    if request.method == "POST":
        form = UpdateVacationForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('SVacation')
    else:
        form = UpdateVacationForm(instance=member)
    return render(request, 'main/AddVacation.html', {'form': form})

@permission_required('main.change_WorkTime', raise_exception=True)
def edit_WorkTime(request, id_work_time):
    member = get_object_or_404(WorkTime, id_work_time =id_work_time)
    if request.method == "POST":
        form = UpdateWorkTimeForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('SWorkTime')
    else:
        form = UpdateWorkTimeForm(instance=member)
    return render(request, 'main/AddWorkTime.html', {'form': form})

@permission_required('main.delete_WorkTime', raise_exception=True)
def Delete_WorkTime(request, id_work_time):
    member = get_object_or_404(WorkTime, id_work_time=id_work_time)
    if request.method == "POST":
        form = UpdateWorkTimeForm(request.POST, instance=member)
        WorkTime.objects.filter(id_work_time = id_work_time).delete()
        return redirect('SWorkTime')
    else:
        form = UpdateStaffForm(instance=member)
    return render(request, 'main/DeleteWorkTime.html', {'form': form})


@permission_required('main.delete_Shopper', raise_exception=True)
def Delete_Shopper(request, id_client):
    member = get_object_or_404(Shopper, id_client=id_client)
    if request.method == "POST":
        form = UpdateShopperForm(request.POST, instance=member)
        Shopper.objects.filter(id_client = id_client).delete()
        return redirect('SWorkTime')
    else:
        form = UpdateShopperForm(instance=member)
    return render(request, 'main/DeleteShopper.html', {'form': form})





@permission_required('main.change_staff', raise_exception=True)
def edit_staff(request, id_staff):
    member = get_object_or_404(Staff, id_staff=id_staff)
    if request.method == "POST":
        form = UpdateStaffForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('SStaff')
    else:
        form = UpdateStaffForm(instance=member)
    return render(request, 'main/AddStaff.html', {'form': form})

@permission_required('main.change_Shoes', raise_exception=True)
def edit_Shoes(request, id_shoes):
    member = get_object_or_404(Shoes, id_shoes=id_shoes)
    if request.method == "POST":
        form = UpdateShoesForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('SShoes')
    else:
        form = UpdateShoesForm(instance=member)
    return render(request, 'main/AddShoes.html', {'form': form})

@permission_required('main.delete_Shoes', raise_exception=True)
def Delete_Shoes(request, id_shoes):
    member = get_object_or_404(Shoes, id_shoes=id_shoes)
    if request.method == "POST":
        form = UpdateShoesForm(request.POST, instance=member)
        Shoes.objects.filter(id_shoes = id_shoes).delete()
        return redirect('SShoes')
    else:
        form = UpdateShoesForm(instance=member)
    return render(request, 'main/DeleteShoes.html', {'form': form})


@permission_required('main.delete_staff', raise_exception=True)
def Delete_Staff(request, id_staff):
    member = get_object_or_404(Staff, id_staff=id_staff)
    if request.method == "POST":
        form = UpdateStaffForm(request.POST, instance=member)
        Staff.objects.filter(id_staff = id_staff).delete()
        return redirect('SStaff')
    else:
        form = UpdateStaffForm(instance=member)
    return render(request, 'main/DeleteStaff.html', {'form': form})
def test(request):
    return render(request, 'main/test.html')

def quarterly_revenue(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="REVENUE_REPORT.pdf"'

    people = Receipt.objects.raw("SELECT id_number, final_price FROM receipt")
    final_price = 0
    for person in people:
        final_price = person.final_price + final_price
    s = str(final_price)
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    w, h = A4
    p.line(20, h-30, 20 + 530, h-30)
    p.drawString(50, h - 50, "REVENUE REPORT")
    p.drawString(50, h - 110, "For the quarter, the store's profit was about:")
    p.drawString(300, h - 110, s + '   RUB')
    p.drawString(245, h - 160, 'Wallker Company ')
    p.line(20, h - 190, 20 + 530, h - 190)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


def new_shoes(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="NEW_SHOES.pdf"'

    people = Shoes.objects.raw("SELECT id_shoes, name, price, cost_of_production FROM shoes WHERE id_shoes IN (SELECT MAX(id_shoes) FROM shoes)")
    for person in people:
        name = str(person.name)
        price = str(person.price)
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    w, h = A4
    p.line(20, h - 30, 20 + 530, h - 30)
    p.drawString(30, h - 50, "HI!")
    p.drawString(30, h - 90, "Dear customer, we would like to notify you of a new pair of shoes called  " + name)
    p.drawString(30, h - 110, 'it will be priced at  ' + price + '000  RUB')
    p.drawString(30, h - 140, 'It will be available in the store soon, but now you can order it by sending us an e-mail')
    p.drawString(30, h - 170, 'Wallker@gmail.com')
    p.drawString(235, h - 190, 'Sincerely Wallker Group ')
    p.line(20, h - 220, 20 + 530, h - 220)
    #Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def shoe_order(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="REVENUE_REPORT.pdf"'
    p = canvas.Canvas(response)
    people = Shoes.objects.raw("SELECT id_shoes, name, size, cost_of_production FROM shoes WHERE remaining < 5 ")
    w, h = A4
    y = 70
    p.line(20, h - 30, 20 + 530, h - 30)
    p.drawString(50, h - 50, "Shoes to be procured:")
    for person in people:
        p.drawString(50, h - y, str(person.name) +'       '+ str(person.size) + 'Size    '+ str(person.cost_of_production)+'000 RUB ')
        y = y+20
    p.line(20, h - y, 20 + 530, h - y)
    p.showPage()
    p.save()
    return response


