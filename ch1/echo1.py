import sys
import rx

argv = rx.from_(sys.argv[1:])

argv.subscribe(
    on_next=lambda i: print("on_next: {}".format(i)),
    on_error=lambda e: print("on_error: {}".format(e)),
    on_completed=lambda: print("on_completed")
)
print('done')
