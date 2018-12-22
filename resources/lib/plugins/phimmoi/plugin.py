from mozie_request import Request
from phimmoi.parser.category import Parser as Category
from phimmoi.parser.channel import Parser as Channel
from phimmoi.parser.movie import Parser as Movie


class Phimmoi:
    domain = "http://www.phimmoi.net"

    def getCategory(self):
        response = Request().get(self.domain)
        return Category().get(response)

    def getChannel(self, channel, page=1):
        if page > 1:
            url = '%s/%spage-%d.html' % (self.domain, channel, page)
        else:
            url = '%s/%s' % (self.domain, channel)
        response = Request().get(url)
        return Channel().get(response, page)

    def getMovie(self, id):
        url = "%s/%sxem-phim.html" % (self.domain, id)
        response = Request().get(url)
        return Movie().get(response)

    def getLink(self, url):
        response = Request().get(url)
        return Movie().get(response, True)
