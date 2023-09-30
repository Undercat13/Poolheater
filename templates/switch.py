relays_status = [0,0,0,0,0,0,0,0,0,0,0,0]


#*basic config
# power heater
# turn valves to correct config
# 	possibly store a txt file with the valve statuses in case of poweroff
# actuate quick start
# increase temp

valve_stat_arr = ["1->pool", "2->pool", "3->pool", "4->pool"]



def writelines():
	valve_status = open("valve_status.txt", "w+")
	for status in valve_stat_arr:
		print(status)
		valve_status.write(status+ '\n')
	valve_status.close()

writelines()

def relay_switch(input):
	match input:
		case 0:
			print("input = 1")
			toggle_status(input)
			relays_status[1] = 0
			relays_status[2] = 0
			relays_status[3] = 0
		case 1:
			print("input = 2")
			toggle_status(input)
			relays_status[0] = 0
			relays_status[2] = 0
			relays_status[3] = 0
		case 2:
			print("input = 3")
			toggle_status(input)
			relays_status[0] = 0
			relays_status[1] = 0
			relays_status[3] = 0
		case 3:
			print("input = 4")
			toggle_status(input)
			relays_status[0] = 0
			relays_status[1] = 0
			relays_status[2] = 0
		case 4:
			print("input = 5")
			valve_stat_arr[0] = "test"
			writelines()

		case 5:
			print("input = 6")
		case 6:
			print("input = 7")
		case 7:
			print("input = 8")
		case 8:
			print("input = 9")
		case 9:
			print("input = 10")
			toggle_status(input)
			sleep(.5)
			toggle_status(input)
		case 10:
			print("input = 11")
			toggle_status(input)
			sleep(.5)
			toggle_status(input)
		case _:
			print("erronous input")

def toggle_status(num):
	if(relays_status[num] == 0):
		relays_status[num] = 1
	else:
		relays_status[num] = 0


writelines()

valve_status = open("valve_status.txt", "r")
valve_stat_arr[0] = valve_status.readline()
valve_stat_arr[1] = valve_status.readline()
valve_stat_arr[2] = valve_status.readline()
valve_stat_arr[3] = valve_status.readline()
valve_status.close()

relay_switch(1)
#relay_switch(4)

valve_status.close()


