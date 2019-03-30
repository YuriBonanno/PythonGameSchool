import numpy as np
from scipy.stats import maxwell
import random as rnd

class Student:
    firstName = 0
    nickName = 0
    lastName = 0
    fullName = 0
    martialArts = 0
    bullying = 0
    maths = 0
    myths = 0
    linguini = 0
    cooking = 0
    popularity = 0
    artism = 0
    cartography = 0
    theoreticalBiology = 0
    physicalBiology = 0
    procrastinating = 0
    crying = 0

    def __init__(self):
        a = 1 #wordt hoger naarmate je verder komt
        maxwellData = (maxwell.rvs(size=13)*a)
        bins = np.linspace(0.5, 10.5, 11)
        digitized = np.digitize(maxwellData, bins)
        for i in range(len(digitized)):
            if digitized[i] <= 0:
                digitized[i] = 1
            if digitized[i] >= 10:
                digitized[i] = 10

        self.martialArts = digitized[0]
        self.bullying = digitized[1]
        self.maths = digitized[2]
        self.myths = digitized[3]
        self.linguini = digitized[4]
        self.cooking = digitized[5]
        self.popularity = digitized[6]
        self.artism = digitized[7]
        self.cartography = digitized[8]
        self.theoreticalBiology = digitized[9]
        self.physicalBiology = digitized[10]
        self.procrastinating = digitized[11]
        self.crying = digitized[12]

        firstNames = ['Tony', 'Johnny', 'Jackie', 'Bobby', 'Davey', 'Ricky', 'Lucas', 'Yuri', 'Sam', 'Lesley', 'Rose', 'Michelle', 'Anna', 'Alice', 'Mia', 'Ophelia', 'Jessy', 'Lily', 'Ava', 'Isabelle', 'Layla', 'Leo']
        nickNames = ['"No Class"', '"The Nose"', '"Lucky"', '"Crusty Lips"', '"Handsome"', '"The Crimson Chin"', '"Golden"', '"The Pencil"', '"Shit Pants"', '"Heart Attack"', '"Monkey"', '"Quiet Kid"', '"The Void"', '"The Red Scare"', '"Insecure"']
        lastNames = ['Black', 'White', 'Red', 'Pink', 'Purple', 'Green', 'Yellow', 'Brown', 'Gray', 'Blue', 'Orange']
        self.firstName = rnd.choice(firstNames)
        self.nickName = rnd.choice(nickNames)
        self.lastName = rnd.choice(lastNames)
        self.fullName = "%s %s %s" % (self.firstName, self.nickName, self.lastName)