
connection = True
paid = True
internet = True
online = False

# with a lot of if else statement.


def check_status():
    if connection:
        if paid:
            if internet:
                if online:
                    print('You are online! ')
                else:
                    print('You are offline')
            else:
                print('No internet...')
        else:
            print('User has not paid.')
    else:
        print('No connection')


# guard clause pattern

def check_status_with_guard_clause():
    if not connection:
        print('No connection...')
        return
    if not paid:
        print('User has not paid...')
        return
    if not internet:
        print('No internet...')
        return
    if not online:
        print('You are offline')
        return

    print('You are online!')


check_status()
check_status_with_guard_clause()

online = True

check_status()
check_status_with_guard_clause()
