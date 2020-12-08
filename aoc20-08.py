from all_inputs import day_8

def parsed_inp(raw_inp):
    inp = raw_inp.splitlines()
    inp = [inst.split() for inst in inp]
    return [(code, int(arg)) for code, arg in inp]


class Console(object):
    def __init__(self, inp):
        self.inp = inp
        self.acc = 0
        self.index = 0
        self.index_history = set()
        
    def ex_inst(self, index):
        code, arg = self.inp[self.index] 
        
        self.index_history.add(self.index)
        if code == "nop":
            self.index += 1
        
        if code == "acc":
            self.acc += arg
            self.index += 1
        
        if code == "jmp":
            self.index += arg
            
    def run(self):
        while True:
            self.ex_inst(self.index)
            if self.index in self.index_history:
                return self.acc

            
inp = parsed_inp(day_8)
c = Console(inp)
c.run()

### Part 2 ###

from copy import copy

def parsed_inp(raw_inp):
    inp = raw_inp.splitlines()
    inp = [inst.split() for inst in inp]
    return [(code, int(arg)) for code, arg in inp]


class Console(object):
    def __init__(self, inp):
        self.inp = inp
        self.acc = 0
        self.index = 0
        self.index_history = set()
        
    def ex_inst(self, index):
        code, arg = self.inp[self.index] 
        
        self.index_history.add(self.index)
        if code == "nop":
            self.index += 1
        elif code == "acc":
            self.acc += arg
            self.index += 1
        elif code == "jmp":
            self.index += arg
            
    def run(self):
        while True:
            self.ex_inst(self.index)
            if self.index >= len(self.inp):
                return 'success', self.acc
            if self.index in self.index_history:
                return 'fail', self.acc
            
            
class Corrector(object):
    def __init__(self, inp):
        self.start_inp = inp
        
    def correct(self):
        for i, (code, arg) in enumerate(self.start_inp):
            if code == "acc":
                continue

            inp = copy(self.start_inp)
            if code == "nop":
                inp[i] = ("jmp", arg)  
            elif code == "jmp":
                inp[i] = ("nop", arg)
            
            c = Console(inp)
            result, acc = c.run()
            if result == "success":
                return acc


inp = parsed_inp(day_8)
c = Corrector(inp)
c.correct()
