from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views  # Встроенные представления Django




# user password - 728fdkd222222
#admin password - 1234
urlpatterns = [

    path('', views.login, name='Home'),
    path('index', views.index, name='index'),
    path('SPosition', views.SPosition, name='SPosition'),
    path('SReceipt', views.SReceipt, name='SReceipt'),
    path('SShoes', views.SShoes, name='SShoes'),
    path('SStaff', views.SStaff, name='SStaff'),
    path('SShopper', views.SShopper, name='SShopper'),
    path('SSickLeave', views.SSickLeave, name='SSickLeave'),
    path('SVacation', views.SVacation, name='SVacation'),
    path('SWorkTime', views.SWorkTime, name='SWorkTime'),

    path('api/tables/', views.get_tables, name='get_tables'),  # API для списка таблиц
    path('api/tables/<str:table_name>/', views.get_table_data, name='get_table_data'),  # API для данных таблицы
    path('api/query/<int:query_id>/', views.run_query, name='run_query'),  # API для выполнения запросов
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login, name='login'),


    path('AddStaff/', views.AddStaff, name='AddStaff'),
    path('AddWorkTime/', views.AddWorkTime, name='AddWorkTime'),
    path('AddVacation/', views.AddVacation, name='AddVacation'),
    path('AddSickLeave/', views.AddSickLeave, name='AddSickLeave'),
    path('AddShopper/', views.AddShopper, name='AddShopper'),
    path('AddShoes/', views.AddShoes, name='AddShoes'),
    path('AddReceipt/', views.AddReceipt, name='AddReceipt'),
    path('AddPosition/', views.AddPosition, name='AddPosition'),


    path('<int:id_staff>/UpdateStaff', views.edit_staff, name='UpdateStaff'),
    path('<int:id_work_time>/UpdateWorkTime', views.edit_WorkTime, name='UpdateWorkTime'),
    path('<int:id_vacation>/UpdateVacation', views.edit_Vacation, name='UpdateVacation'),
    path('<int:id_leave>/UpdateSickLeave', views.edit_SickLeave, name='UpdateSickLeave'),
    path('<int:id_client>/UpdateShopper', views.edit_Shopper, name='UpdateShopper'),
    path('<int:id_shoes>/UpdateShoes', views.edit_Shoes, name='UpdateShoes'),

    path('<int:id_staff>/DeleteStaff', views.Delete_Staff, name='DeleteStaff'),
    path('<int:id_work_time>/DeleteWorkTime', views.Delete_WorkTime, name='DeleteWorkTime'),
    path('<int:id_client>/DeleteShopper', views.Delete_Shopper, name='DeleteShopper'),
    path('<int:id_shoes>/DeleteShoes', views.Delete_Shoes, name='DeleteShoes'),




    #Выходные документы
    path('Dquarterly_revenue', views.quarterly_revenue, name='Dquarterly_revenue'),
    path('new_shoes', views.new_shoes, name='new_shoes'),
    path('shoe_order', views.shoe_order, name='shoe_order'),
    path('Document', views.document, name='Document'),


]


