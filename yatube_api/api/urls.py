from django.urls import include,path
from rest_framework import routers
from api.views import GroupViewSet,PostViewSet,CommentViewSet
from rest_framework.authtoken import views
router=routers.DefaultRouter()
router.register('groups',GroupViewSet,basename='groups')
router.register('posts',PostViewSet,basename='posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)



urlpatterns=[
    path('',include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]