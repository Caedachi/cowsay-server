import argparse
import cherrypy

from server import CowsayServer


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='moo')
    parser.add_argument('--file', type=str, required=True, help='phrases file')
    parser.add_argument('--port', type=int, required=False, default=8080, help='port to bind to')

    args = parser.parse_args()

    cherrypy.config.update({'server.socket_port': args.port})

    cherrypy.quickstart(CowsayServer(args.file))
