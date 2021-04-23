from django.contrib import admin
from django.urls import path
from app.views import showMsg,details_view,create_view,update_view,delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('MyMessage/', showMsg),
    path('MyMessage/MyMessage/delete/<id>/',delete_task),
    path('MyMessage/create/', create_view),
    path('MyMessage/update/<id>/',update_view),
    path('MyMessage/<id>/', details_view),


]
