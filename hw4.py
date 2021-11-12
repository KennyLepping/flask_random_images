# Course: CST 205
# Date:
# Name:
# Final Project Teammates:
# Team Number:
# Description:

# You can delete the links they are just there to help you understand the code

from random import shuffle, choice, sample

from flask import Flask, render_template

from PIL import Image
from flask_bootstrap import Bootstrap
from image_info import image_info

app = Flask(__name__)

# https://bootstrap-flask.readthedocs.io/en/stable/basic.html#starter-template
bootstrap = Bootstrap(app)


def select_random_items(list_to_randomize):
    # Randomize the order of the list
    shuffle(list_to_randomize)

    # https://stackoverflow.com/questions/6494508/how-do-you-pick-x-number-of-unique-numbers-from-a-list-in-python
    # :3 is explained here: https://www.tutorialspoint.com/python3/python_lists.htm
    random_image_ids = list_to_randomize[:3]

    # https://www.w3schools.com/python/ref_random_sample.asp
    # sample() returns a list of random items from a list (This is technically more correct)
    # random_image_ids = sample(image_info, 3)

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
