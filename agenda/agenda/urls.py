
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
#include sirve para incluir un archivo con varias rutas del proyecto

#se puede usar variables definidas en clase SETTING
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#el metodo static., retorna lista de URLPatterns
#
