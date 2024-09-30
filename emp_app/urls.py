from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name="index"),
    path('emp-add/',views.emp_add,name="emp_add"),
    path('emp-remove/',views.emp_remove,name="emp_remove"),
    path('filter/',views.filter,name="filter"),
    path('view-all-emp/',views.view_all_emp,name="view_all_emp"),
    path('emp-single',views.emp_single,name="emp_single"),
    path('disp/<int:emp_id>',views.disp,name='disp'),
]