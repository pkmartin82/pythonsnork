# This is for dictionaries
patrickDictionary = {}
patrickDictionary["first"] = "Patrick"
patrickDictionary["last"] = "Martin"

susan = {"first" : "Susan", "last" : "Ibach"}

print(patrickDictionary)
print(susan)

people = [patrickDictionary, susan]
print(people)

people.append({"first":"bill","last":"gates"})
print(people)
owners = people[2:]
print(len(owners))
print(owners)