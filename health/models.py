from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class HealthProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)],null=True,blank=True,help_text="Enter age :")
	height = models.FloatField(validators=[MaxValueValidator(300), MinValueValidator(20)],null=True,blank=True,help_text="Enter height (In Centimeter) :")
	weight = models.FloatField(validators=[MaxValueValidator(300), MinValueValidator(20)],null=True,blank=True,help_text="Enter weight (In Lbs) :")
	ailments = models.TextField(max_length=1000, null=True, blank=True, help_text='Enter comma separated list of pre-existing ailments :')
	tobacco = models.BooleanField(help_text="Do you consume tobacco?", default=False)
	smoke = models.BooleanField(help_text="Do you consume smoke?", default=False)
	drink = models.BooleanField(help_text="Do you consume drink?", default=False)
	POSS_EXERCISE = (
	    (2, '>15 hours/week'),
	    (1, '6-15 hours/week'),
	    (0, '<6 hours/week'),
	)
	exercise = models.IntegerField(choices=POSS_EXERCISE, blank=True, default=1, help_text='Select how much do you exercise?')
	POSS_TRAVEL = (
		(2, '>10 hours/week'),
		(1, '5-10 hours/week'),
		(0, '<5 hours/week'),
	)
	travel_time = models.IntegerField(choices=POSS_TRAVEL, blank=True, default=1, help_text='Select how much do you travel?')
	POSS_SLEEP = (
		(2, '>8 hours/day'),
		(1, '6-8 hours/day'),
		(0, '<6 hours/day'),
	)
	sleep_time = models.IntegerField(choices=POSS_SLEEP, blank=True, default=1, help_text='Select how much do you sleep?')
	job_type = models.TextField(max_length=1000, null=True, blank=True, help_text='Enter your job description :')

	def __str__(self):
	    """
	    String for representing the Model object (in Admin site etc.)
	    """
	    return self.user.first_name