import colorama
class Movie:
    def __init__(self, title, duration, rating) -> None:
        self.title = title
        self.duration = duration
        self.rating = rating
        
    def increase_duration(self, minutes):
        self.duration += minutes
        if self.duration > 150:
            self.rating -= 0.5
            print(f"{colorama.Fore.RED}Bad news{colorama.Style.RESET_ALL}: The reting of {self.title} is dicreased to {colorama.Fore.RED}{self.rating}")
    

movie1 = Movie("Avatar", 124, 7.0)
movie2 = Movie("Home Alone", 100, 10.0)
movie3 = Movie("Matrix", 139, 8.0)

movies = [movie1, movie2, movie3]

for movie in movies:
    movie.increase_duration(20)