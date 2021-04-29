import rx
from rx import operators as ops
from random import randint


three_emissions = rx.range(0, 3)

three_emissions_ints = three_emissions.pipe(
    ops.map(lambda i: randint(1, 10000)),
    ops.publish()
)

three_emissions_ints.subscribe(lambda s: print("Subscriber 1: {0}".format(s)))
three_emissions_ints.pipe(
    ops.reduce(lambda total, item: total + item)
).subscribe(lambda s: print("Subscriber 2: {0}".format(s)))

three_emissions_ints.connect()

# Subscriber 1과 2는 같은 랜덤 데이타에 대해 다른 작업 결과를 만들어 낼 수 있다.
