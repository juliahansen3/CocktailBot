#!/usr/bin/env python
#8/2/22

# import pandas as pd 
import random 
import time
import socket
import sys


import rospy
import math
import actionlib
import movement # imports the Movement class from the movement.py file


# Just here for imports in case the Movement class variables need to see it in this file
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from move_base_msgs.msg import MoveBaseGoal, MoveBaseAction
from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import Pose, Point, Quaternion, Twist
from tf.transformations import quaternion_from_euler, euler_from_quaternion

from math import atan2




# def write_script(row, column):  
#     #print(trial_number, test_df.iloc[row, column])
#     condition= random.choice(conditions)
#     relationship=random.choice(relationships)
#     print('Scenario:', test_df.iloc[row, column], condition, ',',relationship)
#     return 'Scenario:', test_df.iloc[row, column], condition, ',',relationship



#######################################
# CLASS NAME: Initiator
# DESCRIPTION: Represents the initiator variable in our cocktailbot study
# 
# INPUT: a Movement() object for directing 
#
#######################################
class Initiator:
    def __init__(self, mover):
        self.mover = mover


    def robot_initiates(self, toWhom): 

        # wait X amount of seconds before moving
        time.sleep(random.choice([10,15,20]))


        if toWhom == 'To the Table': # in test_df.iloc[row][column]:
            goal = Point()
            goal.x = 2.7
            goal.y = -0.75
            mover.move_to_goal_point(goal) 


        elif toWhom == 'to Person A/Person B': # in test_df.iloc[row][column]:
            goalA = Point()
            goalA.x = 2.7
            goalA.y = -0.25

            goalB = Point()
            goalB.x = 2.7
            goalB.y = -1.5

            self.mover.move_to_goal_point(random.choice([goalA, goalB]))
        # Determine if it is going to the table or a single person
        #       - if table: set goal 2.6, -1
        #       - if single person: randomly select between two goal points [(2.6, 0), (2.6, -1.5)]
        # PASS goal point to movement method




    def person_initiates(self, toWhom, sckt):
        summoned = pressed_person(self.mover, sckt)
        
	#pressed = ''
        #while pressed == '':
         #   self.mover.stop()
          #  pressed = raw_input("Button Pressed? Press 'Enter' if no")
        
	if summoned:
	    if toWhom == 'To the Table': # in test_df.iloc[row][column]:
	        goal = Point()
	        goal.x = 2.7
	        goal.y = -0.75
	        rospy.loginfo("about to move to the table")
	        self.mover.move_to_goal_point(goal)
	    elif toWhom == 'to Person A/Person B': # in test_df.iloc[row][column]:
	        goalA = Point()
	        goalA.x = 2.7
	        goalA.y = -0.25

	        goalB = Point()
	        goalB.x = 2.7
	        goalB.y = -1.5

	        rospy.loginfo("About to go to the person of my choosing")
	        self.mover.move_to_goal_point(random.choice([goalA, goalB]))
        # WAIT FOR BUTTON TO BE PUSHED
        #       - continue publishing movements of 0
        # Determine if it is going to the table or a single person
        #       - if table: set goal 2.6, -1
        #       - if single person: randomly select between two goal points [(2.6, 0), (2.6, -1.5)]
        # PASS goal point to movement method



    # (test_df, row, column, movement):
    def mixed_initiates(self, toWhom, sckt): # sckt
        summoned = pressed_mixed(self.mover, sckt) #sckt

        #pressed = ''
        #while pressed == '':
         #   self.mover.mixed_circle()
          #  pressed = raw_input("Button Pressed? Press 'Enter' if no")


        #while not pressed(self.mover, sckt):
         #   rospy.loginfo("Button not pressed")
          #  self.mover.mixed_circle()

	if summoned:
	    if toWhom == 'To the Table': # in test_df.iloc[row][column]:
	        goal = Point()
	        goal.x = 2.6
	        goal.y = -0.8
	        rospy.loginfo("about to move to the table")
	        self.mover.move_to_goal_point(goal)
	    elif toWhom == 'to Person A/Person B': # in test_df.iloc[row][column]:
	        goalA = Point()
	        goalA.x = 2.6
	        goalA.y = -0.25

	        goalB = Point()
	        goalB.x = 2.6
	        goalB.y = -1.5

	        rospy.loginfo("About to go to the person of my choosing")
	        self.mover.move_to_goal_point(random.choice([goalA, goalB]))
        # WHILE BUTTON IS NOT PUSHED
        #       - have robot move in a circle motion
        # WHEN BUTTON IS PUSHED
        # Determine if it is going to the table or a single person
        #       - if table: set goal 2.6, -1
        #       - if single person: randomly select between two goal points [(2.6, 0), (2.6, -1.5)]
        # PASS goal point to movement method








def pressed_mixed(mover, sckt): #sckt
    #now keep talking with the client
    pushed = False
    finished = False
    start = rospy.get_time()
    while not rospy.is_shutdown() and not finished:
        while not pushed and rospy.get_time() - start < 180:
        # wait to accept a connection - blocking call
            conn, addr = sckt.accept()
            data = conn.recv(1024)
            # print ('Connected with ' + addr[0] + ':' + str(addr[1]) + " " )
            message = str(data.decode("utf-8"))
            if message =="Button was pressed" :
                ButtonPressed.publish(message)
                print(message)
                #rospy.sleep(10)
                pushed = True
            else:
	        mover.mixed_circle()
                print('not yet pressed')
		pushed = False	
        finished = True
        sckt.close()
    return pushed







def pressed_person(mover, sckt): #sckt
    #now keep talking with the client
    pushed = False
    finished = False
    start = rospy.get_time()
    while not rospy.is_shutdown() and not finished:
        while not pushed and rospy.get_time() - start < 180:
        # wait to accept a connection - blocking call
            conn, addr = sckt.accept()
            data = conn.recv(1024)
            print ('Connected with ' + addr[0] + ':' + str(addr[1]) + " " )
            message = str(data.decode("utf-8"))
            if message =="Button was pressed" :
                ButtonPressed.publish(message)
                print(message)
                #rospy.sleep(10)
                pushed = True
            else:
                mover.stop()
                print('not yet pressed')
		pushed = False    
            
        finished = True
        sckt.close()

    return pushed






if __name__ == '__main__':
    try:
        #info for button:
        rospy.init_node('pressed', anonymous=True)
        ButtonPressed=rospy.Publisher('chat', String, queue_size=10)


        ########################################
        #
        #       SOCKET CONNECTION FOR BUTTON
        #
        ########################################
        
        HOST = '' # Symbolic name, meaning all available interfaces
        PORT = 8888 # Arbitrary non-privileged port
         
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ('Socket created')
         
        #Bind socket to local host and port
        try:
            s.bind((HOST, PORT))
        except socket.error as msg:
            print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()
         
        print ('Socket bind complete')
        
        s.listen(10)
        print ('Socket now listening')  

        mover = movement.Movement()

        initiator = Initiator(mover)
        
 

        # test_data=pd.read_csv('test.csv')
        # test_df=pd.DataFrame(data=test_data)
        #row, column= input('Row, Column #s:').split()

        conditions=['not hungry', 'hungry']
        relationships=['old friend', 'met a couple of times', 'acquaintance']
        # row, column= input('row, column: (make sure to add a space)').split()
        # write_script(int(row), int(column))

        scenario = int(input('What scenario # are you running?'))

        ready=raw_input('Are you ready? (yes/no)').lower()

        while ready == 'no':
            time.sleep(10)
            ready=input('Are you ready?')

        

        if scenario == 1:
            # Initiator == robot 
            # toWhom == Person A/B
            initiator.robot_initiates(toWhom='to Person A/Person B')

        elif scenario == 2:
            # Initiator == both
            # toWhom == Person A/B
            initiator.mixed_initiates(toWhom='to Person A/Person B', sckt=s)

        elif scenario == 3:
            # Initiator == person 
            # toWhom == Person A/B
            initiator.person_initiates(toWhom='to Person A/Person B', sckt=s)

        elif scenario == 4:
            # Initiator == robot 
            # toWhom == Table
            initiator.robot_initiates(toWhom='To the Table')

        elif scenario == 5:
            # Initiator == both 
            # toWhom == Table
            initiator.mixed_initiates(toWhom='To the Table', sckt=s)

        else:
            # Initiator == person 
            # toWhom == Table
            initiator.person_initiates(toWhom='To the Table', sckt=s)


        # ONCE AT THE TABLE:
        #       - order the robot to return to the table after the participants either 
        #               a) took the food, or 
        #               b) ignored the robot
        #       - Will prompt user if the robot is ready for people to take food

        mover.return_to_starting_pos()

    except rospy.ROSInterruptException:
        rospy.loginfo("Didn't work, so cry")
