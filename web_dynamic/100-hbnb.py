#!/usr/bin/python3
"""
script that starts a Flask web application:
"""
import uuid
from flask import Flask, render_template
from models import storage

# setting up flask
app = Flask(__name__)
app.url_map.strict_slashes = False
host = '0.0.0.0'
port = 5000


# page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """ calls .close() after each request"""
    storage.close()


@app.route('/100-hbnb')
def hbnb_filters():
    """ Renders template with states, cities, amenities, and places """
    state_objs = storage.all('State').values()
    all_states = dict([state.name, state] for state in state_objs)
    all_amenities = storage.all('Amenity').values()
    all_places = storage.all('Place').values()
    all_users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('0-hbnb.html',
                           cache_id=uuid.uuid4(),
                           states=all_states,
                           amenities=all_amenities,
                           places=all_places,
                           users=all_users)


if __name__ == "__main__":
    """ Run the Flask application """
    app.run(host=host, port=port)
