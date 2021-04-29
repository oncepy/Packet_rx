import rx
from rx import operators as ops
from random import randint


three_emissions = rx.range(0, 3)

three_emissions_ints = three_emissions.pipe(
    ops.map(lambda i: randint(1, 10000)),
    ops.publish()
)

three_emissions_ints.subscribe(lambda s: print("Subscriber 1: {0}".format(s)))
three_emissions_ints.subscribe(lambda s: print("Subscriber 2: {0}".format(s)))

three_emissions_ints.connect()

# publish 이전에 랜덤 숫자를 생성하고 두 Subscriber 에 공유 한다.
