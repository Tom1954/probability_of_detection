import math


def probability(area, speed, search_width, time):
    prob = 1 - math.exp(-(speed*search_width*time/area))
    print(round(prob, 2))
    return prob


def area(prob, speed, search_width, time):
    a = -speed*search_width*time/math.log(1-prob)
    print(round(a, 2))
    return a


def speed(area, prob, search_width, time):
    s = (area*math.log(1-prob))/(-search_width*time)
    print(round(s, 2))
    return s


def search_width(area, speed, prob, time):
    sw = (area*math.log(1-prob))/(-speed*time)
    print(round(sw, 2))
    return sw


def time(area, speed, search_width, prob):
    t = (area * math.log(1 - prob))/(-speed*search_width)
    print(round(t, 2))
    return t


def main():
    prob = float(0.8)
    a = float(100000)
    s = float(300)
    sw = float(150)
    t = float(5)

    probability(a, s, sw, t)
    area(prob, s, sw, t)
    speed(a, prob, sw, t)
    search_width(a, s, prob, t)
    time(a, s, sw, prob)


if __name__ == "__main__":
    main()
