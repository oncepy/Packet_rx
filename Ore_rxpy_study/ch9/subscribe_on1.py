
import random
import time
from threading import current_thread
import rx
from rx import operators as ops


def intense_calculation(value):
    # sleep for a random short duration between 0.5 to 2.0 seconds
    # to simulate a long-running calculation
    time.sleep(random.randint(5, 20) * .1)
    return value


# Create TASK 1
rx.from_(
    ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
).pipe(
    ops.map(lambda s: intense_calculation(s))
).subscribe(
    on_next=lambda s: print("TASK 1: {0} {1}".format(current_thread().name, s)),
    on_error=lambda e: print(e),
    on_completed=lambda: print("TASK 1 done!")
)

# Create TASK 2
rx.range(1, 10).pipe(
    ops.map(lambda s: intense_calculation(s))
).subscribe(
    on_next=lambda i: print("TASK 2: {0} {1}".format(current_thread().name, i)),
    on_error=lambda e: print(e),
    on_completed=lambda: print("TASK 2 done!")
)

input("Press any key to exit\n")
