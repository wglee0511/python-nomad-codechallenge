"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
from stackoverjobs import stack_over_init
from weworkremotely import wework_init
from remoteok import remoteok_init

keyword_for_getting_jobs = "python"

stack_over_init(keyword_for_getting_jobs)
wework_init(keyword_for_getting_jobs)
remoteok_init(keyword_for_getting_jobs)
