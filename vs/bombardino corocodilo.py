class Bird:
    def speak(self):
        return "cxavili"
    
class Duck(Bird):
    def speak(self):
        return "yiyini"
    
class Crow(Bird):
    def speak(self):
        return "krakuni"
    


birds = [Duck(), Crow()]

for bird in birds:
    print(bird.speak())