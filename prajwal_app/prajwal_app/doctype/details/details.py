# Copyright (c) 2023, Prajwal and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import now
from frappe.model.document import Document

class Details(Document):
	def calculate_age(self):
		if self.dob:
        	today = frappe.utils.today()
        	age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        	self.age = age
