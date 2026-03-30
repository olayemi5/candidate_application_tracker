import frappe


@frappe.whitelist()
def get_my_applications():
    """Return all Job Applicant records belonging to the logged-in user."""
    user = frappe.session.user
    if user == "Guest":
        frappe.throw("Please log in to view your applications.", frappe.AuthenticationError)

    applications = frappe.get_all(
        "Job Applicant",
        filters={"email_id": user},
        fields=["name", "applicant_name", "email_id", "job_title", "status", "creation"],
        order_by="creation desc",
    )

    for app in applications:
        if app.get("job_title"):
            app["job_title_name"] = frappe.db.get_value(
                "Job Opening", app["job_title"], "job_title"
            ) or app["job_title"]
        else:
            app["job_title_name"] = "N/A"

    return applications


@frappe.whitelist()
def get_application_detail(application_name):
    """Return detail of a single Job Applicant record for the logged-in user."""
    user = frappe.session.user
    if user == "Guest":
        frappe.throw("Please log in to view your applications.", frappe.AuthenticationError)

    doc = frappe.get_doc("Job Applicant", application_name)
    if doc.email_id != user:
        frappe.throw("You do not have permission to view this application.", frappe.PermissionError)

    job_title_name = ""
    if doc.job_title:
        job_title_name = frappe.db.get_value("Job Opening", doc.job_title, "job_title") or doc.job_title

    return {
        "name": doc.name,
        "applicant_name": doc.applicant_name,
        "email_id": doc.email_id,
        "job_title": doc.job_title,
        "job_title_name": job_title_name,
        "status": doc.status,
        "creation": doc.creation,
        "cover_letter": doc.cover_letter,
    }
