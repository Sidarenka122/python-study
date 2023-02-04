# О каждом учащемся класса известны его пол, год рождения, рост и вес. Определить, сколько в классе мальчиков
# и сколько девочек. Найти средний возраст мальчиков и девочек. Определить, верно ли, что самый высокий мальчик
# весит больше всех в классе, а самая маленькая девочка является самой юной среди девочек.
import datetime

def isvalidinteger(val):
    return isinstance(val, int) and val > 0


def populatepupils():
    try:
        length = int(input("Enter number of pupils \n"))
    except:
        length = 0
    ArrayOfPupils = []

    for n in range(length):
        gender = ""
        yob = 0
        height = 0
        weight = 0

        while gender not in ["m", "f"]:
            gender = str(input("Gender m/f "))

        while not isvalidinteger(yob):
            try:
                yob = int(input("Year of birth "))
            except:
                yob = 0

        while not isvalidinteger(height):
            try:
                height = int(input("Height "))
            except:
                height = 0

        while not isvalidinteger(weight):
            try:
                weight = int(input("Weight "))
            except:
                weight = 0

        pupil = {
            'gender': gender,
            'yob': yob,
            'height': height,
            'weight': weight,
        }

        ArrayOfPupils.append(pupil)

    return ArrayOfPupils

def calcstatistics():
    pupils = populatepupils()
    today = datetime.date.today()
    currentYear = today.year

    classStats = {
        "maxWeight": {
            "pupilId": -1,
            "value": 0
        },
    }
    femaleStats = {
        "count": 0,
        "totalAge": 0,
        "averageAge": 0,
        "minHeight": {
            "pupilId": -1,
            "value": 0
        },
        "minYob": {
            "pupilId": -1,
            "value": 0
        }
    }
    maleStats = {
        "count": 0,
        "totalAge": 0,
        "averageAge": 0,
        "maxHeight": {
            "pupilId": -1,
            "value": 0
        },
    }

    for n in range(len(pupils)):
        print(pupils[n])

        if pupils[n]['gender'] == "f":
            femaleStats['count'] += 1
            femaleStats['totalAge'] += currentYear - pupils[n]['yob']
            if femaleStats['minYob']['pupilId'] == -1:
                femaleStats['minHeight']['value'] = pupils[n]['height']
                femaleStats['minHeight']['pupilId'] = n
            if pupils[n]['height'] <= femaleStats['minHeight']['value']:
                femaleStats['minHeight']['value'] = pupils[n]['height']
                femaleStats['minHeight']['pupilId'] = n
            if pupils[n]['yob'] >= femaleStats['minYob']['value']:
                femaleStats['minYob']['value'] = pupils[n]['yob']
                femaleStats['minYob']['pupilId'] = n
        elif pupils[n]['gender'] == "m":
            maleStats['count'] += 1
            maleStats['totalAge'] += currentYear - pupils[n]['yob']
            if pupils[n]['height'] >= maleStats['maxHeight']['value']:
                maleStats['maxHeight']['value'] = pupils[n]['height']
                maleStats['maxHeight']['pupilId'] = n

        if pupils[n]['weight'] >= classStats['maxWeight']['value']:
            classStats['maxWeight']['value'] = pupils[n]['weight']
            classStats['maxWeight']['pupilId'] = n

    print("***** RESULT *****")
    print("Number of boys: \n" + str(maleStats['count']))
    print("Number of girls: \n" + str(femaleStats['count']))
    print("Average girls age: ")
    print("0" if femaleStats['count'] == 0 else str(femaleStats['totalAge'] / femaleStats['count']))
    print("Average boys age: ")
    print("0" if maleStats['count'] == 0 else str(maleStats['totalAge'] / maleStats['count']))
    print("Yes, the tallest boy has the biggest weight in the class" if maleStats['maxHeight']['pupilId'] == classStats['maxWeight']['pupilId'] and maleStats['maxHeight']['pupilId'] != -1 else "No, the highest boy doesn't have the biggest weight in the class")
    print("Yes, the shortest girl is the youngest among girls" if femaleStats['minHeight']['pupilId'] == femaleStats['minYob']['pupilId'] and femaleStats['minHeight']['pupilId'] != -1 else "No, he shortest girl is not the youngest among girls")

calcstatistics()

