from locust import HttpUser, task, between

class WordpressUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def view_homepage(self):
        response = self.client.get("/")
        print("Upstream backend:", response.headers.get("X-Upstream"))

    @task(1)
    def view_post(self):
        response = self.client.get("/?p=1")
        print("Upstream backend:", response.headers.get("X-Upstream"))
