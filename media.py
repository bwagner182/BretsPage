import webbrowser

class Movie(): #take details about the movie and create an instance with the details set
        def __init__ (self, movie_title, release_year, cast, movie_storyline, poster_image, trailer):
            self.title = movie_title
            self.year = release_year
            self.cast = cast
            self.storyline = movie_storyline
            self.trailer = trailer
            self.poster = poster_image
            
        def show_trailer(self): ###open the movie trailer when the poster is clicked on
            webbrowser.open(self.trailer)
            