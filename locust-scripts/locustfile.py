from locust import HttpUser, TaskSet, task, between

class UserTasks(TaskSet):
    
    @task(1)
    def cenario_1(self):
        # Cenário 1: Blog post com uma imagem de aproximadamente 1mb
        self.client.get("/?p=10") # Lembre-se de alterar para o ID real

    @task(1)
    def cenario_2(self):
        # Cenário 2: Blog post com um texto de aproximadamente 400kb
        self.client.get("/?p=11") # Lembre-se de alterar para o ID real

    @task(1)
    def cenario_3(self):
        # Cenário 3: Blog post com uma imagem de 300kb
        self.client.get("/?p=12") # Lembre-se de alterar para o ID real

class WebsiteUser(HttpUser):
    tasks = [UserTasks]
    # O between(1, 3) equivale ao antigo min_wait=1000 e max_wait=3000 milissegundos
    wait_time = between(1, 3)