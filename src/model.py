 
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
    

 
    def calculate_need(self):
        
        for process in range(len(self.max)):
            for resource in range(len(self.max[process])):
                self.need[process][resource] = self.max[process][resource]-self.allocated[process][resource]
    
        print(self.need)

obj1 = bankerAlgo()
obj1.calculate_need()
   