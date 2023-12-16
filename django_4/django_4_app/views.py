from django.shortcuts import render, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm, RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class RegistrationView(CreateView):
    template_name = 'registration.html'
    # model = User
    # fields = ['username']
    form_class = RegistrationForm
    success_url = reverse_lazy('/')

    def get_success_url(self):
        responce = HttpResponse()
        responce.set_cookie('name', self.object.username)
        return '/'


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})


class LoginPage(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_authenticated_user = True


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/registration')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        return context


class TestView(TemplateView):
    template_name = 'test.html'

    def post(self, request):
        data = request.POST
        print(data['text'])
        return JsonResponse({'resp': data['text']}, safe=False)


class HomeView(ListView):
    model = Project
    paginate_by = 2
    template_name = 'Home.html'


def home(request):
    projects = Project.objects.all()
    user = request.user
    context = {'user': user, 'projects': projects}
    return render(request, 'home.html', context)

    def get_context_data(self, **kwargs):
        context = super()


def project_edit(request, **kwargs):
    p = Project.objects.get(id=kwargs['id'])
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            p.name = name
            p.save()
            return redirect('/')
    else:
        form = ProjectForm(initial={'name': p.name})
        context = {'form': form}
        return render(request, 'project_create.html', context)


class ProjectView(CreateView):
    form_class = TaskForm
    template_name = 'project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = Project.objects.get(id=self.kwargs['id'])
        tasks = Task.objects.filter(project=project)
        context['project'] = project
        context['tasks'] = tasks
        return context

    def get_success_url(self, **kwargs):
        return f'project/{self.kwargs["id"]}'


def project(request, **kwargs):
    p = Project.objects.get(id=kwargs['id'])
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            deadline = form.cleaned_data['deadline']
            status = form.cleaned_data['status']
            priority = form.cleaned_data['priority']
            task = Task(name=name, deadline=deadline, status=status, priority=priority, project=p)
            task.save()
            return redirect(f'/project/{p.id}')
    else:
        form = TaskForm()
        tasks = Task.objects.filter(project=p)
        return render(request, 'project.html', {'project': p, 'tasks': tasks, 'form': form})


class ProjectCreate(TemplateView):
    template_name = 'project_create.html'

    def get_contex_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectForm()
        return context

    def post(self, request):
        data = request.POST
        project = Project(name=data['text'])
        project.save()
        return JsonResponse({'resp': data['text']}, safe=False)


# def page1(request):
#     if request.method == 'POST':
#         data = request.POST
#         name = data['name']
#         surname = data['surname']
#         age = data['age']
#         dir = Director(name=name, surname=surname, age=age)
#         dir.save()
#     return render(request, 'page1.html')
#
# def page2(request):
#     dirs = Director.objects.all()
#
#     return render(request, 'page2.html', {'data': dirs})
#
# # CRUD - Create Read Update Delete
# def page3(request):
#     if request.method == 'POST':
#         form = FilmForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['title']
#             genre = form.cleaned_data['genre']
#             year = form.cleaned_data['year']
#             dir = Director.objects.get(id=1)
#             film = Film(title=name, genre=genre, year=year, director=dir)
#             film.save()
#             return render(request, 'page3.html', {'form': form})
#     else:
#         form = FilmForm()
#         return render(request, 'page3.html', {'form': form})
#
#
# def book_create(request):
#     if request.method == 'POST':
#         form = BookForm1(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             year = form.cleaned_data['year']
#             author = form.cleaned_data['author']
#             book = Book(title=title, year=year, author=author)
#             book.save()
#             return redirect('/create_post')
#     else:
#         form = BookForm1()
#         return render(request, 'page3.html', {'form': form})
#
#
# def  form_page(request):
#     form = LoginForm()
#     return render(request, 'page3.html', {'form': form})
