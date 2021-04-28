import rx
from rx import operators as ops

# Observable 내에 3개의 Observable 이 있다.
observables = rx.of(
    rx.of(0, 1),
    rx.of('a', 'b', 'c'),
    rx.of(3, 4, 5),
)

# concat의 성질처럼 순서적으로 표시 된다.



