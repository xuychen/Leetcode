class Traveler:
    def __init__(self, name, state, city, travelDays):
        self.name = name
        self.state = [state]
        self.city = city
        self.travelDays = travelDays

class City:
    def __init__(self):
        self.state = "HEALTHY"
        self.travelers = [] 

def travel(initialStates):
    traveler_list = []
    city_list = {}
    day = 0
    maxDay = 0
    stateTransition = {("SICK", "HEALTHY"): "SICK", ("SICK", "RECOVERY"): "RECOVERY", ("SICK", "SICK"): "RECOVERY",
            ("HEALTHY", "HEALTHY"): "HEALTHY", ("HEALTHY", "SICK"): "RECOVERY", ("HEALTHY", "RECOVERY"): "HEALTHY"}

    for ele in initialStates:
        tmp = ele.split(" ")
        traveler_list.append(Traveler(tmp[0], tmp[1], tmp[2:], len(tmp) - 2))

    for traveler in traveler_list:
        maxDay = max(maxDay, traveler.travelDays)

    while day < maxDay:
        for city in city_list:
            city.state = "HEALTHY"
            city.travelers = []

        for traveler in traveler_list:
            today = day if day < traveler.travelDays else traveler.travelDays - 1
            city_list.setdefault(traveler.city[today], City())
            city_list[traveler.city[today]].travelers.append(traveler)
            if traveler.state[-1] in {"SICK", "RECOVERY"}:
                city.state = "SICK"
        
        for city in city_list:
            for traveler in city.travelers:
                traveler.state.append(stateTransition[(city.state), (traveler.state)])

        day += 1