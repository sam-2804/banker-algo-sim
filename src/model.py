 
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

            
    def is_safe(self,proc_idx):
    
        allocation_safe = True
        
        for res_idx in range(len(self.need[proc_idx])):
            if self.need[proc_idx][res_idx] > self.available[res_idx]:                        
                allocation_safe = False
                break
                
            else:    
                continue
        
        if allocation_safe:
            return True
        
        else:
            return False            
                
        
    def release_resources(self,proccess_idx):
        
        for resources_idx in range(len(self.allocated[proccess_idx])):
            self.available[resources_idx] = self.available[resources_idx] + self.allocated[proccess_idx][resources_idx]
        
    
    def simulate_execution(self):
        
        for proc_idx in range(len(self.need)):
            if self.is_safe(proc_idx):
    
                print(f"{proc_idx} is safe")
                print(self.available)
                self.release_resources(proc_idx)
                
                print(f"Releasing resources of process {proc_idx} is completed")                      
                print(self.available)    
            else:
                print(f"{proc_idx} is not safe")


obj1 = bankerAlgo()
obj1.calculate_need()
obj1.simulate_execution()
