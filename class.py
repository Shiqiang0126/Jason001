class MyClass (object):
    """ text line goes there """
    version = 0.1 #class var
    def __init__(self,nm="Johe Doe"):
        """constractor function"""
        self.name = nm #instance var
        print ("Create a  class instance for", self.name)
    def showname(self):
        print( "Showname:",self.name)
        print( "Show class name:", self.__class__.__name__)
    def showver(self):
        print( "Show version:", self.version)
    def addMe2Me(self,x):
        return x+x


c = MyClass()
    
