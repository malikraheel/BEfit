from django.apps import AppConfig


class GymConfig(AppConfig):
    name = 'gym'

# ------- only one time run the function when program run first time ----------------
    def ready(self):
        import gym.mysignal
