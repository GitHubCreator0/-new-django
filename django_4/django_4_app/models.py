from django.db import models


# class Director(models.Model):
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     age = models.IntegerField()
#
#
# class Film(models.Model):
#     title = models.CharField(max_length=100)
#     year = models.DateField()
#     genre = models.CharField(max_length=100)
#     director = models.ForeignKey(Director, on_delete=models.CASCADE)
#
#
# class Country(models.Model):
#     name = models.CharField(max_length=100)
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     price = models.FloatField()
#     # image = models.ImageField(upload_to='static/images')
#     created_at = models.DateTimeField(auto_now_add=True)   # встановлюється 1 раз
#     modified_at = models.DateTimeField(auto_now=True)      # встановлюється при кожній зміні
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#
#
# class Artist(models.Model):
#     name = models.CharField(max_length=50)
#     year = models.DateTimeField()
#
#
# class Albom(models.Model):
#     name = models.CharField(max_length=50)
#     year = models.DateTimeField()
#     # folder = models.ImageField(upload_to='static/images')
#     artist = models.ForeignKey(Artist, default=1, on_delete=models.SETDEFAULT)
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     year = models.DateField()
#     author = models.CharField(max_length=100)


class Abstract(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(Abstract):
    pass


class Task(Abstract):
    status = models.BooleanField()
    deadline = models.DateField()
    priority = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField()


class Group(models.Model):
    group_number = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    meeting_room = models.CharField(max_length=50)
    students = models.ManyToManyField(Student)


class LibraryCard(models.Model):
    issue_date = models.DateField()
    expiration_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)


class Literature(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=50)
    publication_date = models.DateField()
    year = models.IntegerField()


class BookBorrowing(models.Model):
    borrowing_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    giver_name = models.CharField(max_length=100)

    library_card = models.ForeignKey(LibraryCard, on_delete=models.CASCADE)
    literature = models.ForeignKey(Literature, on_delete=models.CASCADE)
