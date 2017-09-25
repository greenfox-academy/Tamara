# Post-it
# - Create a `PostIt` class that has
#   - a `background_color`
#   - a `text` on it
#   - a `text_color`
# - Create a few example post-it objects:
#   - an orange with blue text: "Idea 1"
#   - a pink with black text: "Awesome"
#   - a yellow with green text: "Superb!"

class PostIt(object):
    def __init__(self, background_color, text, color):
        self.background_color = background_color
        self.text = text
        self.color = color
    
first_text = PostIt("orange", "Idea 1", "blue")
second_text = PostIt("pink", "Awesome", "black")
third_text = PostIt("yellow", "Superb!", "green")
    

print(first_text.background_color, first_text.text, first_text.color)
print(second_text.background_color, second_text.text, second_text.color)
print(third_text.background_color, third_text.text, third_text.color)
 