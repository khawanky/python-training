current_movies = {
    'old1': '11:00pm',
    'old2': '9:00pm',
    'old3': '5:00am',
    'old4': '3:00pm'
}

print('Movies: ')
for key in current_movies:
    print(key)

movie = input('What movie would you like to watch?')
showtime = current_movies.get(movie)

if showtime == None:
    print('No movie')
else:
    print(movie, 'is playing at', showtime)
    