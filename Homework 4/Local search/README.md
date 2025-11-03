# ITI0210 Foundations of Artificial Intelligence and Machine Learning



## Explanation of Local Search


#solveable1 4D
        N = 4
        self.Dimension = N

        self.field = [
            [0, 0, 1, 0],
            [0, 2, 0, 0], 
            [0, 0, 3, 0], 
            [0, 4, 0, 0]]
        self.queens = [(0, 2), (1, 1), (2, 2), (3, 1)]

#solveable2 4D
        N = 4
        self.Dimension = N
        self.field = [
            [1, 2, 3, 4], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]]
        self.queens = [(0, 0), (0, 1), (0, 2), (0, 3)]

#unslolveable 4D
        N = 4
        self.Dimension = N
         self.field = [
            [1, 0, 0, 3], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [2, 0, 0, 4]]
        self.queens = [(0, 0), (0, 3), (3, 0), (3, 3)]


#solveable 8D
        It is only solvable if there is one less. Reason for that is that iam not only taking left right up and down in consideration but also diagonaly from up left to down right (\) and from up right to down left (/) into consideration.
        This is why i use less than 8 queens here.
        N = 8
        self.Dimension = N
        self.field = [
            [1, 2, 3, 4, 5, 6, 7, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0]]
            
        self.queens = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]

#not solveable1 8D
        N = 8
        self.Dimension = N
        self.field = [  
            [1, 2, 3, 4, 5, 6, 7, 8], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0]]

        self.queens = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)], (0, 7)]

#not solveable2 8D
        N = 8
        self.Dimension = N
        self.field = [
            [1, 2, 3, 4, 5, 6, 7, 8], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0]]

        self.queens = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6) , (0, 7)]


To evaluate the solutions simply draw a line from each queen like this 
  \ |  /
   \| /
----Q----
   /|\
  / | \
