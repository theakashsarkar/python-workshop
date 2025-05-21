class Bird:
    def quack(self):
        return "quack"

class Duck(Bird):
    def quack(self):
        return "quack"

def alert(birdie):
    birdie.quack()

def alert_duck(birdie: Duck):
    birdie.quack()

def alert_bird(birdie: Bird):
    birdie.quack()

daffy = Duck()
print(alert(daffy))
print(alert_duck(daffy))
print(alert_bird(daffy))