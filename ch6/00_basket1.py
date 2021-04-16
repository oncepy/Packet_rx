import rx
import rx.operators as ops

obs = rx.from_([
    {
        'count': 5,
        'what': 'apple'
    },
    {
        'count': 3,
        'what': 'orange'
    }
]).pipe(
    ops.filter(lambda i: i['what'] == 'apple'),
    ops.map(lambda i: i['count']),
    ops.map(lambda i: {
        'count': i,
        'double': i*2
    })
)

obs.subscribe(
    on_next=lambda i: print("on_next {}".format(i)),
    on_error=lambda e: print("on_error: {}".format(e)),
    on_completed=lambda: print("on_completed")
)

