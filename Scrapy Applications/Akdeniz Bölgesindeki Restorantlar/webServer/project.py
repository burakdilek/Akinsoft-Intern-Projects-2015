# -*- coding: utf-8 -*-
import web
import json
urls = (
    '/', 'index'
)
render = web.template.render("templates")

data = []
with open('..\EgeRestorantScrap\items.jsonlines') as f:
    for line in f:
        line = line.decode("utf-8-sig")
        data.append(json.loads(line))
class index:
    def GET(self):
       return render.index(data)

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), ("localhost", 12345))