import HTTPActivity

class OnePageWikiActivity(HTTPActivity.HTTPActivity):
    def __init__(self, handle):
        HTTPActivity.HTTPActivity.__init__(self, handle)
        self.set_title('OnePageWiki')

