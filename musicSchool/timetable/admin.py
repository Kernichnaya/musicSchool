
#from .models import Author, Book, AuthorForm, BookForm
#from .models import Timetable
#admin.site.register(Timetable)
from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)