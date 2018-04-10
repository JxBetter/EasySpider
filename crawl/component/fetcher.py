'''
async fetcher,a component of framework,gather context from urls

@Version:0.1
@Author:jx
'''
import time
import queue
import asyncio
import aiohttp
from utils.logging import log


class AsyncFetcher:
    def __init__(self, *args):
        '''
        :param urls: init urls
        '''
        self.fetchqueue = queue.Queue()
        for i in args:
            print(i)
            self.fetchqueue.put(i)
        self.context = []
        self.coros = []
        self.tasks = []

    async def fetch(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                start = time.time()
                resp_test = await resp.text()
                end = time.time()
                self.context.append(resp_test)
                log('{} runs {}ms'.format(url, 1000 * (end - start)))
                print(resp_test)
                return resp_test

    def run(self):
        '''
        init coroutines
        :return: True if init successfully
        '''
        while not self.fetchqueue.empty():
            self.coros.append(self.fetch(self.fetchqueue.get()))
        for i in range(len(self.coros)):
            self.tasks.append(asyncio.ensure_future(self.coros[i]))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(self.tasks))
        loop.close()
        return True
