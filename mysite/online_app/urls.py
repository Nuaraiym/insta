from django.urls import path,include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()


router.register(r'users',UserProfileViewSet,basename='users_list')
router.register(r'follow',FollowViewSet,basename='follow_list')
router.register(r'post',PostViewSet,basename='post_list')
router.register(r'post_like',PostLikeViewSet,basename='post_like_list')
router.register(r'comment',CommentLikeViewSet,basename='comment_list')
router.register(r'comment_like',CommentLikeViewSet,basename='comment_like_list')
router.register(r'story',StoryViewSet,basename='story_list')
router.register(r'saveUser',SaveUserViewSet,basename='saveUser_list')
router.register(r'save_item',SaveItemViewSet,basename='save_item_list')
router.register(r'post_rating',PostRatingViewSet,basename='post_rating_list')
router.register(r'chat',ChatViewSet,basename='chat_list')
router.register(r'message',MessageViewSet,basename='message_list')


urlpatterns = [
    path('',include(router.urls)),
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list'),
]

