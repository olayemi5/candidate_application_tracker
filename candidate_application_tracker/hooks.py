app_name = "candidate_application_tracker"
app_title = "Candidate Application Tracker"
app_publisher = "Stephen Olayemi"
app_description = "Portal for candidates to track their job applications on Frappe HRMS"
app_email = "olayemistephen007@gmail.com"
app_license = "mit"

required_apps = ["hrms"]

# Portal menu item so candidates see "My Applications" in the portal sidebar
website_route_rules = [
    {"from_route": "/my-applications/<name>", "to_route": "my-applications/details"},
]

# Add portal menu entry
portal_menu_items = [
    {"title": "My Applications", "route": "/my-applications", "role": "All"},
]

# Allow website users to read their own Job Applicant records
has_website_permission = {
    "Job Applicant": "candidate_application_tracker.permissions.has_website_permission",
}

after_install = "candidate_application_tracker.install.after_install"
