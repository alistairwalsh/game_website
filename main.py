from flask import Flask, render_template, request, flash
from flask_wtf import Form
from wtforms import IntegerField, SubmitField, validators, ValidationError
from random import randint

app = Flask(__name__)
app.secret_key = 'development key'

Answer = randint(1,100)
class GameForm(Form):
   response_string = "Let's play!"
   Guess = IntegerField("guess")
   submit = SubmitField("Submit")


@app.route('/game', methods = ['GET', 'POST'])
def game():
   form = GameForm()
   global Answer
   
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         return render_template('game.html', form = form, Answer = Answer)
      if form.Guess.data == Answer:
         form.response_string = "That's it!"
         Answer = randint(1,100)
         return render_template('success.html',form = form)
      elif form.Guess.data < Answer:
         form.response_string = "My number is higher than that!!"
         return render_template('game.html',form = form, Answer = Answer)
      elif form.Guess.data > Answer:
         form.response_string = "My number is lower than that!!"
         return render_template('game.html',form = form, Answer = Answer)

   elif request.method == 'GET':
      return render_template('game.html', form = form, Answer = Answer)

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)