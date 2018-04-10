class Spider:
    def __init__(self,fetcher,parser=None,saver=None):
        self.fetcher = fetcher
        self.parser = parser
        self.saver = saver


    def run(self):
        self.fetcher.run()
        # self.parser.run(self.fetcher.context)
        # self.saver.run()