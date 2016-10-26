import fresh_tomatoes
from movie import Movie

"""Create a list of movie instances.
Then just pass this list to fresh_pomatoes and it will handle it.
"""

toy_story = Movie("Toy Story",
                  "A story of a boy and his toys that come to life",
                  "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                  "https://www.youtube.com/watch?v=vwyZH85NQC4")

baahubali2 = Movie("Baahubali 2",
		   "Baahubali: The Conclusion is an upcoming Indian epic historical fiction film directed by S. S. Rajamouli.",
		   "http://s1.dmcdn.net/MfFk3/x240-qDN.jpg",
		   "https://www.youtube.com/watch?v=5CHDp2pkvjs")

avatar = Movie("Avatar",
               "A marine on an aline planet",
               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7CuFSIrF-ahR7kDgMVIZYWkeWRfR5FvP83pi7Hel2nTt95Wlb",
               "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = Movie("School of Rock",
                       "Storyline Placeholder",
                       "http://www.gstatic.com/tv/thumb/movieposters/33094/p33094_p_v8_aa.jpg",
                       "https://www.youtube.com/watch?v=WG772T5KNXc")

lolita = Movie("Lolita",
               "Storyline Placeholder",
               "https://a2ua.com/lolita/lolita-003.jpg",
               "https://www.youtube.com/watch?v=i_sGVSzN4lg")

godfather = Movie("God Father",
                  "Storyline Placeholder",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS83DS6ks2W7qKJdT0J7a6Pp9UQl_KyjeIKkKpogeZo3ofnpXKKAARhApTz",
                  "https://www.youtube.com/watch?v=lr9XAu2bH_Y")

list_to_play = [toy_story, baahubali2, avatar, school_of_rock, lolita, godfather]

fresh_tomatoes.open_movies_page(list_to_play)
