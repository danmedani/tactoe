from twisted.web import server, resource
from twisted.internet import reactor, endpoints

boardSize = 4

class Game(resource.Resource):
  isLeaf = True
  board = [[[None for x in xrange(boardSize)] for y in xrange(boardSize)] for z in xrange(boardSize)]

  def render_GET(self, request):
    # self.numberRequests += 1
    print self.board
    print request
    request.setHeader(b"content-type", b"text/plain")
    content = u"I am request #{}\n".format(self.board)
    return content.encode("ascii")

endpoints.serverFromString(reactor, "tcp:8080").listen(server.Site(Game()))
reactor.run()

