
#Adding imports to be able to access their functionalities
from omdb import OMDBClient
import json

#setting myself up as a client(not a server) to the API website with a valid key
API_KEY = "2dd0350e"
client = OMDBClient(apikey=API_KEY)

#this function allows me to search for a movie
def movie_lookup():
    user_title = input("Plz enter movie name")
    if user_title == "done":
        exit()
    else:
        #used below initially but edited out as i figured i'd rather use a jsn method to append data to a .json file, however this proved to be difficult as json can hold one object. I tried to make the jason file a list but this didn't work as planned
        #from there i would have added a dictionary to make the info more simple
        #i believe a json file would work better than a textfile
        
        #response = requests.get("http://www.omdbapi.com/?s="+user_title+"&apikey="+API_KEY)
        #data = response.json()
        data = client.title(user_title)
        
        with open("movies.json", 'a') as outfile:
            outfile.write(json.dumps(data, indent=4)+'\n')
        
        json_data = json.dumps(data)
        print(json_data)

#this appends the data from the searches and stores it in a list/array in a textfile that can be called upon with previous movie function
#currently not in use as i am no longer usimg the textfile and tried to rather use a json file, i kept previous txt file to show it works    
    movie_titles = []

    for title in movie_titles:
        title = user_title
        movie_titles.append(title)
        print(movie_titles)
        fhand = open("movies.txt", "a")
        fhand.write(data)
        fhand.close()

    #attempted to display "Movie not found" if a movie isnt found in the database
    #if response.status_code != 200:
        #print("Movie not found")
    #else:
    #print(data)

#opens the textfile of movies in order to display previous movies
#no longer in use as i tried to use a json file
def previous_movies():
    data = json.load(open("movies.txt"))
    #data = json.loads("Title")
    print(type(data), data)

#infinite loop that allows the program to keep going until the user enters 'done'
while True:
    user_input = input("What would you like to do?")
    if user_input == "prev":
        previous_movies()
    elif user_input == "done":
        exit()
    elif user_input == "search":
        movie_lookup()


    