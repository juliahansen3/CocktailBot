LAST UPDATED: August 19, 2022


PURPOSE: This serves as a document about how to run the cocktail bot experiment for initiative in social feeding. 

- The code is meant to take input from the users depicting which initiative scenario we are testing and run a pioneer 3dx robot accordingly by mapping the robot's position using Odometry based on a goal point that simulates the location of the participant's high table/chairs. 


WHAT YOU NEED:
1) A computer that can run ./run-pioneer-robot which runs roscore, RosAria, Rviz, pioneer-test-sensors, navigation stack, etc., and one that can run python 2.7

2) The cocktail-bot repository that utilizes:
	- actionlib
	- rospy
	- roscpp
	- tf
	- geometry_msgs
	- std_msgs
	- robot-setup-tf (which is another package that can be created following: http://wiki.ros.org/navigation/Tutorials/RobotSetup/TF)
	- odometry-msgs (also another package created following: http://wiki.ros.org/navigation/Tutorials/RobotSetup/Odom)

3) the Arduino button connected to the Dell laptop (look at Arduino README.txt) to ensure everything is set up for running the program




HOW TO RUN CODE:
1) Open a terminal and navigate to the cocktail_bot package
	- you may need to source devel/setup.bash in the catkin_ws order to use the ROS commands

2) Once in the cocktail_bot package, run run-pioneer-robot by typing in the terminal "./run-pioneer-robot" (excluding the quotations)
	- this will run all the necessary background items such as roscore, RosAria, and Rviz. You may minimize the rviz window once it appears

3) Open a new terminal and in the console run "rosrun cocktail_bot CocktailBot_csv_read.py" (do not include the quotations)
	- this should run the program and allow for user input

4) The first prompt after performing step 3 should ask "What scenario # are you running?" which the numbers are as follows
	- 1: initiator = robot, initiated = person A/B
	- 2: initiator = both, initiated = person A/B
	- 3: initiator = person, initiated = person A/B
	- 4: initiator = robot, initated = to table 
	- 5: initiator = both, initiated = to table
	- 6: initiator = person, initiated = to table

5) After entering the scenario #, the screen will prompt you if you are ready to run in which you type "yes" or "no" (without quotes)
	- if yes, the program will start running
	- if no, will re-prompt you in 10 seconds if you are ready

6) Once the robot makes it to the intented "initiated" goal position using odometry, another prompt will appear if you would like the robot to return home. Simply type in "y" or "n" (without the quotes)
	- if y, the robot will turn and return to what it believes to be coordinate (0, 0)
	- if n, the robot will not move and the program will stop



ADDITIONAL NOTES/TIPS FOR RUNNING:
1) TESTING SETUP: 
	- Is best to test/run the robot using both the Asus-Charisma-2G wireless network and ssh into the robot's computer for running given
	  the need to prompt a user
	- the password to access the Asus-Charisma-2G system is on the router, and the ASUS website username and password is "charisma" (no 		  quotes)

2) STARTING POSITIONS AND GOAL POINTS: 
	- The robot does NOT reset he position of (0, 0) everytime you run the CocktailBot_csv_read.py file, so you will need to kill and 		  restart ./run-pioneer-robot
	- Is best to have a marked starting place
	- may also need to modify the goal points to reflect your space. to determine how to change, you can use Rviz and the grid system it 		  generates upon start up. 
		- X is positive in the forward direction on the robot
		- Y is positive in the left direction on the robot
		- A positive Z will turn towards the left

3) KILLING THE SOCKET: If you were required to kill the robot before participants pushed the Arduino button or the robot timed out which it does after 3 minutes in scenarios where initiator = person/both and you cannot run the program given the "socket is already bound", you need to manually kill the socket
	a) In a new terminal type "sudo netstat -ap | grep :8888" (no quotes) 
		- this should list all available ports/processes that are currently running/listening to ports
	b) Find the PID number provided by the socket which is either listed after "tcp" or under it.
		- if nothing appears on the screen showing it is in TIME_WAIT, then you do not need to kill the socket
	3) in the same terminal type "kill -9 PID" (no quotes) where PID is replaced with the number found in step 2. 
		- this terminates the socket and you should be able to now rosrun the original code once again





















 









