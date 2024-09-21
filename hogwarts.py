students = [
    {"name" : "Hermione", "house" : "Gryffindor", "Patronous" : "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "Patronous" : "Stag"},
    {"name" : "Ron", "house" : "Gryffindor", "Patronous" : "Jack Russel Terrier"},
    {"name" : "Draco", "house" : "Slytherrin", "Patronous" : None}]
for _ in students:
    print(_["name"], _["house"], _["Patronous"], sep=", ")


