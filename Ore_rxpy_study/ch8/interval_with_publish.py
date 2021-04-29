import rx
from rx import operators as ops
import time


source = rx.interval(1.0).pipe(ops.publish())

source.subscribe(lambda s: print("Subscriber 1: {0}".format(s)))
source.connect()

# sleep 5 seconds, then add another subscriber
time.sleep(5)
source.subscribe(lambda s: print("Subscriber 2: {0}".format(s)))

input("Press any key to exit\n")

