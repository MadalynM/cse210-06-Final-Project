# cse210-06-Final-Project

# Gold Seeker
Gold Seeker is a game where the player (#) searches for gold (@). The player dodges obstacles like snakes and rocks. The rocks will reset the players points when the player is hit by them and the snakes will end the game. The player gains points by getting gold. 

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 gold_seeker 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- gold_seeker                (source code for game)
  +-- game              (specific game classes)
    +-- casting         (various actor classes)
    +-- directing       (director and scene manager classes)
    +-- scripting       (various action classes)
    +-- services        (various service classes)
    +-- shared          (various classes shared throughout the program)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
+-- README.md           (general info)

## Authors
---
Madalyn Mounts (mou21015@byui.edu)
Samuel Ernesto Narvaez Peinado (nar20002@byui.edu)
Agipare Emmanuel (agi22001@byui.edu)
Stephen Port (por21022@byui.edu)
Mohamed Nasiru ()
