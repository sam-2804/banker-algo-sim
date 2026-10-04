 
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

            
    def simulate_execution(self):
        
        for proc_idx in range(len(self.need)):
            allocation_safe = True
            
            for res_idx in range(len(self.need[proc_idx])):
                if self.need[proc_idx][res_idx] > self.available[res_idx]:                        
                    allocation_safe = False
                    print(f"Process {proc_idx} is not safe")
                    print("Allocation is not safe, Requested resource is greater than available resource")
                    break
                    
                else:    
                    continue
            
            if allocation_safe:
                print(f"process {proc_idx} is safe")
                
            else:
                # WIP : Add the block of code that will allocate resources and free it up 
                continue
                
obj1 = bankerAlgo()
obj1.calculate_need()
obj1.simulate_execution()
