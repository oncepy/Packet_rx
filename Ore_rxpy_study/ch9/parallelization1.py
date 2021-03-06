import rx
from rx import operators as ops
from rx.scheduler import ThreadPoolScheduler
from threading import current_thread
import multiprocessing
import random
import time


def intense_calculation(value):
    # sleep for a random short duration between 0.5 to 2.0 seconds
    # to simulate a long-running calculation
    time.sleep(random.randint(5, 20) * .1)
    return value


rx.from_(
    ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa"]
).pipe(
    ops.map(lambda s: intense_calculation(s))
).subscribe(
    on_next=lambda i: print("{0} {1}".format(current_thread().name, i)),
    on_error=lambda e: print(e),
    on_completed=lambda: print("TASK 1 done!")
)

input("Press any key to exit\n")

