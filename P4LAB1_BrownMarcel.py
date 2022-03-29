user_text = input()
count = 0

for character in user_text:
    if character not in ' .,!':
        count += 1
print(count)
