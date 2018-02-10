#this is main file where we create the instances of Movie class
#and run the file to view the movie website page
# we have to import media and fresh_tomatoes python files
import media
import fresh_tomatoes

#below are various instances (alaska,bfg,starwar,american_sniper,
#now_you_can_see_me,the_secret_life_of_pets) of movie class



thor = media.Movie("Thor Ragnarok",
                        "130 minutes",
                        "180p",
                        "Ragnarok is a 2017 American superhero film based on the Marvel Comics character Thor",
                        "Comedy",
                        "Taika Waititi",
                        "https://cdn.images.express.co.uk/img/dynamic/36/590x/thor-ragnarok-end-credits-avengers-infinity-war-870508.jpg",
                        "https://www.youtube.com/watch?v=ue80QwXMRHg",
                        "R")

wonder_woman = media.Movie("Wonder Women",
                            "141 minutes",
                            "180p",
                            "Wonder Woman is a 2017 American superhero film based on the DC Comics character of the same name, distributed by Warner Bros.",
                            "Action",
                            "Patty Jenkins",
                            "http://www.atoupeira.com.br/wp-content/uploads/2017/09/Capa_Mulher-Maravilha_Looke.jpg",
                            "https://www.youtube.com/watch?v=VSB4wGIdDwo",
                            "RG")

logan = media.Movie("Logan",
                    "137 minutes",
                    "180p",
                    "Logan is a 2017 American superhero film, produced by Marvel Entertainment",
                    "Action",
                    "James Mangold",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo",
                    "U/Z")

justice_league = media.Movie("Justice League",
	                        "120 minutes",
                    		"180p",
                            "Justice League is a 2017 American superhero film based on the DC Comics ",
                        	"Action",
                            "Zack Snyder",
                        	"https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",
                        	"https://www.youtube.com/watch?v=3cxixDgHUYw",
                        	"F")
jumanji = media.Movie("Jumanji - Welcome to the Jungle",
						"119 minutes",
                    	"180p",
                    	"Jumanji: Welcome to the Jungle is a 2017 American comedy ",
                        "Comedy",
                        "Jake Kasdan",
                        "https://upload.wikimedia.org/wikipedia/en/d/dc/Jumanji_Welcome_to_the_Jungle.png",
                        "https://www.youtube.com/watch?v=2QKg5SZ_35I",
                        "E")

baby_driver = media.Movie("Baby Driver",
						"113 minutes",
                        "180p",
                        "Baby Driver is a 2017 action crime film written and directed by Edgar Wright",
                        "Action",
                        "Edgar Wright",
                        "https://upload.wikimedia.org/wikipedia/en/8/8e/Baby_Driver_poster.jpg",
                        "https://www.youtube.com/watch?v=z2z857RSfhk",
                        "E")


# we create a list of instances of movie class and assign it to movies variable
movies = [thor,wonder_woman,logan,justice_league,jumanji,baby_driver]

# calling open_movies_page method to view movie website
# input is  list of all the instances
fresh_tomatoes.open_movies_page(movies)

# print media.Movie.show_image.__doc__
#(above line is one example how to read the documentation of
#function of Movie class)
