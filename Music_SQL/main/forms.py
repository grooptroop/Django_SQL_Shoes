from django import forms
from django.forms import TextInput

from .models import *


class AddStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('first_name', 'middle_name','last_name','position','birthday','telephone_staff')

        widgets = {
            'first_name': TextInput(attrs={ 'placeholder': "Имя"}),
            'middle_name': TextInput(attrs={'placeholder': "Фамилия"}),
            'last_name': TextInput(attrs={'placeholder': "Отчество"}),
            'birthday': TextInput(attrs={'placeholder': "День рождения"}),
            'telephone_staff': TextInput(attrs={'placeholder': "телефон"}),


        }

class AddWorkTimeForm(forms.ModelForm):
    class Meta:
        model = WorkTime
        fields = ('staff', 'position','day_work','month_work','year_work','monthly_salary')

        widgets = {
            'day_work': TextInput(attrs={ 'placeholder': "День работы"}),
            'month_work': TextInput(attrs={'placeholder': "Месяц работы"}),
            'year_work': TextInput(attrs={'placeholder': "Год работы"}),
            'monthly_salary': TextInput(attrs={'placeholder': "Месячный оклад"}),


        }

class AddVacationForm(forms.ModelForm):
    class Meta:
        model = Vacation
        fields = ('staff', 'starting_date','number_of_days','type','actual_start','actual_end')

        widgets = {
            'starting_date': TextInput(attrs={ 'placeholder': "Начало отпуска"}),
            'number_of_days': TextInput(attrs={'placeholder': "Количество дней"}),
            'actual_start': TextInput(attrs={'placeholder': "Фактическое начало"}),
            'actual_end': TextInput(attrs={'placeholder': "Фактический конец"}),


        }

class AddSickLeaveForm(forms.ModelForm):
    class Meta:
        model = SickLeave
        fields = ('start_date', 'end_date','code_disease','staff')

        widgets = {
            'start_date': TextInput(attrs={ 'placeholder': "Начало болезни"}),
            'end_date': TextInput(attrs={'placeholder': "Конец болезни"}),
            'code_disease': TextInput(attrs={'placeholder': "Код болезни"}),

        }
class AddShopperForm(forms.ModelForm):
    class Meta:
        model = Shopper
        fields = ('first_name', 'middle_name','last_name','telephone_shopper','email','birthday','address','favorite_shoes')

        widgets = {
            'first_name': TextInput(attrs={ 'placeholder': "Имя"}),
            'middle_name': TextInput(attrs={'placeholder': "Фамилия"}),
            'last_name': TextInput(attrs={'placeholder': "Отчество"}),
            'telephone_shopper': TextInput(attrs={'placeholder': "Телефон"}),
            'email': TextInput(attrs={'placeholder': "Почта"}),
            'birthday': TextInput(attrs={'placeholder': "День рождения"}),
            'address': TextInput(attrs={'placeholder': "Адрес"}),
            'favorite_shoes': TextInput(attrs={'placeholder': "Предпочитаемый бренд"}),


        }

class AddShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = ('brand', 'name','size','price','remaining','cost_of_production')

        widgets = {
            'name': TextInput(attrs={ 'placeholder': "Название"}),
            'size': TextInput(attrs={'placeholder': "Размер"}),
            'price': TextInput(attrs={'placeholder': "Цена"}),
            'remaining': TextInput(attrs={'placeholder': "Остаток"}),
            'cost_of_production': TextInput(attrs={'placeholder': "Оптовая цена"}),


        }

class AddReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ('client', 'date_of_purchase','time_of_purchase','staff','final_price','recepit_id')

        widgets = {
            'date_of_purchase': TextInput(attrs={'placeholder': "Дата оформления"}),
            'time_of_purchase': TextInput(attrs={'placeholder': "Время оформления"}),
            'final_price': TextInput(attrs={'placeholder': "Суммарная цена"}),
        }

class AddPositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ('position_staff', 'salary')

        widgets = {
            'position_staff': TextInput(attrs={'placeholder': "Должность"}),
            'salary': TextInput(attrs={'placeholder': "Оклад"}),
        }

class UpdateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

class UpdateWorkTimeForm(forms.ModelForm):
    class Meta:
        model = WorkTime
        fields = '__all__'

class UpdateVacationForm(forms.ModelForm):
    class Meta:
        model = Vacation
        fields = '__all__'

class UpdateSickLeaveForm(forms.ModelForm):
    class Meta:
        model = SickLeave
        fields = '__all__'

class UpdateShopperForm(forms.ModelForm):
    class Meta:
        model = Shopper
        fields = '__all__'

class UpdateShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = '__all__'

class UpdateReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = '__all__'


