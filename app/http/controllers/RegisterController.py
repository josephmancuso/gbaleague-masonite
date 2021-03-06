''' A Module Description '''
from masonite.view import view
from masonite.facades.Auth import Auth
from config import application
from config import auth
import bcrypt


class RegisterController(object):
    ''' Class Docstring Description '''

    def __init__(self):
        pass

    def show(self, Request, View):
        ''' Show the registration page '''
        return View('auth/register', {'app': application, 'Auth': Auth(Request)})

    def store(self, Request):
        ''' Register a new user '''
        # register the user
        password = bcrypt.hashpw(
                bytes(Request.input('password'), 'utf-8'), bcrypt.gensalt()
            )

        auth.AUTH['model'].create(
            name=Request.input('name'),
            password=password,
            email=Request.input('email'),
        )

        # login the user
        # redirect to the homepage
        if Auth(Request).login(Request.input(auth.AUTH['model'].__auth__), Request.input('password')):
            return Request.redirect('/home')

        return Request.redirect('/register')
