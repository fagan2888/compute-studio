import os
import requests
import json
from requests.exceptions import RequestException, Timeout
import requests_mock

requests_mock.Mocker.TEST_PREFIX = "test"

WORKER_HN = os.environ.get("WORKERS")
TIMEOUT_IN_SECONDS = 1.7
MAX_ATTEMPTS_SUBMIT_JOB = 4


class JobFailError(Exception):
    """An Exception to raise when a remote jobs has failed"""


class WorkersUnreachableError(Exception):
    """
    An Exception to raise when the backend workers are not reachable. This
    should only be raised when the webapp is run without the workers.
    """


class Compute(object):
    def remote_submit_job(
        self, url: str, data: dict, timeout: int = TIMEOUT_IN_SECONDS, headers=None
    ):
        response = requests.post(url, json=data, timeout=timeout)
        return response

    def remote_query_job(self, theurl):
        job_response = requests.get(theurl)
        return job_response

    def remote_get_job(self, theurl):
        job_response = requests.get(theurl)
        return job_response

    def submit_job(self, project, task_name, task_kwargs, tag=None):
        print("submitting", task_name)
        url = f"http://{WORKER_HN}/{project.owner}/{project.title}/"
        return self.submit(
            tasks=dict(task_name=task_name, tag=tag, task_kwargs=task_kwargs), url=url
        )

    def submit(self, tasks, url):
        submitted = False
        attempts = 0
        while not submitted:
            try:
                response = self.remote_submit_job(
                    url, data=tasks, timeout=TIMEOUT_IN_SECONDS
                )
                if response.status_code == 200:
                    print("submitted: ", url)
                    submitted = True
                    data = response.json()
                    job_id = data["task_id"]
                else:
                    print("FAILED: ", WORKER_HN)
                    attempts += 1
            except Timeout:
                print("Couldn't submit to: ", WORKER_HN)
                attempts += 1
            except RequestException as re:
                print("Something unexpected happened: ", re)
                attempts += 1
            if attempts > MAX_ATTEMPTS_SUBMIT_JOB:
                print("Exceeded max attempts. Bailing out.")
                raise WorkersUnreachableError()

        return job_id


class SyncCompute(Compute):
    def submit(self, tasks, url):
        submitted = False
        attempts = 0
        while not submitted:
            try:
                response = self.remote_submit_job(
                    url, data=tasks, timeout=TIMEOUT_IN_SECONDS
                )
                if response.status_code == 200:
                    print("submitted: ", url)
                    submitted = True
                    if not response.text:
                        return
                    data = response.json()
                else:
                    print("FAILED: ", WORKER_HN, response.status_code)
                    attempts += 1
            except Timeout:
                print("Couldn't submit to: ", WORKER_HN)
                attempts += 1
            except RequestException as re:
                print("Something unexpected happened: ", re)
                attempts += 1
            if attempts > MAX_ATTEMPTS_SUBMIT_JOB:
                print("Exceeded max attempts. Bailing out.")
                raise WorkersUnreachableError()

        success = data["status"] == "SUCCESS"
        if success:
            return success, data
        else:
            return success, data


class SyncProjects(SyncCompute):
    def submit_job(self, projects):
        url = f"http://{WORKER_HN}/sync/"
        return self.submit(tasks=projects, url=url)
