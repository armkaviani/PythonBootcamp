from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(f"Secret number: {random_number}")

    
@app.route('/')
def home():
    return "<h1> Guess a number between 0 and 9 </h1>" \
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnVlaWdtMDE4ZTA1aXhrdzUyYndzZG5wYXRjOW9zZm1oZzFiN3p4cSZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/3CCXHZWV6F6O9VQ7FL/giphy.gif' width='300'>"
    

@app.route("/<int:guess>")
def guess_number(guess):
    if guess < random_number:
        return "<h1 style='color:red;'> Too low, try again! </h1>" \
                    "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width='300'>"
    elif guess > random_number:
        return "<h1 style='color:purple;'> Too high, try again! </h1>" \
                    "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='300'>"
    else:
        return "<h1 style='color:green;'> You found me! </h1>" \
                    "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width='300'>"