import asyncio


def work_callback(result, loop):
    print('ending loop for result: {}'.format(result))
    loop.stop()
    
def do_some_work(x, y, cb, loop):
    r = x + y
    loop.call_later(3, cb, r, loop)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_soon(do_some_work, 2, 3, work_callback, loop)
    jobs = loop.run_forever()