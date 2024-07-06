# It's fast because they use hashing.

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'Taiwan': 'Taipei'}

def show_all_capitals():
    print('=== capitals ===')
    for key, value in capitals.items():
        print('my key='+key+',my value='+value)

def get_capital(search_key):
    val = capitals.get(search_key)
    if val != None:
        print(val)
    else:
        print('unknown key:'+search_key)

get_capital('filipino')
print(capitals.keys())
print(capitals.values())
print(capitals.items())

show_all_capitals()

capitals.update({'AAA': 'BBB'})

show_all_capitals()

capitals.pop('AAA')

show_all_capitals()
