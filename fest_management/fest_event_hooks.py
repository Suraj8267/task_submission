import frappe

def validate_fest_event(doc, method=None):
    if doc.capacity is not None and doc.capacity <= 0:
        frappe.throw("Capacity must be greater than zero.")
def log_new_fest_event(doc, method=None):
    frappe.logger("fest_management").info(
        f"New Fest Event created: {doc.name}"
    )
