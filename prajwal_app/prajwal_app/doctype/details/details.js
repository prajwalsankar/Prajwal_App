// Copyright (c) 2023, Prajwal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Details', {
	refresh: function(frm) {
		frappe.msgprint("Hi Everyone")
		frm.doc.full_name = frm.doc.first_name+" "+frm.doc.last_name 
	}
});
