import argparse
import cherrypy

from server import CowsayServer


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='moo')
    parser.add_argument('--file', type=str, required=True, help='phrases file')

    args = parser.parse_args()

    cherrypy.quickstart(CowsayServer(args.file))
