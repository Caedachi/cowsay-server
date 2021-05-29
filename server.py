import cherrypy

from random import choice
from helpers import cowsay, load_phrases


class CowsayServer:
    def __init__(self, filename: str):
        self.filename = filename

    @cherrypy.expose
    def cowsay(self):
        phrases = load_phrases(self.filename)
        random_phrase = choice(phrases)

        return cowsay(random_phrase)
