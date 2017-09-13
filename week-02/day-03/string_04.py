# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" between the words "It" and "you"

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
solution = quote.split(" ")
print(solution.index("It"))
solution.insert(3, "always takes longer than")
#solution [:3] += ["always takes longer than"] 2.solution
quote = " ".join(solution)

#solution.append("always takes longer than")
#
print(quote)