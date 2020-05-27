from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
	        ('Аккордеон', 'Аккордеон'),
		('Гитара', 'Гитара'),
                ('Баян','Баян'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = [
    ('Понедельник', (
            ('Пн. 10:00', 'Пн. 10:00'),
            ('Пн. 12:00', 'Пн. 12:00'),
            ('Пн. 15:00', 'Пн. 15:00'),
            ('Пн. 17:00', 'Пн. 17:00'),
                    )
    ),
    ('Вторник', (
            ('Вт. 10:00', 'Вт. 10:00'),
            ('Вт. 12:00', 'Вт. 12:00'),
            ('Вт. 15:00', 'Вт. 15:00'),
            ('Вт. 17:00', 'Вт. 17:00'),
                    )
    ),
    ('Среда', (
            ('Ср. 10:00', 'Ср. 10:00'),
            ('Ср. 12:00', 'Ср. 12:00'),
            ('Ср. 15:00', 'Ср. 15:00'),
            ('Ср. 17:00', 'Ср. 17:00'),
                    )
    ),   
    ('Четверг', (
            ('Чт. Пт.10:00', 'Чт. 10:00'),
            ('Чт. 12:00', 'Чт. 12:00'),
            ('Чт. 15:00', 'Чт. 15:00'),
            ('Чт. 17:00', 'Чт. 17:00'),
                    )
    ),  
    ('Пятница', (
            ('Пт. 10:00', 'Пт. 10:00'),
            ('Пт. 12:00', 'Пт. 12:00'),
            ('Пт. 15:00', 'Пт. 15:00'),
            ('Пт. 17:00', 'Пт. 17:00'),
                    )),
]

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return self.product.name

