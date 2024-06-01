import asyncio

# defining our coroutine
async def custom_coroutine():
    # report a message
    print("Hello world")

# create an event loop
coro = custom_coroutine()
loop = asyncio.get_event_loop()
loop.run_until_complete(coro)