from locust import HttpUser, task, between

class MyWebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def visit_homepage(self):
        self.client.get("/")
