from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add',views.add, name='add'),
    path('add_record',views.add_record, name='add_record'),
    path('produtos', views.produtos, name='produtos'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/update_record/<int:id>', views.update_record, name='update_record'),

]