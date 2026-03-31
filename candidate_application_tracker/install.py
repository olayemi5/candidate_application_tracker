import frappe


def after_install():
    """Ensure Job Applicant is accessible via portal for website users."""
    _ensure_webview_permission()
    frappe.db.commit()


def _ensure_webview_permission():
    """Add 'Website User' read permission to Job Applicant if missing."""
    role = "Website User"
    if not frappe.db.exists("Role", role):
        frappe.get_doc({"doctype": "Role", "role_name": role, "desk_access": 0}).insert(ignore_permissions=True)

    if frappe.db.exists("Custom DocPerm", {"parent": "Job Applicant", "role": role, "permlevel": 0}):
        return

    frappe.get_doc({
        "doctype": "Custom DocPerm",
        "parent": "Job Applicant",
        "parenttype": "DocType",
        "parentfield": "permissions",
        "role": role,
        "read": 1,
        "write": 0,
        "create": 0,
        "delete": 0,
        "permlevel": 0,
    }).insert(ignore_permissions=True)
