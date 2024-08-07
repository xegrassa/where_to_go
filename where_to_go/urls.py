from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

import places.views
from places import views as places_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("places/<int:place_id>/", places_view.read_place, name="place_detail"),
    path("", places.views.show_main),
    path("tinymce/", include("tinymce.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += debug_toolbar_urls()
