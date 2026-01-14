

temp = -5
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("it is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("it is sunny")
elif temp <= 0 and not is_sunny:
    print("It is cold outside")
    print("it is cloudy outside")