import django.shortcuts
from django.core.paginator import Paginator
from .models import JobListing  # Import the JobListing model


def main_page(request, page=1):
    # Query all job listings from the JobListing model
    job_listings = JobListing.objects.all().order_by('-job_posted_at_datetime_utc').values()

    # Get the checkbox values from the request
    location_values = request.GET.getlist("location")
    type_values = request.GET.getlist("type")
    education_values = request.GET.getlist("education")
    sort_date = request.GET.get("sort_date", "")
    sort_title = request.GET.get("sort_title", "")

    query = request.GET.get("query", "")
    if ":" in query:
        query_dict = dict(item.split(":") for item in query.split(", ") if ":" in item)
    else:
        query_dict = {"title": query}

    filters = {
        "location": lambda job, values: job["job_city"].lower() in [value.lower() for value in
                                                                    values] if values else True,
        "type": lambda job, values: job["job_employment_type"].replace(" ", "").lower() in [
            value.replace(" ", "").lower() for value in values] if values else True,
        "education": lambda job, values: any(job["job_educational_level"].get(level) == True for level in values),
        "title": lambda job, values: any(term in job["job_title"].lower() for term in values[0].lower().split()),
        "employer": lambda job, values: any(term in job["employer_name"].lower() for term in values[0].lower().split()),
    }

    if location_values:
        job_listings = [job for job in job_listings if filters["location"](job, location_values)]
    if type_values:
        job_listings = [job for job in job_listings if filters["type"](job, type_values)]
    if education_values:
        job_listings = [job for job in job_listings if filters["education"](job, education_values)]

    for filter_name, filter_func in filters.items():
        filter_values = query_dict.get(filter_name, "").split()
        if filter_values:
            job_listings = [job for job in job_listings if filter_func(job, filter_values)]

    sort_date = request.GET.get("sort_date", "")
    sort_title = request.GET.get("sort_title", "")

    sort_options = {
        "sort_date": lambda: job_listings.order_by(
            "-job_posted_at_datetime_utc" if sort_date.lower() == "desc" else "job_posted_at_datetime_utc"),
        "sort_title": lambda: job_listings.order_by("-job_title" if sort_title.lower() == "desc" else "job_title"),
    }
    for sort_name, sort_func in sort_options.items():
        sort_value = request.GET.get(sort_name, "")
        if sort_value:
            job_listings = sort_func()

    for job in job_listings:
        job["salary"] = f"{job['job_min_salary']} - {job['job_max_salary']}"

    total_jobs = len(job_listings)

    paginator = Paginator(job_listings, 10)
    page_obj = paginator.get_page(page)

    return django.shortcuts.render(
        request,
        "jobsearch/main_page.html",
        {
            "page_obj": page_obj,
            "results_count": len(job_listings),
            "total_jobs": total_jobs,
        },
    )
