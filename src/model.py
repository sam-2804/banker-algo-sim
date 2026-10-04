 
class bankerAlgo():
    
    def __init__(self):
        self.max = [
            [7,5,3],
            [3,2,2],
            [9,0,2]
        ]
        
        self.allocated =  [
            [0,1,0],
            [2,0,0],
            [3,0,2]
        ]
        
        #Default values since need is not calculated yet
        self.need = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        
        
        self.available = [3,3,2]
    
   