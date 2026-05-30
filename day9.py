#function chaining
"""def celsius_to_fahrenheit(celsius):
    return round ((celsius * 9/5) + 32, 1)

def is_fever(temp_c):
    return temp_c >= 37.5

def describe_temperature(temp_c):
    f= celsius_to_fahrenheit(temp_c)
    fever=is_fever(temp_c)
    status= 'FEVER' if fever else 'NORMAL'
    return f"{temp_c}°C is {f}°F and indicates {status}"

print(describe_temperature(36.5))
print(describe_temperature(38.2))
print(describe_temperature(40.0))

def get_temps():
    return [36.5, 38.2, 37.0, 40.1, 36.9,]

def analyse_all(temps):
    for t in temps:
        print(describe_temperature(t))
        
analyse_all(get_temps())
"""
"""def add(a, b):
    print (a,b)
add(20, 30)"""