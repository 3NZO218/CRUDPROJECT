from django.contrib import admin
from .models import Book, Author ,Store
from .models import Publisher
from django.contrib.auth import get_user_model

CustomUser = get_user_model()
users = CustomUser.objects.all()
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Store)

