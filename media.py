import webbrowser


class Video():

    """
Video class object that provides a way to store movie related information
and will be used in the entertainment_center.py file

Attributes:
title:
It is the movie (or Tv series) title from IMDB  (http://www.imdb.com/)
storyline:
A short discription of the movie (or Tv series) from IMDB
(http://www.imdb.com/)
poster_image_url:
The URL address of a poster image of the movie (or TV series) from IMDB
(http://www.imdb.com/) or other recursos
trailer_youtube_url:
A watch link on official trailer from youtube (https://www.youtube.com)
"""


    def __init__(
            self, movie_title, movie_storyline, poster_image, trailer_youtube, imbd_id):
        """Initialises Video class and provides a way to store information"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imbd_id = imbd_id

    def show_trailer(self):
        """Plays the movie trailer in the web browser"""
        webbrowser.open(self.trailer_youtube_url, new=2, autoraise=True)
