# matrix.py class
# done without numpy, but with full knowledge that numpy exists
class Matrix:
    def __init__(self,inputlist):
        self.matrix = []
        self.rows = 0
        self.columns = 0
        if type(inputlist) == list:
            for x in range(0,len(inputlist)):
                self.rows += 1
                self.matrix.append([])
                for y in inputlist[x]:
                    self.columns += 1
                    self.matrix[x].append(y)

    def __str__(self):
        result = ""
        for x in self.matrix:
            result += "["
            for y in x:
                result += str(y)+","
            result = result[:-1]
            result += "]\n"
        result = result[:-1]
        return result

    def __mul__(self,right):

        if type(right) == int:
            mat = []
            for x in range(0,len(self.matrix)):
                mat.append([])
                for y in self.matrix[x]:
                    mat[x].append(y * right)
            return Matrix(mat)
        elif type(right) == Matrix:
            mat = []
            for y in range(0,right.columns):
                mat.append([])
                for x in range(0,self.rows):
                    mat[y].append(0)
            #multiplication goes here
            
            return Matrix(mat)
    def get(self,column,row):
        return self.matrix[column][row]

    def getRow(self,row):
        return self.matrix[row]

    def getColumn(self,column):
        result = []
        for y in range(0,self.rows):
            result.append(self.matrix[y][column])
        return result
    def dotProduct(self,othermat,column,row):
        sum = 0
        for x,y in zip(self.getColumn(column),othermat.getRow(row)):
            sum += (x*y)
        return sum



                #something goes here
        #mat will have the rows of self, and the columns of right



