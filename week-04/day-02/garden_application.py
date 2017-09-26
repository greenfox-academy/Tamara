class Garden(object):
    def __init__(self):
        self.water = 10
        self.plants = []

    def add(self, plants):
        self.plants.append(plants)
  
    def get_water(self, water, plants):
        # for i in range(len(plants)):
        #     for j in range(len(plants)):
        #         if i < 10 or j < 5:
        #             self.trees[i].current_water_amount += 10
        #             self.flowers[j].current_water_amount += 10
        # return plants
        for plant in self.plants:
            if plant.needs_water():
                plant.water(10)
            else:
                pass


class Tree(object):
    def __init__(self, color, current_water_amount=10):
        self.color = color
        self.current_water_amount = current_water_amount
        
    def needs_water():
        if current_water_amount <5:
            return True

    def watering(self, water):
        if current_water_amount < 10:
            current_water_amount += 4
            

class Flower(object):
    def __init__(self, color, current_water_amount=5):
        self.color = color
        self.current_water_amount = current_water_amount
        
    def watering(self, water):
        if current_water_amount < 5:
            current_water_amount += 7.5
            

garden = Garden()
garden.plants.append(Tree('purple'))
garden.plants.append(Tree('orange'))
garden.plants.append(Flower("yellow"))
garden.plants.append(Flower("blue"))

garden.get_water(40, "plants")
# garden.get_water(70, "plants")