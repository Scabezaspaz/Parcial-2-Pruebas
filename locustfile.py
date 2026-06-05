from locust import HttpUser, task, between


class RecargaUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task(3)
    def recarga_valida(self):
        self.client.post("/recarga", json={
            "monto": 15000,
            "premium": False
        })

    @task(2)
    def recarga_premium(self):
        self.client.post("/recarga", json={
            "monto": 35000,
            "premium": True
        })

    @task(1)
    def recarga_minima(self):
        self.client.post("/recarga", json={
            "monto": 1000,
            "premium": False
        })