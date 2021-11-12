# Course: CST 205
# Date:
# Name:
# Final Project Teammates:
# Team Number:
# Description:

from random import shuffle, choice, sample

from flask import Flask, render_template

from PIL import Image
from flask_bootstrap import Bootstrap
from image_info import image_info

app = Flask(__name__)

# https://bootstrap-flask.readthedocs.io/en/stable/basic.html#starter-template
bootstrap = Bootstrap(app)


def select_random_items(lst):
    shuffle(lst)  # Delete if not needed

    # Long way:
    # random_image_ids = []
    # for i in range(3):
    #     random_image_ids.append(choice(lst))

    # https://www.w3schools.com/python/ref_random_sample.asp
    # sample() returns a list of random items from a list
    # Best Way:
    random_image_ids = sample(image_info, 3)

    return random_image_ids


@app.route('/')
def index():
    return render_template("index.html", random_images=select_random_items(image_info))


# https://www.geeksforgeeks.org/python-get-values-of-particular-key-in-list-of-dictionaries/
# https://appdividend.com/2019/11/16/how-to-find-element-in-list-in-python/
@app.route('/picture/<string:image_id>')
def image_page(image_id: str):
    # Create a list of image ids
    image_info_ids = [image_id['id'] for image_id in image_info]

    # Finds the index of the current image id
    image_index = image_info_ids.index(image_id)

    # Opens image to get information
    current_image_pillow_info = Image.open(f"static/images/{image_id}.jpg")

    return render_template("image_page.html", image=image_info[image_index],
                           current_image_pillow_info=current_image_pillow_info)
