''' A Module Description '''
from masonite.request import Request

class WelcomeController(object):
    ''' Controller for welcoming the user '''

    def __init__(self):
        pass

    def show(self):
        ''' Show Welcome Template '''
        return view('index')
