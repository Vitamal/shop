from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect

from .app_utils import user_import
from .forms.upload_file_form import UploadFileForm
from .models import Order, User


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_datetime')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'registration_date', 'order')
    change_list_template = "admin/model_change_list.html"

    def get_urls(self):
        urls = super(UserAdmin, self).get_urls()
        custom_urls = [
            url('^import/$', self.process_import, name='process_import'), ]
        return custom_urls + urls

    def process_import(self, request, *args, **kwargs):
        if request.method == 'GET':
            return render(request, 'admin/import_from_csv.html', {'form': UploadFileForm()})
        elif request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                user_import(request, request.FILES['file'])
                return HttpResponseRedirect('/admin/user_orders/user/')
            else:
                return render(request, 'admin/import_from_csv.html', {'form': form})
        else:
            raise Http404('Unsupported request method')
