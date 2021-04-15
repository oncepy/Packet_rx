import datetime
import asyncio

async def wait(id, delay):
    now = datetime.datetime.now()
    print('[id={}] wait for start {}'.format(id, now))
    await asyncio.sleep(delay)
    now = datetime.datetime.now()
    print('[id={}] wait for end {}'.format(id, now))
    return True

loop = asyncio.get_event_loop()
# loop.run_until_complete(wait(2))

loop.run_until_complete(asyncio.gather(
    wait('A', 2),
    wait('B', 1)
))

loop.close()

