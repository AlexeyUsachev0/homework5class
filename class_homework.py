class Bicycle:
    weight = "unknown"
    purpose = "unknown"

    def __init__(self, bike_type, model, material_frame, material_fork, frame_id):
        self.bike_type = bike_type
        self.model = model
        self.material_frame = material_frame
        self.material_fork = material_fork
        self.__frame_id = frame_id

    def bike_purpose(self):
        return print(f'{self.model} is for {self.purpose}')

    def skidding(self):
        if self.bike_type == "track" or self.bike_type == "fixed gear":
            print("bike is skidding")
        else:
            print("no skid for you")

    @property
    def bike_id(self) :
        return self.__frame_id
    @bike_id.setter
    def bike_id(self, frame_id):
        self.__frame_id = frame_id
        print(f'номер рамы перебит на {self.__frame_id}')



class EBike(Bicycle):
    def __init__(self, bike_type, model, material_frame, material_fork, frame_id, battery_watts):
        super().__init__(bike_type, model, material_frame, material_fork, frame_id)
        self.battery_watts = battery_watts

    def bike_purpose(self):
        return print(f'{self.model} is for {self.purpose} with motor')



tsunami_snm100 = Bicycle("track","snm100","aluminium","aluminium", 1)
specialized_electro = EBike("road","crux", "carbon", "carbon", 2, 100)
# tsunami_snm100._Bicycle__frame_id = 4
# print(tsunami_snm100._Bicycle__frame_id)
# print(tsunami_snm100.frame_id)
print(tsunami_snm100.bike_id)
tsunami_snm100.bike_id = 5
print(tsunami_snm100.bike_id)

print(specialized_electro.weight)
specialized_electro.purpose = "road cycling"
specialized_electro.bike_purpose()
tsunami_snm100.bike_purpose()

print(specialized_electro.bike_id)
specialized_electro.bike_id = 8
print(specialized_electro.bike_id)