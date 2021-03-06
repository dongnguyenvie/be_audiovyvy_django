"""be_audiovyvy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from audio_src.apps.plugins.jwt import urlpatterns as urlJWT
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


URL_APPS = [
    path('article/', include(('audio_src.apps.articles.api.urls', 'article-api'), namespace="article-api")),
    path('user/', include(('audio_src.apps.users.api.urls', 'user-api'), namespace="user-api")),
    path('blog/', include(('audio_src.apps.blogs.api.urls', 'blog-api'), namespace="blog-api")),
    path('widget/', include(('audio_src.apps.widgets.api.urls', 'widgets-api'), namespace="widgets-api")),
    path('category/', include(('audio_src.apps.categories.api.urls', 'category-api'), namespace="category-api")),
    path('menu/', include(('audio_src.apps.menus.api.urls', 'menu-api'), namespace="menu-api")),
    path('setting/', include(('audio_src.apps.settings.api.urls', 'setting-api'), namespace="setting-api")),
    path('tag/', include(('audio_src.apps.tags.api.urls', 'tag-api'), namespace="tag-api")),
    path('comment/', include(('audio_src.apps.comments.api.urls', 'comment-api'), namespace="comment-api")),
    path('media/', include(('audio_src.apps.medias.api.urls', 'media-api'), namespace="media-api")),

    # path('aaaa/', include((urlJWT, 'asetting-api'), namespace="asetting-api"))
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(URL_APPS)),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', include(('audio_src.apps.utils.swagger.urls', 'swagger-api'), namespace="swagger-api")),
    path('test/', include('audio_src.apps.test_api.api.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)