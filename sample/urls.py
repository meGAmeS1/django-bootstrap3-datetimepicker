from django.conf import settings
from django.conf.urls import url

from django.conf.urls.static import static


urlpatterns = [
    url(r'.*', 'sample.todo_app.views.edit'),
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]