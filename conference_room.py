import collections
def process_rooms_txt():
    rooms_file = open("rooms.txt", "r") # Open the file rooms.txt in read only mode

    # A dictionary with key as 'floor#.room#' and values as [capacity, timings..]
    rooms = collections.defaultdict(list) 
    
    #Iterate through each line in the file and process it into a dictionary
    for line in rooms_file:
        line = line.strip('\n') # To remove the '\n' from the line
        key, capacity, *timings = line.split(',')
        rooms[key].append(capacity)
        rooms[key].extend([*timings])

    return dict(rooms)

# Processes the input string into a meaningful dictionary
def process_input(input_slot):
    # A dictionary with 'team_floor.team_size' as key and values as [timings]
    team_info = collections.defaultdict(list)
    key, *timings = input_slot.split(',')

    team_info[key].extend([*timings])

    return dict(team_info)


def find_a_room(team_info, rooms):
    sorted(rooms) # Sort the rooms based on floor #

    closer = float('inf') # To keep a track of the room closest to the team
    ans = ''

    team_floor = str(min(float(k) for k in rooms.keys())).split('.')[0]
    team_size = str(min(float(k) for k in rooms.keys())).split('.')[1]

    team_start = list(team_info.values())[0][0]
    team_end = list(team_info.values())[0][1]
 
    i = 0
    #Iterate through all keys and keep a track of the closest room
    for k in rooms.keys():
        #If the room capacity is > team_size, we skip that room
        if rooms[k][0] < team_size:
            continue
        else:
            temp_arr = rooms[k][1:]
            n = len(temp_arr)
            i = 0
            while i < n:
                if temp_arr[i] <= team_start and temp_arr[i + 1] >= team_end:
                    if abs(int(team_floor) - int(str(k).split('.')[0])) <= closer:
                        closer = min(closer, abs(int(team_floor) - int(str(k).split('.')[0])))
                        ans += str(k)
                i += 2 #To check every pair of time
    return ans

def schedule_room(input_slot):
    rooms = process_rooms_txt()
    team_info = process_input(input_slot)

    ans = find_a_room(team_info, rooms)
    
    return ans

if __name__ == "__main__":
    input_slot = "5.8,10:30,11:30"
    ans = schedule_room(input_slot)
    print("input_slot : ", input_slot)
    print("Answer : ", ans)
