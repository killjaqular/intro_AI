import random

def random_row():
    alt = random.choice(["Yes", "No"])
    bar = random.choice(["Yes", "No"])
    fri = random.choice(["Yes", "No"])
    hun = random.choice(["Yes", "No"])
    pat = random.choice(["None", "Some", "Full"])
    price = random.choice(["$", "$$", "$$$"])
    rain = random.choice(["Yes", "No"])
    res = random.choice(["Yes", "No"])
    type = random.choice(["French", "Burger", "Thai", "Italian"])
    wait = random.choice(["0-10", "10-30", "30-60", ">60"])
    target = random.choice(["T", "F"])
    return ",".join([alt,bar,fri,hun,pat,price,rain,res,type,wait,target])


with open("extrainput2.in", "w") as f:
    f.write("Alternate,Bar,Friday/Saturday,Hungry,Patrons,Price,Raining,Reservation,Type,Wait Estimate\n")
    for i in range(100):
        f.write(random_row() + "\n")
