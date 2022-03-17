red = int(input())
green = int(input())
blue = int(input())

small_value = min(red, green, blue)

if red < small_value:
    red = small_value
    
elif green < small_value:
    green = small_value

elif blue < small_value:
    blue = small_value
    
red = red - small_value
green = green - small_value
blue = blue - small_value

print(red, green, blue)
