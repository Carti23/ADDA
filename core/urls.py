from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token


#swagger setup
schema_view = get_swagger_view(title='Pastebin API')
router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')),
    path('swagger/', schema_view),
    path('api/payment/', include('payments.urls')),
    path('auth/', obtain_auth_token),
    path('api/v2/', include(router.urls)),
    # path('chat/', include('chat_room.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)