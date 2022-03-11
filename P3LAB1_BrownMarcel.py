red = int(input())
green = int(input())
blue = int(input())

sub_color = (red, green, blue)

small_value = min(sub_color)

rwg = red - small_value
gwg = green - small_value
bwg = blue - small_value

print(rwg, gwg, bwg)