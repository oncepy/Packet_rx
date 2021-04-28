import rx
from rx import operators as ops
import time

disposable = rx.interval(1.0).pipe(
    ops.map(lambda i: "{0} Mississippi".format(i))
).subscribe(lambda s: print(s))

# sleep 5 seconds so Observable can fire
time.sleep(5)

# disconnect the Subscriber
print("Unsubscribing!")
disposable.dispose()

# sleep a bit longer to prove no more emissions are coming
time.sleep(5)
