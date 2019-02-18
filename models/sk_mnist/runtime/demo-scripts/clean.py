import subprocess
import shlex
argo_jobs = subprocess.check_output(shlex.split('argo list'))
argo_jobs = argo_jobs.decode('utf-8')
argo_jobs = argo_jobs.splitlines()

latest_job = argo_jobs[1].split(' ')[0]
print('found process ', latest_job)
subprocess.run(shlex.split(f'argo delete {latest_job}'))
