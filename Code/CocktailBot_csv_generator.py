#8/2/22

import random
from random import sample 
import csv 

initiators=['Robot Initiates','Person Initiates', 'Both Initiate']
to_whoms=['To the Table', 'to Person A/Person B']

def generate_groups():
    groups ={} #creating overall dictionary 
    for i in range(12): 
        orderings={} #creating 12 sub dictionaries to store each set of trials 
        initiator=sample(initiators, 3) #randomly creating an order for the three initiator variables and the two to whom variables
        to_whom=sample(to_whoms, 2)

        for j in range(2): #variable pairing
            for k in range(3):
                orderings[3*j+k+1]= initiator[k], to_whom[j]
        keys=list(orderings.keys()) 
        random.shuffle(keys) #randomizing order of keys:values
        new_ordering=[]
        for x in keys: 
            new=(x, orderings[x]), 
            new_ordering.append(new)

        groups[i+1]= new_ordering
    with open('test.csv', 'w') as f:
        writer=csv.writer(f)
        writer.writerow(['Group1', 'Group2', 'Group3','Group4', 'Group5', 'Group6'])
        [writer.writerow(groups[i+1]) for i in range(12)]
        f.close()

    return groups #returns 12 groups each containing six scenarios 


if __name__ == '__main__':
    generate_groups()

