from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('afitop100/', include('afitop100.urls')),
    path('', RedirectView.as_view(url='afitop100/', permanent=True)),
]
