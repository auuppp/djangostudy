from django.contrib import admin
from models import Publisher, Author, Book
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name','email')
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher','publication_date')
    list_filter = ('publication_date','publisher',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'authors', 'publication_date', 'publisher')
    #filter_horizontal = ('authors',)
    filter_vertical = ('authors',)
    raw_id_fields = ('publisher',)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)


# Register your models here.
