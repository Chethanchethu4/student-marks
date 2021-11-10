class std:

    def gethighestmarks(self):
        print(" get hihest marks")
        return 67
dheeraj=std() #obejct is created
dheeraj.maths = 24
dheeraj.science = 25
print(dheeraj.gethighestmarks())
print(dheeraj.maths)

from std import std
dheeraj = std(12,94,78)
print(dheeraj.maths)
print(dheeraj.gethighestmarksInmaths())
