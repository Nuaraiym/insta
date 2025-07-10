from .models import Post, Comment, CommentLike
from modeltranslation.translator import TranslationOptions,register

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('post', 'description','hashtag')

@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('post', 'text')

@register(CommentLike)
class CommentLikeTranslationOptions(TranslationOptions):
    fields = ('comment',)