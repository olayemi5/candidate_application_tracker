import frappe


def has_website_permission(doc, ptype, user=None, verbose=False):
    """Allow website users to view only their own Job Applicant records."""
    if not user:
        user = frappe.session.user
    if user == "Guest":
        return False
    return doc.email_id == user
