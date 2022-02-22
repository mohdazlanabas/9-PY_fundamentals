a = [1, 2, 3, 4]
a.append(20)
print(a)

b = [1, 2, 3, 4]
b.insert(300, 5)
print(b)

c = [1, 2, 3, 4]
b.remove(2)
print(c)

d = [1, 2, 3, 4]
d.pop()
print(d)

e = [1, 2, 3, 4]
print(e.index(1))

f = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 8]
print(e.count(8))

g = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 8]
g.sort()
print(g)
g.reverse()
print(g)

h = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for i in h:
    if i not in uniques:
        uniques.append(i)
print(uniques)

j = (1, 2, 3)
print(j[0])

h = (1, 2, 3)
#xcor = h[0]
#ycor = h[1]
# zcor = h[2
xcor, ycor, zcor = h
print(xcor, ycor, zcor)

customer = {
    "name": 'John Smith',
    'age': 30,
    'is_verified': True,
}
customer['name'] = 'Jacky Onassis'
print(customer['name'])

#phone = input('Enter Your Phone NUmber: ')
# digits_mapping = {
#    '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '0': 'Zero',}
#output = ''
# for ch in phone:
#    output += digits_mapping.get(ch, '!') + '  '
# print(output)

#message = input('Key In A Phrase For Emoji Display > ')
#k = message.split(' ')
# emojis = {
#    ':)': '😀',
#    ':(': '🙁'}
#output2 = ''
# for l in k:
#    output2 += emojis.get(l, l) + ' '
# print(output2)


def greet_user(first_name, last_name):
    print(f'Hi there {first_name} {last_name} ')
    print('Welcome aboard')


print('Start')
greet_user('John', 'Simth')
print('Finish')


def square(number3):
    return number3 * number3


result = square(3)
print(result)
print(square(4))

###


def emoji_converter(message2):
    words = message2.split(' ')
    emojis = {
        ':)': '😀',
        ':(': '🙁'
    }
    output2 = ''
    for word in words:
        output2 += emojis.get(word, word) + ' '
    return output2


message2 = input('Key In A Phrase For Emoji Display > ')
result = emoji_converter(message2)
print(result)

# EXCEPTIONS

try:
    age2 = int(input('Age: '))
    income = 20_000
    risk = income / age2
    print(age2)
except ZeroDivisionError:
    print('Age cannot Be zero')
except ValueError:
    print('Invalid Value')
