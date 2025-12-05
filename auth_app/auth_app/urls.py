from django.urls import include, path

urlpatterns = [
    path('auth', include('authentication.urls')),
    path('users', include('users.urls')),
    path('authorization', include('authorization.urls')),
    path('posts', include('posts.urls')),
    path('articles', include('article.urls')),
]
