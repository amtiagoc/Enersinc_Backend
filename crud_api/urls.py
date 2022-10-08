from django.urls import path
from .views import UserList, UserDetail
#, CreateUser, AdminUserUser

app_name = 'crud_api'

urlpatterns = [
    path('<int:pk>/',UserDetail.as_view(), name='detailuser'),
    path('',UserList.as_view(), name='listuser'),
    # Post Admin URLs
    #path('admin/create',CreateUser.as_view(),name='createuser'),
    #path('admin/edit/<int:pk>/',AdminPostUser.as_view(), name='admindetailuser'),
    
]
