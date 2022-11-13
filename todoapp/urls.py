from django.urls import path
from todoapp import views

urlpatterns = [
    path("list/" , views.posts_list_view),
    path("user/" , views.register_user),
    path('create/todo/' , views.create_new_todo_view),
    path('detail/todo/<int:id>/' , views.detail_todo_view),
    path('edit/<int:id>/' , views.update_view),
    path('delete/<int:id>/' , views.delete_view)

]
