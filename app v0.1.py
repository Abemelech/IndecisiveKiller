from tkinter import *
from threading import Thread
import os


window = Tk()

window.wm_title("Any Platform")
window['background'] = "#221F1F"

data = {}

#Function that allows continues loop to count time

def indecisive():
    ''' Sort the data and captures which choices the user thought of watching, 
    and just pick two'''

    sort_data = sorted(data.items(), key= lambda x: x[1], reverse= True)
    final_title1 = sort_data[0][0][0]
    final_image1 = sort_data[0][0][1]
    final_title2 = sort_data[1][0][0]
    final_image2 = sort_data[1][0][1]
    open_new_window(final_title1, final_image1, final_title2, final_image2)
    
def open_new_window(text1, img1, text2, img2):
    '''Create a window of the new choices that the user can make
    to reduce indecisiveness'''

    newWindow = Toplevel(window)
    newWindow.title("Choose")
    newWindow['background'] = "#221F1F"
    
    finalchoice1 = Button(newWindow, text= text1, width= 225, height= 300, image = img1, command= ""   )
    finalchoice1.grid(row= 0, column= 0, padx= 10, pady= 10)
    
    finalchoice2 = Button(newWindow, text = text2, width= 225, height = 300, image = img2, command= "")
    finalchoice2.grid(row = 0, column= 1, padx= 10, pady = 10)

def timer(lim):
    '''The timer that checks if the user is indecisive. if the user is,
    then the function calls the indecisive function to choose between choice'''
    time = 0
    while time < lim:
        time += 0.005
        print(time)
    if time >= lim:
        indecisive()
        #print(indecisive)

Thread(target=timer, args=(500, )).start()

#Starting and Recording length of time
class Tracker:
    
    def __init__(self, button):
        self.button = button
        self.title = self.button.cget('text')
        self.image = self.button.cget('image')
        self.timer = 0
        self.start = False
        
    def start_count(self):
        '''Count the hover time each choices.'''
        self.start = True
        while self.start:
            self.timer += 0.005
            #print(int(self.timer))

        
    def stop_count(self):
        '''Stop couting hover when it is outside of the buttons'''
        self.start = False
        data[(self.title, self.image)] = self.timer


def assign(widget):
    '''Create a Threading opperation so multiple loops can occure at 
    the same time'''

    tracker = Tracker(widget)
    
    def start():
        tracker.start_count()
    def end():
        tracker.stop_count()

    def start_t(event):
        Thread(target= start).start()
    
    def end_t(event):
        Thread(target= end).start()

    widget.bind('<Enter>', start_t)
    widget.bind('<Leave>', end_t)


#Import Photos
photo1 = PhotoImage(file= "C:\\Users\\USER\\Documents\\FBA\Coding\\Hackathon\\DataGrind 2.0\\Poster 1.png")
photo2 = PhotoImage(file= "C:\\Users\\USER\\Documents\\FBA\Coding\\Hackathon\\DataGrind 2.0\\Poster 2.png")
photo3 = PhotoImage(file= "C:\\Users\\USER\\Documents\\FBA\Coding\\Hackathon\\DataGrind 2.0\\Poster 3.png")
photo4 = PhotoImage(file= "C:\\Users\\USER\\Documents\\FBA\Coding\\Hackathon\\DataGrind 2.0\\Poster 4.png")
photo5 = PhotoImage(file= "C:\\Users\\USER\\Documents\\FBA\Coding\\Hackathon\\DataGrind 2.0\\Poster 5.png")
photo6 = PhotoImage(file= "C:\\Users\\USER\\Documents\\FBA\Coding\\Hackathon\\DataGrind 2.0\\Poster 6.png")

#Creating UI
lable_t = Label(window, text = "Choosen App", font  = ("Bebas Neue", 24, "bold"), fg= "#B81D24", bg = "#221F1F")
lable_t.grid(row = 0, column= 0, padx= 30, pady= 20)


#Create the list of choices
choice1 = Button(window, text = "Movie/Game Title 1", width = 225, height= 300, image = photo1, command = "")
choice1.grid(row= 1, column= 0, padx= 10, pady= 10)
assign(choice1)


choice2 = Button(window, text = "Movie/Game Title 1", width = 225, height= 300, image = photo2, command = "")
choice2.grid(row= 1, column= 1, padx= 10, pady= 10)
assign(choice2)


choice3 = Button(window, text = "Movie/Game Title 3", width = 225, height= 300,  image = photo3, command = "")
choice3.grid(row= 1, column= 2, padx= 10, pady= 10)
assign(choice3) 

choice4 = Button(window, text = "Movie/Game Title 4", width = 225, height= 300, image = photo4, command = "")
choice4.grid(row= 2, column= 0, padx= 10, pady= 10)
assign(choice4)


choice5 = Button(window, text = "Movie/Game Title 5", width = 225, height= 300, image = photo5, command = "")
choice5.grid(row= 2, column= 1, padx= 10, pady= 10)
assign(choice5)


choice6 = Button(window, text = "Movie/Game Title 6", width = 225, height= 300,  image = photo6, command = "")
choice6.grid(row= 2, column= 2, padx= 10, pady= 10)
assign(choice6) 

#somefunction(any of the buttons)
#   create a data of a timer and and the what was hoverd on
#   also run the timer




window.mainloop()

print(data)
