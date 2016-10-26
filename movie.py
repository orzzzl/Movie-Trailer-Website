
from video import Video

class Movie(Video):
    """This is the class specify a movie which is to be used on the website"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, movie_title, poster_image, trailer_youtube)
        self.storyline = movie_storyline
