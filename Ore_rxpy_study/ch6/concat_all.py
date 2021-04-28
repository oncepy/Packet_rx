import rx
from rx import operators as ops

items = ["134/34/235/132/77", "64/22/98/112/86/11", "66/08/34/778/22/12"]

# RxPy v3.0 에서 부터 concat_all() 이 없어지고 merge 연산을 사용하고 max_concurrent 아규먼트를 1로 설정하도록 변경되었다.

rx.from_(items).pipe(
    ops.map(lambda s: rx.from_(s.split("/"))),
    ops.merge(max_concurrent=1),
    ops.map(lambda s: int(s))
).subscribe(
    lambda i: print(i)
)




