from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list),
    path('categories/<int:pk>/', views.category_detail),
    path('courses/', views.course_list),
    path('courses/<int:pk>/', views.course_detail),
    path('lessons/', views.lesson_list),
    path('lessons/<int:pk>/', views.lesson_detail),
    path('tasks/', views.task_list),
    path('tasks/<int:pk>/', views.task_detail),
    path('submissions/', views.submission_list),
    path('submissions/<int:pk>/', views.submission_detail),
    path('purchases/', views.purchase_list),
    path('purchases/<int:pk>/', views.purchase_detail),
    path('progress/', views.progress_list),
    path('progress/<int:pk>/', views.progress_detail),
    path('reviews/', views.review_list),
    path('reviews/<int:pk>/', views.review_detail),
]
