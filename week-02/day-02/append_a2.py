# - Create a variable named `nimals`
#   with the following content: `["kuty", "macsk", "cic"]`
# - Add all elements an `"a"` at the end

nimals = ["kuty", "macsk", "cic"]
def content (animals):
    for i in range(len(animals)):
        animals[i] += "a"
    return animals

print(content(nimals))