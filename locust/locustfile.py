from locust import HttpUser, task, between

class WordpressUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def view_homepage(self):
        self.client.get("/")

    @task(1)
    def view_post(self):
        self.client.get("/?p=1")
