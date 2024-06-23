from django.contrib import admin
from django.urls import path,include


admin.site.site_header="IFSC Bank Admin"
admin.site.site_title="IFSC Admin Portal"
admin.site.index_title="Welcome to IFSC Bank "

urlpatterns= [
   path('admin/', admin.site.urls),
   path('', include('bank.urls')),
]