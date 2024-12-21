import random
import os

def training_op(env: str = "Local"):
    """
    A simple training function that just prints a random integer
    and the environment.
    """
    print(f"[Training] ENV: {env}")
    print(f"[Training] Random integer: {random.randint(1, 100)}")
