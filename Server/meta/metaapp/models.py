from django.db import models

# Create your models here.

class Games(models.Model): 
    class Meta: 
        db_table = 'games' 
    developer_id = models.IntegerField() 
    publisher_id = models.IntegerField() 
    brief = models.TextField() 
    description = models.CharField(max_length= 10000)  
    # date = models.DateTimeField() 
    name = models.TextField()
    
class Developers(models.Model): 
    class Meta: 
        db_table = 'developers' 
    name = models.TextField() 
    country = models.TextField() 
 
class Steam_games(models.Model): 
    class Meta: 
        db_table = 'steam_games' 
    url = models.TextField() 
    rating = models.TextField() 
    price = models.IntegerField() 
 
class Egs_games(models.Model): 
    class Meta: 
        db_table = 'egs_games' 
    url = models.TextField() 
    rating = models.TextField() 
    price = models.IntegerField() 
 
class Publishers(models.Model): 
    class Meta: 
        db_table = 'publishers' 
    name = models.TextField() 
    country = models.TextField() 
 
class Genre(models.Model): 
    class Meta: 
        db_table = 'genre' 
    genre = models.TextField()