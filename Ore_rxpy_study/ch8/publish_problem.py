import rx
from rx import operators as ops
from random import randint


three_emissions = rx.range(0, 3).pipe(ops.publish())

three_emissions_ints = three_emissions.pipe(
    ops.map(lambda i: randint(1, 10000))
)

three_emissions_ints.subscribe(lambda s: print("Subscriber 1: {0}".format(s)))
three_emissions_ints.subscribe(lambda s: print("Subscriber 2: {0}".format(s)))

three_emissions.connect()

# Subscriber 1 과 2 가 다른 랜덤 숫자를 받는다.
# 같은 랜덤 숫자를 받을 수 없는가?
