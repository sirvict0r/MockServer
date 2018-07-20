import os

from response.requestHandler import RequestHandler


class StaticHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.filetypes = {
            ".js": "text/javascript",
            ".css": "text/css",
            ".jpg": "image/jpeg",
            ".png": "image/png",
            ".json": "application/json",
            "notfound": "application/json",
        }

    def find(self, file_path):
        split_path = os.path.splitext(file_path)
        extension = split_path[1]

        try:
            print("public{}".format(file_path))

            if extension in (".json",".jpg", ".jpeg", ".png"):
                self.contents = open("public{}".format(file_path), 'rb')
            else:
                self.contents = open("public{}".format(file_path), 'r')

            self.setContentType(extension)
            self.setStatus(200)
            return True
        except:
            self.setContentType('forbidden')
            self.setStatus(403)
            return False

    def setContentType(self, ext):
        self.contentType = self.filetypes[ext]
