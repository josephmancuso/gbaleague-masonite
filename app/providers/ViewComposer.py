''' A ViewCompoer Service Provider '''
from masonite.provider import ServiceProvider

class ViewComposer(ServiceProvider):

    wsgi = False

    def register(self):
        pass

    def boot(self, ViewClass, Request):
        ViewClass.share({'request': Request})
