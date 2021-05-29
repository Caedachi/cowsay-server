# cowsay-server
```
 _________________________________________
/ ANY SUFFICIENTLY ADVANCED TECHNOLOGY IS \
| INDISTINGUISHABLE FROM MAGIC, SO THEY   |
\ SAY                                     /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

## Requirements
- Python 3
- cowsay

## Dependencies
- cherrypy

## Usage
`python3 main.py --file FILE`

Where `FILE` is the file containing the phrases to use. The file should have one phrase per line.

Use `GET` requests to `http://localhost:8080/cowsay` to get a phrase:

```
$ curl http://localhost:8080/cowsay
 _______
< HELLO >
 -------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

```