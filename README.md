# CocktailBot
This repository contains the code for setting up and moving a 3Dx pioneer robot in a 'cocktail environment'. It also contains the Arduino and Python code for configuring the connection between an Arduino button system and a remote computer connected to the robot. To use this code, you must have ROS 1, Arduino IDE, and Python 2. 
Each trial consists of six scenarios with different pairings of initiation form and scenario context. The order of these scenarios in each trial was randomized to ensure little to no bias.

<b> SETTING UP THE ROBOT:</b>

1. Turn on the robot.
2. Connect the two USB cables on the robot to the back of the computer you're using (in our case we used an aadi2 computer). 
3. Enter the cocktailbot workspace in terminal and jump to the cocktail_bot directory by typing <b>CocktailBot_ws/src/cocktail_bot</b>.
4. Write <b>./run-pioneer-robot</b> in the same terminal.
5. SSH into the aadi2 computer on another computer by typing <b>ssh aadi2@IP_ADDRESS</b> on a terminal window on the other computer.
6. Once you're in, navigate to CocktailBot_ws/src/cocktail_bot/scripts and run <b>python CocktailBot_csv_read.py</b> .
7. After a couple of seconds, you should get a message saying the socket was created, is binded and ready for connections. The screen will prompt you to enter the trial you are running and then will ask if you are ready to continue. By entering yes, you are ready to begin a trial. 
8. Once the robot has reached the table, the code will prompt you asking if CocktailBot is ready to return to base. By entering yes the robot will return to/close to its starting position. 
9. Repeat steps 6-8 for all the trials you wish to run. 

<b> SETTING UP THE BUTTON:</b>

1. Make sure the USB cable is connecting the Arduino MKR wifi shield to a separate computer. Upload the code by pressing the arrow symbol in the top left corner. Check that the shield is connected to the internet by opening up serial monitor on Arduino IDE. It should say "You're connected to the network". 
2. Once the shield is connected to the network, run roscore in a terminal window and run the Arduino_receive_test.py Python script in a separate terminal window. If the connection between the Arduino and the robot laptop is formed, then the terminal will print "connection established". If the button is pushed, the Arduino client server will send a message saying that the button was pushed to the host computer.
3. After verifying that a connection can be established between the two computers, run <b>python CocktailBot_csv_read.py</b> in the CocktailBot_ws/src/cocktail_bot/scripts directory. If the button is pushed, then the robot will enter a new state of action and move. 
