import random
class Ghost(object):
    color = ''
    def __init__ (self):
        movie_list = ['white', 'yellow', 'purple', 'red']
        self.color = random.choice(movie_list)

ghost = Ghost()
print(ghost.color)