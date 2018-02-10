''' A Module Description '''
from masonite.view import view
from masonite.facades.Auth import Auth
from config import application


class LoginController(object):
    ''' Class Docstring Description '''

    def __init__(self):
        pass

    def show(self, Request, View):
        ''' Return the login page '''
        return View('auth/login', {'app': application, 'Auth': Auth(Request)})

    def store(self, Request):
        if Auth(Request).login(Request.input('username'), Request.input('password')):
            Request.redirect('/home')
        else:
            Request.redirect('/login')
        return 'check terminal'

    def logout(self, Request):
        Auth(Request).logout()
        return Request.redirect('/login')
