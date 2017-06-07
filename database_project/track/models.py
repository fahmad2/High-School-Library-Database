# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta
from datetime import datetime

#create your models here

def validate_length13(value):
    print 'reached here'
    length = 13
    if len(value) != int(length):
        raise ValidationError(
            "ISBN not 13 digits"
        )

class Borrower(models.Model):
    STUDENT= 'ST'
    TEACHER= 'TE'
    ADMIN= 'AD'
    CLASS= 'CL'
    PARENT= 'PT'
    TYPE_CHOICES =(
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (ADMIN, 'Admin'),
        (CLASS, 'Class'),
        (PARENT, 'Parent')
    )
    name = models.CharField(max_length=30)
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=STUDENT
    )
    checkOutStatus = models.BooleanField(default = False, editable = True)
    def __unicode__(self):
        return self.name

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30,unique=True)
    author = models.CharField(max_length=30)

    ISBN = models.CharField(max_length=13, validators=[validate_length13],unique=True)
    check_out_date = models.DateField(default=None,blank=True, null=True)
    check_out_by = models.ForeignKey(Borrower,default=None)
    search_capability = models.BooleanField(default = False, editable = True)
    def __unicode__(self):
        return self.title

class Order(models.Model):
    name = models.CharField(max_length=50,unique=False)
    placed_by = models.ForeignKey(Borrower, default = Borrower.ADMIN)
    PC_REPAIR = 'PR'
    BOOK_ORDER = 'BO'
    CLEANING_SUPPLIES  = 'CS'
    FURNITURE_ORDER = 'FO'
    OTHER = 'O'
    TYPE_CHOICES =(
   	(PC_REPAIR, 'Pc Repair'),
	(BOOK_ORDER, 'Book Order'),
	(CLEANING_SUPPLIES, 'Cleaning Supplies'),
	(FURNITURE_ORDER, 'Furniture Order'),
	(OTHER, 'Other')
    )
    type = models.CharField(
    	max_length=2,
	choices = TYPE_CHOICES,
	default = OTHER
    )
   
    def __unicode__(self):
	return self.name
