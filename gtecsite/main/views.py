from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView
from .models import Course, Trainer,Category

# Home Page
class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryListView(ListView):
    model = Category
    template_name = 'main/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'main/category_detail.html'  # Create this template
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['certificate_courses'] = category.courses.filter(course_type='certificate')
        context['diploma_courses'] = category.courses.filter(course_type='diploma')
        context['master_courses'] = category.courses.filter(course_type='master')
        return context


class CoursesByCategoryView(ListView):
    model = Course
    template_name = 'main/courses_by_category.html'
    context_object_name = 'courses'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        return Course.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class CourseListView(ListView):
    model = Course
    template_name = 'main/course.html'  # You can name this anything
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'main/course_detail.html'  # your template file
    context_object_name = 'course'

class TrainerListView(ListView):
    model = Trainer
    template_name = 'main/trainers.html'
    context_object_name = 'trainers'


class AboutView(TemplateView):
    template_name = 'main/about.html'


class ContactView(TemplateView):
    template_name = 'main/contact.html'