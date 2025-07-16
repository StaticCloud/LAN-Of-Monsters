from enum import Enum

class Grid:
    def __init__(self):
        self.clientCoords = (1, 1)
        self.direction = 2
        self.distance = 4
        self.grid = [[]]
        self.map = [
            ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
            ["#","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","#"],
            ["#","_","#","#","#","_","#","_","#","_","#","_","#","_","#","#","#","_","#"],
            ["#","_","#","_","#","_","#","_","#","#","#","_","#","_","#","_","#","_","#"],
            ["#","_","_","_","#","_","#","_","_","_","_","_","#","_","#","_","_","_","#"],
            ["#","_","#","_","#","_","#","_","#","_","#","_","#","_","#","_","#","_","#"],
            ["#","_","#","#","#","_","#","_","#","_","#","_","#","_","#","#","#","_","#"],
            ["#","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","#"],
            ["#","_","#","_","#","_","#","#","_","#","_","#","#","_","#","_","#","_","#"],
            ["#","_","#","_","#","_","#","_","_","#","_","_","#","_","#","_","#","_","#"],
            ["#","_","#","_","#","_","_","#","_","#","_","#","_","_","#","_","#","_","#"],
            ["#","_","#","_","#","_","#","#","_","#","_","#","#","_","#","_","#","_","#"],
            ["#","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","#"],
            ["#","_","#","#","#","_","#","_","#","_","#","_","#","_","#","#","#","_","#"],
            ["#","_","#","_","#","_","#","_","#","#","#","_","#","_","#","_","#","_","#"],
            ["#","_","_","_","#","_","#","_","_","_","_","_","#","_","#","_","_","_","#"],
            ["#","_","#","_","#","_","#","_","#","#","#","_","#","_","#","_","#","_","#"],
            ["#","_","#","#","#","_","#","_","#","_","#","_","#","_","#","#","#","_","#"],
            ["#","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","#"],
            ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
        ]

        self.view = [[" " for _ in range(21)] for _ in range(21)]

        self.sprites = [
            [
                ["*","*","*","*","*","_","_","_","_","_","_","*","*","*","*"],
                ["*","*","*","*","/"," "," "," "," "," "," ","\\","*","*","*"],
                ["*","*","*","*","|"," "," "," "," "," "," ","|","*","*","*"],
                ["*","*","*","*","|","O","O"," "," ","O","O","|","*","*","*"],
                ["*","*","*","*","|","O","O"," "," ","O","O","|","*","*","*"],
                ["*","*","*","_","/"," "," "," "," "," "," ","\\","*","*","*"],
                ["*","*","/"," "," "," ","O"," "," ","O"," "," ","\\","*","*"],
                ["*","/"," "," ","O"," "," "," "," "," "," ","O"," ","\\","*"],
                ["/"," "," "," ","O","O"," ","O","O"," ","O","O"," "," ","\\"],
                ["\\"," "," "," ","O","O","O","O","O","O","O"," "," "," ","\\"],
                ["/"," ","/"," "," ","O","O","O","O","O","O"," "," "," ","/"],
                ["\\","_","\\"," "," "," ","O","O","O","O"," ","/"," "," ","\\"],
                ["*","*","/"," "," "," "," "," "," "," "," ","\\","_","_","/"],
                ["*","*","\\"," "," "," "," "," "," "," "," "," ","/","*","*"],
                ["*","*","/"," "," "," ","_","_","_"," "," "," ","/","*","*"],
                ["*","*","/"," "," "," ","/","*","\\"," "," "," ","\\","*","*"],
                ["*","*","\\","_","_","/","*","*","*","\\"," "," "," ","\\","*",],
                ["*","*","*","*","*","*","*","*","*","*","\\","_","_","/","*","*"],
            ],
            [
                ["*","*","*","_","_","_","","*","*","*"],
                ["*","*","/"," "," "," ","\\","","*","*"],
                ["*","*","|"," "," "," ","|","*","*","*"],
                ["*","*","|","O"," ","O","|","*","*","*"],
                ["*","/"," "," "," "," "," ","\\","*"],
                ["/"," ","O"," ","O"," ","O"," ","\\"],
                ["\\","_","O","O","O","O","O"," ","/"],
                ["*","_","\\","O","O","O"," ","\\","*"],
                ["*","/"," "," ","_"," "," ","/"],
                ["*","/"," ","/","*","\\","_","/","*"],
                ["*","_","/","*","*","*","*","*","*","*"]
            ],
            [
                ["*","*","_","*","*"],
                ["*","/"," ","\\","*"],
                ["*","O"," ","O","*"],
                ["/"," ","O"," ","\\"],
                ["*","_","\\","_","/"],
                ["*","*","\\","/","*"]

            ]
        ]

    def RefreshMap(self):
        self.map = [
            ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
            ["#","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","#"],
            ["#","_","#","#","#","_","#","_","#","_","#","_","#","_","#","#","#","_","#"],
            ["#","O","#","_","#","_","#","_","#","#","#","_","#","_","#","_","#","_","#"],
            ["#","_","_","_","#","_","#","_","_","_","_","_","#","_","#","_","_","_","#"],
            ["#","_","#","_","#","_","#","_","#","_","#","_","#","_","#","_","#","_","#"],
            ["#","_","#","#","#","_","#","_","#","_","#","_","#","_","#","#","#","_","#"],
            ["#","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","#"],
            ["#","_","#","_","#","_","#","#","_","#","_","#","#","_","#","_","#","_","#"],
            ["#","_","#","_","#","_","#","_","_","#","_","_","#","_","#","_","#","_","#"],
            ["#","_","#","_","#","_","_","#","_","#","_","#","_","_","#","_","#","_","#"],
            ["#","_","#","_","#","_","#","#","_","#","_","#","#","_","#","_","#","_","#"],
            ["#","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","#"],
            ["#","_","#","#","#","_","#","_","#","_","#","_","#","_","#","#","#","_","#"],
            ["#","_","#","_","#","_","#","_","#","#","#","_","#","_","#","_","#","_","#"],
            ["#","_","_","_","#","_","#","_","_","_","_","_","#","_","#","_","_","_","#"],
            ["#","_","#","_","#","_","#","_","#","#","#","_","#","_","#","_","#","_","#"],
            ["#","_","#","#","#","_","#","_","#","_","#","_","#","_","#","#","#","_","#"],
            ["#","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","#"],
            ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
        ]


    def MoveForward(self):
        if self.direction == 0:
            self.clientCoords = (self.clientCoords[0], self.clientCoords[1] - 1)
        if self.direction == 1:
            self.clientCoords = (self.clientCoords[0] + 1, self.clientCoords[1])
        if self.direction == 2:
            self.clientCoords = (self.clientCoords[0], self.clientCoords[1] + 1)
        if self.direction == 3:
            self.clientCoords = (self.clientCoords[0] - 1, self.clientCoords[1])

    def TurnLeft(self):
        self.direction = (self.direction - 1) % 4
    
    def TurnRight(self):
        self.direction = (self.direction + 1) % 4

    def UpdateMap(self):
        self.RefreshMap();
        self.map[self.clientCoords[1]][self.clientCoords[0]] = "O"
        self.GetView()
    
    def SpaceIsFree(self) -> bool:
        if self.direction == 0:
            return self.map[self.clientCoords[1] - 1][self.clientCoords[0]] != "#"
        if self.direction == 1:
            return self.map[self.clientCoords[1]][self.clientCoords[0] + 1] != "#"
        if self.direction == 2:
            return self.map[self.clientCoords[1] + 1][self.clientCoords[0]] != "#"
        if self.direction == 3:
            return self.map[self.clientCoords[1]][self.clientCoords[0] - 1] != "#"

    def GetView(self):
        self.distance = 4
        x, y = self.clientCoords

        if self.direction == 0:
            for i in range(1, self.distance):
                if self.map[y - i][x] == "#":
                    self.distance = i
                    break

            self.grid = [["_" for _ in range(3)] for _ in range(self.distance)]

            for i in range(self.distance):
                self.grid[i][0] = self.map[y - i][x + 1]
                self.grid[i][1] = self.map[y - i][x]
                self.grid[i][2] = self.map[y - i][x - 1]
        
        elif self.direction == 2:
            for i in range(1, self.distance):
                if self.map[y + i][x] == "#":
                    self.distance = i
                    break

            self.grid = [["_" for _ in range(3)] for _ in range(self.distance)]
            
            for i in range(self.distance):
                self.grid[i][0] = self.map[y + i][x - 1]
                self.grid[i][1] = self.map[y + i][x]
                self.grid[i][2] = self.map[y + i][x + 1]
        
        elif self.direction == 1:
            for i in range(1, self.distance):
                if self.map[y][x + i] == "#":
                    self.distance = i
                    break
             
            self.grid = [["_" for _ in range(3)] for _ in range(self.distance)]
            
            for i in range(self.distance):
                self.grid[i][0] = self.map[y + 1][x + i]
                self.grid[i][1] = self.map[y][x + i]
                self.grid[i][2] = self.map[y - 1][x + i]
        
        elif self.direction == 3:
            for i in range(1, self.distance):
                if self.map[y][x - i] == "#":
                    self.distance = i
                    break

            self.grid = [["_" for _ in range(3)] for _ in range(self.distance)]

            for i in range(self.distance):
                self.grid[i][0] = self.map[y - 1][x - i]
                self.grid[i][1] = self.map[y][x - i]
                self.grid[i][2] = self.map[y + 1][x - i]
        
        self.ClearView()

        for row in range(self.distance - 1, -1, -1):
            for col in range(3):
                self.DrawView(row, col)

    
    def DrawView(self, row, col): 
        if row == 2:
            if self.grid[row][col] == "_":
                if col == 2:
                    self.DrawWall(6, 8, 4, 3, Wall.NONE)
                elif col == 1 and self.distance == 3:
                    self.DrawWall(8, 8, 4, 3, Wall.NONE)
                elif col == 0:
                    self.DrawWall(11, 8, 4, 3, Wall.NONE)
            elif self.grid[row][col] == "#":
                if col == 2:
                    self.DrawWall(6, 6, 8, 3, Wall.LEFT)
                if col == 1: 
                    self.DrawWall(8, 8, 4, 3, Wall.NONE)
                if col == 0:
                    self.DrawWall(13, 6, 8, 3, Wall.RIGHT) 
        elif row == 1:
            if self.grid[row][col] == "_":
                if col == 2:
                    self.DrawWall(3, 6, 8, 3, Wall.NONE)
                elif col == 1 and self.distance == 2:
                    self.DrawWall(6, 6, 8, 8, Wall.NONE)
                elif col == 0:
                    self.DrawWall(14, 6, 8, 3, Wall.NONE)
            elif self.grid[row][col] == "#":
                if col == 2:
                    self.DrawWall(3, 3, 14, 3, Wall.LEFT)
                elif col == 1:
                    self.DrawWall(6, 6, 8, 8, Wall.NONE)
                elif col == 0:
                    self.DrawWall(16, 3, 14, 3, Wall.RIGHT)
                
        elif row == 0:
            if self.grid[row][col] == "_":
                if col == 2:
                    self.DrawWall(0, 3, 14, 3, Wall.NONE)
                elif col == 1 and self.distance == 1:
                    self.DrawWall(3, 3, 14, 14, Wall.NONE)
                elif col == 0:
                    self.DrawWall(17, 3, 14, 3, Wall.NONE)
            elif self.grid[row][col] == "#" or self.grid[row][col] == "O":
                if col == 2:
                    self.DrawWall(0, 0, 20, 3, Wall.LEFT)
                elif col == 1 and self.distance == 1:
                    self.DrawWall(3, 3, 14, 14, Wall.NONE)
                elif col == 0:
                    self.DrawWall(19, 0, 20, 3, Wall.RIGHT)
            
            if col == 2:
                if len(self.grid) > 1 and self.grid[1][col - 1] == "O":
                    self.RenderMonster(2, 2, self.sprites[0])
                elif len(self.grid) > 2 and self.grid[2][col - 1] == "O":
                    self.RenderMonster(6, 4, self.sprites[1])
                elif len(self.grid) > 3 and self.grid[3][col - 1] == "O":
                    self.RenderMonster(8, 6, self.sprites[2])

    def DrawWall(self, x, y, height, length, wall):
        if wall != Wall.NONE:
            for i in range(length):
                for j in range(height - (i * 2)):
                    if wall == Wall.LEFT:
                        self.view[y + j + i][x + i] = "\\"
                    if wall == Wall.RIGHT:
                        self.view[y + j + i][x - i] = "/"
        else:
            for i in range(length):
                for j in range(height):
                    self.view[y + j][x + i] = "#"
                    
    def ClearView(self):
        self.view = [[" " for _ in range(21)] for _ in range(21)]

    def RenderView(self):
        view = ""
        for i in range(20):
            for j in range(20):
                view += self.view[i][j] + " "
            view += "\n"
        
        return view
    
    def RenderMonster(self, x, y, sprite):
        for i in range(len(sprite)):
            for j in range(len(sprite[i])):
                if sprite[i][j] != "*":
                    self.view[y + i][x + j] = sprite[i][j]

    def RenderMap(self):
        self.UpdateMap()
        
        return f'{self.RenderView()}'

class Wall(Enum):
    LEFT = 0
    NONE = 1
    RIGHT = 2