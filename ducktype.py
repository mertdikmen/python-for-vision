class Pig:
    def yell(self):
        print "Oink!"
	
class Duck:
    def yell(self):
        print "Quack!"
        
def make_sound(animal):
    animal.yell()
    
if __name__ == '__main__':
    pig = Pig()
    duck = Duck()
    
    make_sound(pig)
    make_sound(duck)