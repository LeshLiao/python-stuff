
# class Car:
#     speed = 0
#     started = False
#     def start(self):
#         self.started = True
#         print("Car started, let's ride!")
#     def increase_speed(self, delta):
#         if self.started:
#             self.speed = self.speed + delta
#             print('Vrooooom!')
#         else:
#             print("You need to start the car first")
#     def stop(self):
#         self.speed = 0
#         print('Halting')

# car = Car()
# car.start()
# car.increase_speed(10)

# class ExpoMarker:
#   color = ''
#   Has_Ink = True

#   def __init__ (self, color):
#     self.color = color

#   def draw_painting(self):
#     self.Has_Ink = False
#     print("You drew a " + self.color + " art piece")

#   def test_marker(self):
#     if self.Has_Ink:
#       print('This marker has Ink!')
#     else:
#       print('It\'s out of Ink!')

# marker1 = ExpoMarker('red')
# marker2 = ExpoMarker('blue')
# marker3 = ExpoMarker('yellow')
# marker4 = ExpoMarker('black')
# marker5 = ExpoMarker('white')
# # marker.draw_painting()
# # marker.test_marker()

# all_color = [marker1, marker2, marker3, marker4, marker5]

# for student in all_color:
#   student.draw_painting()

class Marker:
    color = ''
    has_ink = False
    def __init__(self, color, has_ink = False):
        self.color = color
        self.has_ink = has_ink

class PermanentMarker(Marker):
    def __init__(self):
        pass

class DryEraseMarker(Marker):
    def __init__(self):
        pass
        # self.center_stand_out = center_stand_out
        # super().__init__()
    def Draw_On_Whiteboard(self):
        print("This word is now erasable!")

new_pen = DryEraseMarker()
new_pen.Draw_On_Whiteboard()
