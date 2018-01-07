# Sharpie
# - Create `Sharpie` class
#   - We should know about each sharpie their `color` (which should be a string), 
#  `width` (which will be a floating point number), `ink_amount` (another floating point number)
#   - When creating one, we need to specify the `color` and the `width`
#   - Every sharpie is created with a default 100 as `ink_amount`
#   - We can `use()` the sharpie objects
#     - which decreases inkAmount

class Sharpie (object):
    def __init__(self, color, width):
        self.color = color
        self.width = float(width)
        self.ink_amount = float(100)
    
    def use(self):
        self.ink_amount -= 1


blue_sharpie = Sharpie('blue', 10)
blue_sharpie.use()
print(blue_sharpie.ink_amount)
blue_sharpie.use()
print(blue_sharpie.ink_amount)
green_sharpie = Sharpie('green', 12)
green_sharpie.use()
print(green_sharpie.ink_amount)