from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('relationship_app.urls')),  # 👈 connect your app
=======
    path('', include('bookshelf.urls')),
>>>>>>> ce7335629f97d40a13c334895130406c72ec0ccf
]
