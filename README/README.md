# SYNCSHACK_2021

## Team Lineup: ##

Team Member | Engineering Major
------------ | -------------
Rishi Deshpande | Mechantronic
Jordan Guyot | Mechatronic
Cameron Mitchel | Mechanical
Joshua Novick | Mechatronic
Adam Riesel | Mechatronic
Hamish Vass | Biomedical
    
    


## Synopsis ##
The game *Drinkey Bill* requires the installation of two additional python librarys `termcolor` and `pydealer` - these are automatically installed for the user when the game is run.

There is no external rule book on how to play the game. It is designed to be played with no prior knowledge, and to prompt the player on what do do and how to play as the game progresses.

The game is recommended to be played with 2-8 players although it can handle any amount of players.



## What problem are we trying to solve? ##
Right now, the world is more isolated and alone then it ever has been. To this date it has been 21 months since this pandemic began. That’s 638 days. Of that a vast majority has been spent indoors and locked inside our own homes. In the four weeks leading up to the 25th of April 2021 alone, there were 82,000 calls to lifeline and 22,000 calls to Beyond Blue. This is unacceptable and we wanted to do something about it.

## What does our product do/Who is it for? ##
In light of the current impacts of lockdown and restrictions from the coronavirus. Our product, *Drinky Bill*, aims to help people reconnect remotely through an online platform with drinking mini games; designed for compatibility with interfaces such as zoom and skype. *Drinky Bill*, is a suitable mini games platform suitable for all adults and people over the legal drinking age who are seeking the joy of social interaction and games online, from their own homes all while being prompted to drink resposnsibly.

## How did we make the prototype? ##
We took a modular approach towards prototyping, whereby we started our design at a high level, defining our application's general control flow from the entry of the program to the exit using a control flow diagram. Once we had a unanimous agreement on the application’s high-level functionality, we defined our modules, being a module for each game. This allowed us to divide the work easier, where we could individually work on a module to get it working independent of the main program. Our low-level design for each module contains an entry function for the main program to access and pass objects through, and several other functions for each game to work. Once the low-level design of each module worked independently, we worked to integrate these with the main function, testing to ensure that each individual module worked as intended. Beyond that, we tested our program at a high level to ensure it had the intended functionality and user experience. As a final touch, we designed plans for our future vision of the product to implement scalability and longevity of the product, researching innovative technologies to implement.

We made the prototype using GitHub and Visual Studio Code. We coded in Python as that is the language we are the most comfortable in as first year students; it is also the one we feel is the best fit for what we are trying to do. The code consists of different files which define the functions for each game, while the main.py file brings all of these functions together and runs the platform smoothly. The prototype of the website was made on Figma.com.
 
## What challenges did we run into? ##
Being first year students, our greatest challenges came through a general lack of holistic experience among multiple language and high level coding projects. We attempted a number of new aspects of coding including front end development which ultimately proved unsuccessful. Among this, the overall process of integrating multiple modules into one whole program was a difficult challenge to manoeuver as first years. Despite these setbacks, we ultimately played to the strengths we had developed last semester, allowing us to produce a successful, harmonious and enjoyable program.
 
## Where can our product go in the future? ##
Our product has a lot of potential as an online web-application, whereby we hope to integrate it with AWS Serverless Architecture as seen here, to increase its ability to handle user traffic on an online web-app, without the costs and hassles of operating servers. 
Ideally, we will be able to integrate AI and Machine Learning into the architecture beyond that, so that we can use it for a range of applications, such as monitoring alcohol consumption without needing to manually input quantities, and provide recommended games when we expand our games library.
Overtime, we will allow for community collaboration, whereby the community around the app will be able to develop and publish games, which can be played and rated by the community to allow for new content to constantly be cycled through.
As lockdowns come to an end, we additionally would like to create a phone app so that users can easily use our platform on the go. This can be additionally implemented using AWS services so that it integrates with our online web-app.

Despite Drinkey Bill being initially targeted towards those in lockdown, the future of Drinkey Bill is still promising. When the time comes we are allowed to visit other people houses Drinkey Bill can be used as a substitute if there are no cards available or people don’t know the rules. Additionally we will continue to add more games and improve the front end coding in order to further enhance the appeal of Drinkey Bill


The Drinkey Bill team have considered Australian responsible service of alcahol laws in the production of the game and promote the safe, responsible use of alcahol for all.