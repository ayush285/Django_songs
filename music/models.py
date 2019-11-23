from django.contrib.auth.models import Permission, User
from django.db import models


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

# First - UserID, FormID, FormName, FormDescr
# Second - QuesID, Label, Type, Text

# class Form(models.Model):
#     user = models.ForeignKey(User, default=1)
#     # form_id = models.IntegerField(default=1)
#     form_name = models.CharField(max_length=50)
#     form_desc = models.CharField(max_length=500)

#     def __str__(self):
#         return self.form_name + " " + self.form_desc


# class Question(models.Model):
#     #ques_id = models.IntegerField(default=1)
#     form = models.ForeignKey(Form, on_delete=models.CASCADE)
#     ques_type = models.CharField(max_length=500)
#     ques_text = models.CharField(max_length=500)
#     is_req = models.BooleanField(default=False)
#     is_vis = models.BooleanField(default=False)

#     def __str__(self):
#         return self.ques_text + " " self.ques_type


# class Data1(models.Model):
#     client= models.CharField(max_length=100,default='Hi')
#     Answer1= models.CharField(max_length=100,default='Hi')
#     Answer2= models.CharField(max_length=200,default='Hi')
#     Answer3= models.CharField(max_length=200,default='Hi')
    
# class Data2(models.Model):
#     client= models.CharField(max_length=100,default='Hi')
#     Answer1= models.CharField(max_length=100,default='Hi')
#     Answer2= models.CharField(max_length=200,default='Hi')
#     Answer3= models.CharField(max_length=200,default='Hi')

# class QuesType(models.Model):
#     TypeID= models.IntegerField()
#     Type= models.CharField(max_length=50,default='Hi')

# class UserForm(models.Model):
#     UserID= models.IntegerField()
#     FormID= models.IntegerField()
#     FormName=models.CharField(max_length=100,default='Hi')

#     class Meta:
        
#         unique_together=(("UserID","FormID"),)

# class Question(models.Model):
#     QuesID= models.IntegerField()
#     FormID= models.ForeignKey(UserForm,on_delete=models.CASCADE)
#     TypeID= models.IntegerField()
#     Questxt= models.CharField(max_length=100,default='Hi')

#     class Meta:
#         unique_together=(("QuesID","FormID"),)


# class Mcq(models.Model):
#     QuesID= models.ForeignKey(Question,on_delete=models.CASCADE)
#     Options= models.CharField(max_length=100,default='Hi')