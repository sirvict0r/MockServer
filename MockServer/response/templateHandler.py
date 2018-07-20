from response.requestHandler import RequestHandler

class JsonHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.contentType = 'application/json'

    def find(self, routeData):
        try:
            jsonfile = open('json/{}'.format(routeData['json']))
            self.contents = jsonfile
            self.setStatus(200)
            return True
        except:
            self.setStatus(403)
            return False

