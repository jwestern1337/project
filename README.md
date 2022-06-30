# project

A python project written for my computer science class

There is a user login system
The user is given first letter of each word in a song title and the song producer.
The user is then given 5 guesses to get the correct song , if they get it right then they get congratulated.
There are admin functions such as adding a user or deleting user accounts.

CHANGELOG:
  - 11/05/2022
     - made it so you cannot delete the user you are logged in as
     - removed the background color class (it was not needed)
  - 17/05/2022
     - reduced size of code by ~50 lines
     - changed animated title, easier to read now
  - 19/05/2022
     - added more comments to the code to explain things better
     - fixed login system, would sometimes ask for password twice then crash
     - (admin only) when you register a user, check if that user already exists
  - 26/05/2022
     - (admin only) when registering a user, sometimes it would create the user, ask for their password, then create the user again. thats now fixed
     - fixed a typo in the play function
     - set the thread that ran the animated title screen to be killable (daemon = True) so if you ctrl+c it will close the program at some points rather than staying open
  - 30/06/2022
     - Improved setup function, detects if the creds directory is empty
     - Fixed a few errors in the setup function
     - Reduced size of file by 2 lines
