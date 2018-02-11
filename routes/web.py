''' Web Routes '''
from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('home'),
    Get().route('/league/@id', 'LeagueController@show').name('league'),
    Get().route('/league/@id/teams', 'LeagueController@teams').name('league-teams'),
    Get().route('/league/@id/draft', 'DraftController@show').name('league-draft'),
    Post().route('/league/@id/draft', 'DraftController@draft'),
]

# Authentication Routes
ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show'),
    Get().route('/logout', 'LoginController@logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show'),
    Post().route('/register', 'RegisterController@store'),
    Get().route('/home', 'HomeController@show').middleware('auth'),
]
