from django.db import models

class Hero(models.Model):
    restaurantName = models.CharField(max_length=100, verbose_name="Restaurant name", default="El Deliciós d'Etiopia")
    restaurantMotto = models.TextField(verbose_name="Restaurant Motto", default='Fresh and Delicious Ethiopian Food just for you!')
    def __str__(self):
        return self.restaurantName

class About(models.Model):
    aboutTitle = models.CharField(max_length=100, verbose_name="About Us Title", default='About Us')
    aboutPar1 = models.TextField(verbose_name="About us content 1", default='')
    aboutPar2 = models.TextField(verbose_name="About us content 2", default='')
    aboutPar3 = models.TextField(verbose_name="About us content 3", default='')
    def __str__(self):
        return self.aboutTitle

class WhyUs(models.Model):
    whyUsTitle = models.CharField(max_length=100, verbose_name="Why Us title", default='Why choose our restaurant')
    whyUs1 = models.CharField(max_length=100, verbose_name="Title 1", default='')
    whyUsDesc1 = models.TextField(verbose_name="Content 1", default='')
    whyUs2 = models.CharField(max_length=100, verbose_name="Title 2", default='')
    whyUsDesc2 = models.TextField(verbose_name="Content 2", default='')
    whyUs3 = models.CharField(max_length=100, verbose_name="Title 3", default='')
    whyUsDesc3 = models.TextField(verbose_name="Content 3", default='')
    def __str__(self):
        return self.whyUsTitle

class Footer(models.Model):
    footerTitle = models.CharField(max_length=100, verbose_name="Restaurant name", default="El Deliciós d'Etiopia")
    footerBody = models.CharField(max_length=200, verbose_name="Restaurant Motto", default='Fresh and Delicious Ethiopian Food just for you!')
    twitterLink = models.TextField(max_length=100, verbose_name="Twitter Link")
    facebookLink = models.TextField(max_length=100, verbose_name="Facebook Link")
    instagramLink = models.TextField(max_length=100, verbose_name="Instagram Link")
    linkedinLink = models.TextField(max_length=100, verbose_name="LinkedIn Link")
    year = models.TextField(max_length=100, default='2021', verbose_name="Year")
    copyrightText = models.TextField(max_length=100, verbose_name="Copyright text")
    def __str__(self):
        return self.footerTitle

class Location(models.Model):
    avenue = models.CharField(max_length=200, verbose_name="Avenue")
    city = models.CharField(max_length=100, verbose_name="City")
    country = models.CharField(max_length=100, verbose_name="Country")
    def __str__(self):
        return self.avenue +" " + self.city +", "+ self.country

class OpenHours(models.Model):
    weekdays_startTime  = models.CharField(max_length=100, verbose_name="Weekdays Opening time")
    weekdays_endTime = models.CharField(max_length=100, verbose_name="Weekdays Closing time")
    weekends_startTime  = models.CharField(max_length=100, verbose_name="Weekends Opening time")
    weekends_endTime = models.CharField(max_length=100, verbose_name="Weekends Closing time")

    def __str__(self):
        return self.weekdays_startTime +" " + self.weekdays_endTime + ", " + self.weekends_startTime+ " " + self.weekends_endTime

class Email(models.Model):
    email_address  = models.TextField(max_length=100, verbose_name="Email address")
    def __str__(self):
        return self.email_address

class Call(models.Model):
    phone_number  = models.TextField(max_length=100, verbose_name="Phone number")
    def __str__(self):
        return self.phone_number

class StarterMenu(models.Model):
    starterOption = models.CharField(max_length=100, default="Starter", editable=False)
    starterContent = models.CharField(max_length=100, verbose_name="Starter name")
    starterDesc = models.TextField(verbose_name="Starter content")
    starterPrice = models.CharField(max_length=100, verbose_name="Price")
    def __str__(self):
        return self.starterContent
    
class MainMenu(models.Model):
    mainOption = models.CharField(max_length=100, default="Main", editable=False)
    mainContent = models.CharField(max_length=100, verbose_name="Food name")
    mainDesc = models.TextField(verbose_name="Food content")
    mainPrice = models.CharField(max_length=100, verbose_name="Price")
    def __str__(self):
        return self.mainContent
    
class DessertMenu(models.Model):
    dessertOption = models.CharField(max_length=100, default="Dessert", editable=False)
    dessertContent = models.CharField(max_length=100, verbose_name="Dessert name")
    dessertDesc = models.TextField(verbose_name="Dessert content")
    dessertPrice = models.CharField(max_length=100, verbose_name="Price")


    def __str__(self):
        return self.dessertContent
    
class DrinksMenu(models.Model):
    drinksOption = models.CharField(max_length=100, default="Drink", editable=False)
    drinksContent = models.CharField(max_length=100, verbose_name="Drink name")
    drinksDesc = models.TextField(verbose_name="Drink content")
    drinksPrice = models.CharField(max_length=100, verbose_name="Price")
    def __str__(self):
        return self.drinksContent
    
