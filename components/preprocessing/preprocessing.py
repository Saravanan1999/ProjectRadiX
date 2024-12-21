import random
import os

def preprocessing_op(env: str = "Local"):
    """
    A simple preprocessing function that just prints a random integer
    and the environment.
    """
    print(f"[Preprocessing] ENV: {env}")
    print(f"[Preprocessing] Random integer: {random.randint(1, 100)}")
