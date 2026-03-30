import frappe


def after_install():
    """Ensure Job Applicant is accessible via portal for website users."""
    _ensure_webview_permission()
    frappe.db.commit()


def _ensure_webview_permission():
    """Add 'Website User' read permission to Job Applicant if missing."""
    exists = frappe.db.exists("Custom DocPerm", {
        "parent": "Job Applicant",
        "role": "Website User",
        "permlevel": 0,
    })
    if exists:
        return

    doc = frappe.get_doc("DocType", "Job Applicant")
    doc.append("permissions", {
        "role": "Website User",
        "read": 1,
        "write": 0,
        "create": 0,
        "delete": 0,
        "permlevel": 0,
    })
    doc.save(ignore_permissions=True)
