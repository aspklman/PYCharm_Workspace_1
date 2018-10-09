#coding:utf-8
from django.contrib import admin
from books.models import Publisher, Book, Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')
    fields = ('name', 'country', 'state_province', 'city', 'address')       #【编辑页面】的字段顺序，及编辑页面显示的字段

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')      #【显示页面】的字段
    list_filter = ('publication_date','publisher')                            #【显示页面】右侧的过滤器
    date_hierarchy = 'publication_date'
    ordering = ['-publication_date']                                            #【显示页面】排序
    fields = ('title', 'authors', 'publisher')                                 #【编辑页面】的字段顺序，及编辑页面显示的字段
    filter_horizontal = ('authors',)                                              #【编辑页面】某字段过滤选择器的显示方式(水平/垂直)
    raw_id_fields = ('publisher',)

# Register your models here.
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)