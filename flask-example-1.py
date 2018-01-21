from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello World'


@app.route('/test/<string:name>')
def test(name):
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Whoah Dude",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- George Washington",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Abraham Lincoln"]
    randomNumber = randint(0, len(quotes) - 1)
    quote = quotes[randomNumber]

    return render_template(
        'test.html', **locals()
    )


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
