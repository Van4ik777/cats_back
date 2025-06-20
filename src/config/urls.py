from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

schema_view = get_schema_view(
    openapi.Info(title="Event API", default_version='v1'),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cats.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
