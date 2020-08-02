from django.db import models

# Create your models here.
TRUE_FALSE_CHOICES = (
	(True, 'Yes'),
	(False, 'No'),
)

MANUFACTURED_YEAR_CHOICES = (
	('1970', '1970'),
	('1980', '1980'),
	('1990', '1990'),
	('2000', '2000'),
	('2010', '2010'),
	('2020', '2020'),
)

CAR_MODEL_CHOICES = (
	('toyota', 'Toyota'),
	('mazda', 'Mazda'),
	('renault', 'Renault'),
	('ford', 'Ford'),
	('dansun', 'Datsun'),
)

class FileClaimVehicleTheft(models.Model):
	name = models.CharField(max_length=100, db_index=True)
	occupation = models.CharField(max_length=50, db_index=True)
	phone_number = models.IntegerField(db_index=True)
	email = models.EmailField(max_length=50, db_index=True)

	vehicle_registration = models.CharField(max_length=100, db_index=True)
	vehicle_make = models.CharField(max_length=200, choices=CAR_MODEL_CHOICES, db_index=True, default='')
	manufactured_year = models.CharField(max_length=200, choices=MANUFACTURED_YEAR_CHOICES, db_index=True)

	hp_loan_agreements = models.BooleanField(default=True)
	# hp_loan_agreements = models.CharField(max_length=200, choices=TRUE_FALSE_CHOICES, db_index=True, default='')
	
	class Meta:
		ordering = ('name',)
		verbose_name = 'car_theft_claim'
		verbose_name_plural = 'car_theft_claims'

	def __str__(self):
		return self.name