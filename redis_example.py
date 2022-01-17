

import json
import redis as r


connection=r.Redis(db=2)

class TravelAgency():

    tour_id=0
    trip_id=0
    def passenger_create(self,name,phone,age):
        self.pass_id += 1
        connection.hset(f"{self.pass_id}",mapping={"name":name,"phone":phone,"age":age})


    
    def show_passenger(self,name):
        return self.connection.hgetall(name)



    def trip_create(self,passenger,beginning,destination,time,vehicle,pass_id):
        passengers={}
        for i in pass_id:
            passenger = self.connection.hgetall(i)
            for j in passenger:
                passenger[j.decode('utf-8')] = passenger.pop(j).decode('utf-8')
            passengers[i] = passenger


        connection.hset(f"trip:{beginning}:{destination}:{time}:{vehicle}",mapping={"beginning":beginning,"destination":destination,
        "time":time,"vehicle":vehicle,"passenger":json.dumps(passengers)})

        self.trip_id+=1


    def show_trip(self,beginning,destination,time):
        return (connection.hgetall(f"trip:{beginning}:{destination}:{time}"))


    
    def tour_create(self,leader,passenger,days,price,beginning,destination,details,pass_id):
        passengers={}

        for i in pass_id:
            passenger = self.connection.hgetall(i)
            for j in passenger:
                passenger[j.decode('utf-8')] = passenger.pop(j).decode('utf-8')
            passengers[i] = passenger


        connection.hset(f"tour:{leader}:{beginning}:{destination}",mapping={"leader":leader,"passenger":json.dumps(passengers),"days":days,"price":price,
        "beginning":beginning,"destination":destination,"details":details})

        self.tour_id+=1
    

    def show_tour(self,beginning,destination,leader):
        return (connection.hgetall(f"tour:{leader}:{beginning}:{destination}"))
        
   
