import HTTPActivity

class OnePageWikiActivity(httpactivity.HTTPActivity):
    def __init__(self, handle):
        httpactivity.HTTPActivity.__init__(self, handle)
        self.set_title('OnePageWiki')

