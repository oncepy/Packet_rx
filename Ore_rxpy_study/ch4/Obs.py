import rx
from rx.core import Observer

letters = rx.from_(['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon'])


class MySubscriber(Observer):

    def on_next(self, value):
        print(value)

    def on_error(self, error):
        print(error)

    def on_completed(self):
        print("completed !!")


letters.subscribe(MySubscriber())




