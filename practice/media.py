#!/usr/bin/python
import webbrowser
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_media):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_media_url = trailer_media

    def show_trailer(self):
        webbrowser.open(self.trailer_media_url)

