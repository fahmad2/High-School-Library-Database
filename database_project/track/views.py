# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from .models import Borrower, Book, Order
from datetime import timedelta
import datetime
import math

# Create your views here.

def index(request):
	latest_borrower_list = Book.objects.all()
	output = ", ".join([str(b.check_out_date)+'\n' for b in latest_borrower_list])
	return HttpResponse(output)

def application(request):
	return HttpResponse("Hello. You are at the application index")

def studentsWithBooks(request):
	latest_student_list = Borrower.objects.filter(type = 'ST', checkOutStatus = True)
        checkedOut_book_list = Book.objects.all()
	final_list =[]
        for a in checkedOut_book_list:
		for b in latest_student_list:
			if(a.check_out_by == b):
 				final_list.append(a)
				break
	output = '  ---  '.join(["StudentName: "+str(c.check_out_by)+", BookName: "+str(c.title)+", CheckOutDate: "+str(c.check_out_date)+", DueDate: "+str(c.check_out_date+timedelta(days=14)) for c in final_list])
	return HttpResponse(output)

def users(request):
	return HttpResponse("Hello. You are at the users index")

def booksCheckedOut(request, param):
	final_list = []
	output = ""
	class_name_list = Borrower.objects.filter(name = param, type = 'CL')
	if(len(class_name_list) > 0):
		class_name = class_name_list[0]
		book_list = Book.objects.all()
		for a in book_list:
		    if(a.check_out_by == class_name):
			final_list.append(a)
		output = ", ".join("result: "+b.title+" search request: "+param for b in final_list)
	else:
 		book_name_list = Book.objects.filter(title =param)
		if(len(book_name_list) > 0):
		    book_name = book_name_list[0]
	 	    final_list.append(book_name)
		    output = ", ".join("result: "+b.title+" CheckedOutBy: "+str(b.check_out_by) for b in final_list)
		else:
		    book_num_list = Book.objects.filter(ISBN = param)
		    if(len(book_num_list) > 0):
			book_num = book_num_list[0]
		    	final_list.append(book_num)
     			output = ", ".join("result: "+b.title+" search request: "+param for b in final_list)
	return HttpResponse(output)

def orders(request):
	order_list = Order.objects.order_by('-type')[0:5]
	output = ', '.join(str(b) for b in order_list)
	return HttpResponse(output)

def booksInSystemWithSearch(request):
	book_list = Book.objects.filter(search_capability = True)
	output = ', '.join([str(b) for b in book_list])
	return HttpResponse(output)

def studentsInfo(request):
	final_list = []
	amount_due_list = []
	students_list = Borrower.objects.filter(type = 'ST')
  	parents_list = Borrower.objects.filter(type = 'PT')
	checked_out_list = Book.objects.all()
	output = ""
	for a in checked_out_list:
		for b in students_list:
			if(a.check_out_by == b):
				check_out_date = a.check_out_date
				today = datetime.date.today()
				delta = today - check_out_date
				num_days = delta.days
				diff = math.floor(num_days/14)*3
				final_list.append(b)
				amount_due_list.append(diff)
				output = output + "Student Name: "+str(b)+" and AmountDue: $"+str(diff)+"    ---    "
		for b in parents_list:
			if(a.check_out_by == b):
                		check_out_date = a.check_out_date
                		today = datetime.date.today()
                		delta = today - check_out_date
				num_days = delta.days
                		diff = math.floor(num_days/14)*3
                		final_list.append(b)
                		amount_due_list.append(diff)
				output = output + "Parent Name: "+str(b)+" and AmountDue: $"+str(diff)+"    ---    "

	return HttpResponse(output)
