from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    #path('blog/', include('pixels_blog.urls')),
    path('', include('pixels_blog.urls'))
]
