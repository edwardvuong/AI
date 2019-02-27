from map import Map

#Vaiable map size
mapSize = 19

class Robot:
    def __init__(self):
        self.start = (0, 0)
        self.track = [self.start]
    '''
    Cleans by skipping 1 row and looking at dirt in adjacent 
    locations located on the current row the row above it. 
    '''
    def clean(self, task: Map):

        #Map size is odd we must clean 1 row in order skip by 2
        start = 2
        if (mapSize%2 == 1):
            for y in range(0, mapSize):
                self.start = (0,y)
                self.track.append([0,y])  
                #Check current location on first row
                if(home.dirty[0][y] > 0):
                    home.dirty[0][y] = 0 
        #Map size is even we can close rows in quantities of 2
        else:
            y = 0
            start = 0
        #Skip every other row
        for x in range (start, mapSize, 2):
            self.start = (x - 1,y)
            self.track.append([x - 1,y])
            #Check adjacent location
            if(home.dirty[x - 1][y] > 0):
                home.dirty[x - 1][y] = 0
            #Clean from right to left
            if(y == mapSize - 1):
                for y in range(mapSize - 1, -1, -1):
                    self.start = (x,y)
                    self.track.append([x,y])
                    #Check current location
                    if(home.dirty[x][y] > 0):
                        home.dirty[x][y] = 0
                    #Check adjacent location
                    if(home.dirty[x  - 1][y] > 0):
                        self.start = (x - 1, y)
                        self.track.append ([x - 1, y])
                        home.dirty[x - 1][y] = 0
                    #Check adjacent location
                    if(home.dirty[x - 1][y-1] > 0):
                        self.start = (x - 1, y - 1)
                        self.track.append([x - 1, y - 1])
                        home.dirty[x - 1][y - 1] = 0
            #Clean from left to right
            elif(y == 0):
                for y in range(0, mapSize):
                    self.start = (x,y)
                    self.track.append([x,y])
                    #Check current location
                    if(home.dirty[x][y] > 0):
                        home.dirty[x][y] = 0
                    #Check adjacent location
                    if(home.dirty[x  - 1][y] > 0):
                        self.start = (x - 1, y)
                        self.track.append([x - 1, y])
                        home.dirty[x - 1][y] = 0
                    #Check adjacent location
                    if(home.dirty[x - 1][y - 1] > 0):
                        self.start = (x - 1, y - 1)
                        self.track.append([x - 1, y + 1])
                        home.dirty[x - 1][y - 1] = 0
  
    def show(self):
        print('STEPS:', len(self.track) - 1, '/', mapSize*mapSize, 'MAX')

if __name__ == '__main__':
    home = Map(mapSize, mapSize)
    home.show()
    print(home.is_dirty())
    agent = Robot()
    agent.clean(home)
    agent.show()
    print(home.is_dirty())
    home.show()
