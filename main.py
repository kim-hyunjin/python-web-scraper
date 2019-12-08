from indeed import extract_indeed_page_number, extract_indeed_jobs

last_indeed_page = extract_indeed_page_number()

indeed_jobs = extract_indeed_jobs(last_indeed_page)

for jobs in indeed_jobs:
    print(jobs)
    print()
