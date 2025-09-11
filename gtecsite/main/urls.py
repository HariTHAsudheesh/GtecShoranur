from django.urls import path
from .views import (
    HomeView,
    CategoryListView,CoursesByCategoryView,CategoryDetailView,
    CourseListView,
    CourseDetailView,
    TrainerListView,
    AboutView,
    ContactView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CoursesByCategoryView.as_view(), name='courses_by_category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('trainers/', TrainerListView.as_view(), name='trainer_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
