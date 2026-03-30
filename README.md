### Candidate Application Tracker

A Frappe app that gives job candidates a self-service portal to log in and track the status of their applications submitted via Frappe HRMS.

### Installation

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app candidate_application_tracker
```

### How It Works

- Candidates who applied via HRMS Job Opening can log in to the website portal
- They see a dashboard at `/my-applications` listing all their submissions
- Each row shows the job title, status, and date applied
- Clicking a row shows full details including evaluation score (if resume_evaluator is installed)

### License

MIT
