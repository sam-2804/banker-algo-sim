 
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
        
        process_completion = [False] * len(self.max)
        
        while not all(process_completion):
            progress_made = False
            
            for proc_idx in range(len(self.need)):
                if process_completion[proc_idx]:
                    continue
                if not process_completion[proc_idx] and self.is_safe(proc_idx): 
                    self.release_resources(proc_idx)
                    process_completion[proc_idx] = True
                    progress_made = True
                    
                else:
                    print(f"process {proc_idx} is not safe")
            
            if progress_made:
                continue
            else:
                print("Deadlock detected")
                break
                
        if all(process_completion):
            print("System is safe")

obj1 = bankerAlgo()
obj1.calculate_need()
obj1.simulate_execution()
