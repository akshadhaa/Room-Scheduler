Info about all the rooms is present in rooms.txt, where info about each room is line separated. Each line is a comma separated string containging:
 
 "floor number.room number","capacity","starttime1", "endtime1", "starttime2", "endtime2", ... 

The input is a string about the team that wants to schedule a room. Format of the input is: 

"team's floor #.team_size, "starttime1", "endtime1"

* For the purpose of this assignment, the input string can have only 1 pair of start and end times.

Unit test can be performed using Pytest library on find_a_room method, by passing a pair of dummy data about the rooms and teams and asserting the values.
