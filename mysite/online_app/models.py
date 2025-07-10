from django.db import models
from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):
    bio = models.TextField(null=True,blank=True)
    images_profile = models.ImageField(upload_to='images/',null=True,blank=True)
    website = models.URLField(null=True,blank=True)


class Follow(models.Model):
    follower = models.CharField(max_length=64)
    following = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower},{self.created_at}'

class Post(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    post = models.CharField(null=True,blank=True)
    image = models.ImageField(upload_to='post_images')
    video = models.FileField(upload_to='post_video')
    description = models.TextField()
    hashtag = models.CharField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.image},{self.created_at}'

class PostLike(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='users')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_like')
    like = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
       unique_together = ('user','post')

    def __str__(self):
        return f'{self.user}'

    # def unique_together(self):
    #    return PostLike.objects.filter(post=self.request.user)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.CharField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.created_at}'

class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    comment = models.TextField(null=True,blank=True)
    like = models.ForeignKey(PostLike,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.like},{self.comment}'

class Story(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    image = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='story_image')
    video = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='store_video')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.image},{self.created_at}'


class SaveUser(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class SaveItem(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    save_user = models.ForeignKey(SaveUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post},{self.created_at}'

class PostRating(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    post = models.OneToOneField(PostLike,on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.post}<{self.rating},{self.created_at}'


class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.person}'

class Message(models.Model):
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    text = models.TextField()
    images = models.ImageField(upload_to='message_images',null=True,blank=True)
    video = models.FileField(upload_to='message_video',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.text}'




