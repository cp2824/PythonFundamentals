"""
media.py
    class movie
        __init__
        title
        storyline
        poster_image (wiki)
        trailer_youtube_url
        def show_trailer
"""
import webbrowser
import fresh_tomatoes

class movie:
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self._title = title
        self._storyline = storyline
        self._poster_image_url = poster_image_url
        self._trailer_youtube_url = trailer_youtube_url


    def show_trailer(self):
        webbrowser.open(self._trailer_youtube_url)


def main():
    movies = []
    Harry_Potter1 = movie("Harry Potter And The Sorcerer's Stone",
              "a boy who learns on his eleventh birthday that he is the orphaned son of two powerful wizards",
              "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Philosopher%27s_Stone_(film)#/media/File:Harry_Potter_and_the_Philosopher%27s_Stone_posters.JPG",
              "https://www.youtube.com/watch?v=vkHWWZATCQ8")
    #Harry_Potter.show_trailer()
    Harry_Potter3 = movie("Harry Potter And The Prisoner of Azkaban",
                          "fighting werewolves and animagus",
                          "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Prisoner_of_Azkaban_(film)#/media/File:Prisoner_of_azkaban_UK_poster.jpg",
                          "https://www.youtube.com/watch?v=d38qpnv8xOk")
    Harry_Potter2 = movie("Harry Potter And The Chamber of Secrets",
                          "Voldemort's back in a blast from the past",
                          "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Chamber_of_Secrets_(film)#/media/File:Harry_Potter_and_the_Chamber_of_Secrets_movie.jpg",
                          "https://www.youtube.com/watch?v=q_V45YQ-EaA")
    Harry_Potter4 = movie("Harry Potter And The Goblet of Fire",
                          "Harry fights his way to the center of a maze to visit Voldemort and friends",
                          "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Goblet_of_Fire_(film)#/media/File:Harry_Potter_and_the_Goblet_of_Fire_Poster.jpg",
                          "https://www.youtube.com/watch?v=7lJ6Suyp1ok")

    movies.append(Harry_Potter1)
    movies.append(Harry_Potter3)
    movies.append(Harry_Potter4)
    movies.append(Harry_Potter2)

    # Test it
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()