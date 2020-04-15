### data is taken as two dimensional array as when you import text file the python reads it as two dimensional array
data = [[7.11,8,"9:00", "9:15", "14:30","15:00"],
         [8.23,6, "10:00", "11:00", "14:00", "15:00"],
         [ 8.43,7,"11:30","12:30","17:00", "17:30"],
         [9.511,9,"9:30","10:30","12:00","12:15", "15:15","16:15"],
         [9.527,4,"9:00","11:00","14:00","16:00"],
         [9.547,8,"10:30","11:30","13:30", "15:30","16:30","17:30"]]


#print(data)

noOfMem = int(input("Please enter the number of team members:"))
floor = int(input("Please enter the floor the team members work :"))
startTime = input("please enter the start time of the meeting in HH:MM format:")
stopTime = input("please enter the stop time of the meeting:")

newData = []

#first the number of members in a team is compared with the maximum capacity of
# the room and if it is satisfied we compare the time slots and if those are available for particular room then
# then the room number is added into the list called newData
for item in data:
    if noOfMem <= item[1]:
        if startTime in item:
            if stopTime in item:
                newData.append(item[0])



## the new list is checked if it is empty and if not then the priority is set using if else for the nearest floor
# if the newData is empty that means there are no rooms found for the available time slots so the message is printed.
#print(newData)

if newData != []:
    for all in newData:
        if (int(all) - floor) == 0:
            print(all)
        elif (int(all) - floor) == 1:
            print(all)
        elif (int(all) - floor) == -1:
            print(all)
        else:
            print(all)
else:
    print("There are no rooms available for the required time slot.")

