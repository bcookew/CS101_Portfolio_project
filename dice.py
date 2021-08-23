import random

def d20():
    random.seed(random.randint(1,1000000))
    return random.randint(1, 20)

def d12():
    random.seed(random.randint(1,1000000))
    return random.randint(1, 12)

def d10():
    random.seed(random.randint(1,1000000))
    return random.randint(1, 10)

def d8():
    random.seed(random.randint(1,1000000))
    return random.randint(1, 8)

def d6():
    random.seed(random.randint(1,1000000))
    return random.randint(1, 6)

def d4():
    random.seed(random.randint(1,1000000))
    return random.randint(1, 4)

def baddy_action():
    random.seed(random.randint(1,1000000))
    action = random.randint(1,10)
    if action in range(1,5):
        return "attack"
    elif action in range(5,8):
        return "cast spell"
    elif action in range(8,11):
        return "evade"

