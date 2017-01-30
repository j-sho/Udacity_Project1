import fresh_tomatoes_TVseries
import fresh_tomatoes_movies
import media

# Movies details
grease = media.Video("Grease",
					"Good girl Sandy and greaser Danny fell in love over the summer. "
					"When they unexpectedly discover they're now in the same high school,"
					" will they be able to rekindle their romance?",
					"https://images-na.ssl-images-amazon.com/images/M/"
					"MV5BMTcyMTA5MTY3MF5BMl5BanBnXkFtZTgwMTMwNzAxMDE@._V1_.jpg",
					"https://youtu.be/f2CCEixOVVU")
dirty_dancing = media.Video("Dirty Dancing",
							"Spending the summer at a Catskills resort with her family, "
							"Frances Houseman falls in love with the camp's dance instructor, "
							"Johnny Castle.",
							"https://images-na.ssl-images-amazon.com/images/M/"
							"MV5BMTc3MDY3ODQ2OV5BMl5BanBnXkFtZTgwOTQ2NTYxMTE@._V1_.jpg",
							"https://youtu.be/-Qd0vb_DMBY")
ghost = media.Video("Ghost", 
					"After a young man is murdered, his spirit stays behind to warn his "
					"lover of impending danger, with the help of a reluctant psychic.",
					"https://images-na.ssl-images-amazon.com/images/M/"
					"MV5BMTU0NzQzODUzNl5BMl5BanBnXkFtZTgwMjc5NTYxMTE@._V1_.jpg",
					"https://youtu.be/vIy3MDzPyKg")
bodyguard = media.Video("The Bodyguard",
						"A former Secret Service agent takes on the job of bodyguard"
						" to a pop singer, whose lifestyle is most unlike a President's.",
						"https://images-na.ssl-images-amazon.com/images/M/"
						"MV5BYjNhMGEwNDYtOTYxZC00NmY3LWI0ZmMtMDdmZTU2OTgzMDYwXk"
						"EyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg", 
						"https://youtu.be/LqkflVAneKg")
schindler = media.Video("Schindler's List",
						"In German-occupied Poland during World War II, Oskar Schindler "
						"gradually becomes concerned for his Jewish workforce after "
						"witnessing their persecution by the Nazi Germans.",
						"https://images-na.ssl-images-amazon.com/images/M/"
						"MV5BMzMwMTM4MDU2N15BMl5BanBnXkFtZTgwMzQ0MjMxMDE@._V1_.jpg",
						"https://youtu.be/JdRGC-w9syA")
wild = media.Video("Into the wild",
					"After graduating from Emory University, top student and athlete"
					" Christopher McCandless abandons his possessions, gives his entire"
					" $24,000 savings account to charity and hitchhikes to Alaska "
					"to live in the wilderness. Along the way, Christopher encounters "
					"a series of characters that shape his life.",
					"https://images-na.ssl-images-amazon.com/images/M/"
					"MV5BMTAwNDEyODU1MjheQTJeQWpwZ15BbWU2MDc3NDQwNw@@._V1_.jpg",
					"https://youtu.be/g7ArZ7VD-QQ")
green_mile = media.Video("The Green Mile",
						"The lives of guards on Death Row are affected by one of their charges: "
						"a black man accused of child murder and rape, yet "
						"who has a mysterious gift.",
						"https://images-na.ssl-images-amazon.com/images/M/"
						"MV5BMTUxMzQyNjA5MF5BMl5BanBnXkFtZTYwOTU2NTY3._V1_.jpg",
						"https://youtu.be/ctRK-4Vt7dA")
beautiful_mind = media.Video("A Beautiful Mind",
							"After John Nash, a brilliant but asocial mathematician, accepts "
							"secret work in cryptography, his life takes a turn for "
							"the nightmarish.",
							"https://images-na.ssl-images-amazon.com/images/M/"
							"MV5BMzcwYWFkYzktZjAzNC00OGY1LWI4YTgtNzc5MzVjMDVmNjY0XkEyXk"
							"FqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,673,1000_AL_.jpg",
							"https://youtu.be/WFJgUm7iOKw")
shawshank = media.Video("The Shawshank Redemption",
						"Two imprisoned men bond over a number of years, finding solace "
						"and eventual redemption through acts of common decency.",
						"https://images-na.ssl-images-amazon.com/images/M/"
						"MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_"
						"SY1000_CR0,0,672,1000_AL_.jpg",
						"https://youtu.be/6hB3S9bIaco")

#List of movies
movies = [grease, dirty_dancing, ghost, bodyguard, schindler, wild, green_mile,
		beautiful_mind, shawshank]
#Create HTML page with movies
fresh_tomatoes_movies.open_movies_page(movies)

#TV Series details
lost = media.Video("Lost", 
						"The survivors of a plane crash are forced to work together in order "
						"to survive on a seemingly deserted tropical island.",
						"https://images-na.ssl-images-amazon.com/images/M/"
						"MV5BMjA3NzMyMzU1MV5BMl5BanBnXkFtZTcwNjc1ODUwMg@@._V1_.jpg",
						"https://youtu.be/72kQIIDBIUU")
orange = media.Video("Orange Is the New Black",
						"The story of Piper Chapman, a woman in her thirties who is sentenced "
						"to fifteen months in prison after being convicted of a decade-old "
						"crime of transporting money to her drug-dealing girlfriend.",
						"https://images-na.ssl-images-amazon.com/images/M/"
						"MV5BMjMzMjAxNDY5MV5BMl5BanBnXkFtZTgwMzAzNTQxODE@."
						"_V1_SY1000_CR0,0,674,1000_AL_.jpg",
						"https://youtu.be/zLyUlTu4KbI")
americans = media.Video("The Americans",
							"Two Soviet intelligence agents pose as a married couple to spy on "
							"the American government.",
							"https://images-na.ssl-images-amazon.com/images/M/"
							"MV5BMjAwMzIzOTIyN15BMl5BanBnXkFtZTgwMjU0NTY3MzE@._V1_.jpg",
							"https://youtu.be/__nTeZrEtvw")
stranger_things = media.Video("Stranger Things",
								"When a young boy disappears, his mother, a police chief, and his"
								" friends must confront terrifying forces in order to get him back.",
								"https://images-na.ssl-images-amazon.com/images/M/"
								"MV5BMjEzMDAxOTUyMV5BMl5BanBnXkFtZTgwNzAxMzYzOTE@._V1_.jpg",
								"https://youtu.be/b9EkMc79ZSU")
sense8 = media.Video("Sense8",
						"A group of people around the world are suddenly linked mentally, "
						"and must find a way to survive being hunted by those who see them as "
						"a threat to the world's order.",
						"http://capitalismo.biz/wp-content/uploads/2015/09/Sense8-poster.jpg",
						"https://youtu.be/E9c_KSZ6zMk")
the_100 = media.Video("The 100",
						"Set 97 years after a nuclear war has destroyed civilization, when "
						"a spaceship housing humanity's lone survivors sends 100 juvenile "
						"delinquents back to Earth in hopes of possibly re-populating "
						"the planet.",
						"https://images-na.ssl-images-amazon.com/images/M/"
						"MV5BYWIzNDMwNGYtMjk5ZC00ZjA2LTg4ZDgtZmI5NDEzMzdkZTc5Xk"
						"EyXkFqcGdeQXVyNDExMTIxMDc@._V1_.jpg",
						"https://youtu.be/aDrsItJ_HU4")

#List of TV series
tv_series = [lost, orange, americans, stranger_things, sense8, the_100]
#Create HTML page with TV series
fresh_tomatoes_TVseries.open_movies_page(tv_series)
