import imdb
from tkinter import *
from tkinter import messagebox
global movie_name

win = Tk()
win.title("IMDB Database")
win.geometry("400x100")


label = Label(win,text="Type Movie Name Here :")
label.pack(anchor="center")

entry = Entry(win)
entry.pack(anchor="center")


def open_popup():
    top = Toplevel(win)
    top.geometry("600x200")
    top.title("Movie Information")

    moviesDB = imdb.IMDb()
    movies = moviesDB.search_movie(entry.get())
    id = movies[0].getID()
    movie = moviesDB.get_movie(id)
    Label(top , text = f"{movie['title']} - {movie['year']}").pack(anchor = "w")
    Label(top , text = f"IMDB Rating : {movie['rating']}").pack(anchor = "w")
    directors = movie['directors']
    casting = movie['cast']
    director = ''.join(map(str,directors))
    Label(top , text = f"Directors : {director}").pack(anchor = "w")
    actors = ",".join(map(str,casting[0:5]))
    Label(top , text = f"Actors: {actors}").pack(anchor = "w")

""" def detail():
    moviesDB = imdb.IMDb()
    movies = moviesDB.search_movie(entry.get())
    if(movies):
        id = movies[0].getID()
        movie = moviesDB.get_movie(id)
        messagebox.showinfo(f"{movie['title']} - {movie['year']}")
        
        print("Movie Info : ")
        print(f"{movie['title']} - {movie['year']}")
        print(f"rating : {movie['rating']}")
        directors = movie['directors']
        casting = movie['cast']
        director = ''.join(map(str,directors))
        print(f"directos : {director}")
        actors = ",".join(map(str,casting[0:5]))
        print(f"Actprs: {actors}")
        messagebox.showinfo(f"Actors: {actors}")
 """
button = Button(win,text="Search",command=open_popup)
button.pack(anchor="center")

win.mainloop()
