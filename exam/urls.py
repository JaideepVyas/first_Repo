from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    return redirect('/exam/')

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ expose login at ROOT
    path('', include('accounts.urls')),

    path('exam/', include('examapp.urls')),
    path('results/', include('results.urls')),

    path('', home),
]
