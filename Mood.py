class Mood:
   def __init__(self):
      '''
      Constructor for this class
      Creates an object
      Everything set here is a member
      of the object instantiated
      '''
      self.mood = "Happy"

   def printMood(self):

      print("My mood is : {}".format(self.mood))
