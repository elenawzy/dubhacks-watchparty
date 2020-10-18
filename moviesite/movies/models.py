from django.db import models

# Create your models here.

class Screening(models.Model):
	RSVPs = models.IntegerField(default = 0)
	MovieTitle = models.CharField(max_length = 100)
	AgeRating = models.IntegerField(default = 0)
	SID = models.IntegerField(primary_key = True)
	Language = models.CharField(max_length = 20)
	YearProduced = models.IntegerField(default = 0)
	#TimeAt = models.TimeField(auto_now = False, auto_now_add = False)
	DateAt = models.DateTimeField(auto_now = False, auto_now_add = False)
	#Tickets = models.ManyToManyField('Viewer', blank = True)

	def __str__(self):
		return self.MovieTitle + " (" + str(self.SID) + ")"


class Viewer(models.Model):
	Username = models.CharField(primary_key = True, max_length = 20)
	Password = models.CharField(max_length = 20)
	Nickname = models.CharField(max_length = 20)
	Rating = models.DecimalField(max_digits = 2, decimal_places = 1)
	Age = models.IntegerField(default = 0)

	def __str__(self):
		return self.Username + " (" + self.Nickname + ")"
	#Friends = models.ManyToManyField("self", blank = True)

class Friend(models.Model):
	Username1 = models.ForeignKey('Viewer', on_delete = models.CASCADE, related_name = 'Viewer1')
	Username2 = models.ForeignKey('Viewer', on_delete = models.CASCADE, related_name = 'Viewer2')

	def __str__(self):
		return self.Username1.Username + " & " + self.Username2.Username 

class Genre(models.Model):
	SID = models.ForeignKey('Screening', on_delete = models.CASCADE)
	GenreTitle = models.CharField(max_length = 30)

	def __str__(self):
		return self.GenreTitle + " (" + str(self.SID) + ")"

class Ticket(models.Model):
	SID = models.ForeignKey('Screening', on_delete = models.CASCADE, related_name = 'ScreeningNum')
	Username = models.ForeignKey('Viewer', on_delete = models.CASCADE, related_name = 'Viewer')

	def __str__(self):
		return self.Username.Username + " (" + str(self.SID) + ")"
