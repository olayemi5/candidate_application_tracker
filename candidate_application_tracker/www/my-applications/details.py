import frappe

no_cache = 1


def get_context(context):
    if frappe.session.user == "Guest":
        frappe.throw("Please log in to view your applications.", frappe.AuthenticationError)
    context.no_cache = 1
