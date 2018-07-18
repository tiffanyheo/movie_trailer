import media
import fresh_tomatoes  # to make the designed web page

# make movie instances
mad_max = media.Movie("Mad Max : Fury Road",
       "Survival action in a desert after a nuclear holocaust.",
       "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
       "https://youtu.be/hEJnMQG9ev8")

atonement = media.Movie("Atonement",
       "A lier girl changes two people's life in the world war.",
       "https://upload.wikimedia.org/wikipedia/en/e/e4/Atonement_UK_poster.jpg",
       "https://youtu.be/rkVQwwPrr4c")

darkknight = media.Movie("The Dark Knight",
       "Batman against joker.",
       "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
       "https://youtu.be/EXeTwQWrcwY")

fast_and_furious = media.Movie("The Fate of the Furious",
       "The best car action movie in the world.",
       "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg",
       "https://youtu.be/9GvX2uexGkA")

avengers = media.Movie("Avengers : Infinity War",
       "The story of heros to save the world.",
       "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
       "https://youtu.be/6ZfuNTqbHE8")

interstellar = media.Movie("Interstellar",
       "Find the new earth.",
       "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
       "https://youtu.be/0vxOhd4qlnA")

secret = media.Movie("Secret",
       "Fasinating love story in music school.",
       "https://upload.wikimedia.org/wikipedia/en/thumb/c/c6/Secret-Bunengshuodemimi2.jpg/220px-Secret-Bunengshuodemimi2.jpg",
       "https://youtu.be/DTDuOkNSJA4")

you_are_the_apple = media.Movie("You Are the Apple of My Eye",
       "The pure first love.",
       "https://upload.wikimedia.org/wikipedia/en/a/aa/You_Are_the_Apple_of_My_Eye_film_poster.jpg",
       "https://youtu.be/v5H6wE47FrI")

bourne = media.Movie("The Bourne Ultimatum",
       "The story of the legandary assassination agent",
       "https://upload.wikimedia.org/wikipedia/en/b/bb/Ludlum_-_The_Bourne_Ultimatum_Coverart.png",
       "https://youtu.be/ZT2ZxjUjSo0")

# make the list of the movie instance
movies = [mad_max, atonement, darkknight, fast_and_furious, avengers, interstellar, secret, you_are_the_apple,bourne]


# open the web page to show the movie list
fresh_tomatoes.open_movies_page(movies)
