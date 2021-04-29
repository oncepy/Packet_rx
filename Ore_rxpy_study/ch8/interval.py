import rx
import time


source = rx.interval(1.0)

source.subscribe(lambda s: print("Subscriber 1: {0}".format(s)))

# sleep 5 seconds, then add another subscriber
time.sleep(5)
source.subscribe(lambda s: print("Subscriber 2: {0}".format(s)))

input("Press any key to exit\n")

# 2번 subscriber 는 0 부터 수신한다. 즉, interval 은 cold observable 이다.


