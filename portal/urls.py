from django.urls import path
from .views import login_view , register , homeview , del_student_view , add_student_view,edit_student_view
urlpatterns = [
    path('' , login_view , name= 'login'),
    path('register' , register , name= 'register'),
    path('home' , homeview , name= 'home'),
    path('add/student' , add_student_view , name= 'add_student'),
    path('edit/student/<int:stu_id>' , edit_student_view, name= 'edit_student'),
    path('del/student/<int:stu_id>' , del_student_view , name= 'del_student'),

]