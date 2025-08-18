# Lecture 3 Apna college 

# WAP to ask user to enter names of their 3 favourite movies & store them in list

movies = []

# mov1 = input('Enter 1st movies:')
# mov2 = input('Enter 2nd movies:')
# mov3 = input('Enter 3rd movies:')

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)


# Method 2(Using loop)

for i in range(3):
    movie = input(f"Enter your Favorite movie {i + 1}: ")
    movies.append(movie)

print(movies)