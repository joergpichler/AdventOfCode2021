class Machine:
    def __init__(self) -> None:
        self._reset()
    
    def _reset(self) -> None:
        self._x = 1
        self._signal_strengths = {20:0, 60:0, 100:0, 140:0, 180:0, 220:0}
    
    def _callback(self, cycle):
        if cycle in self._signal_strengths:
            self._signal_strengths[cycle] = cycle * self._x

    def run(self, instructions):
        cycle = 0

        for i in instructions:
            cycle += 1
            if i == 'noop':
                self._callback(cycle)
                continue
            else:
                s = i.split(' ')
                if s[0] != 'addx':
                    raise Exception
                self._callback(cycle)
                cycle += 1
                self._callback(cycle)
                self._x += int(s[1])
        
        result = sum(self._signal_strengths.values())
        self._reset()
        return result

def parse(file):
    with open(file, 'r') as f:
        return [l.strip() for l in f]

def main():
    instructions = parse('test.txt')
    machine = Machine()

    assert machine.run(instructions) == 13140

    instructions = parse('input.txt')
    print(f'{machine.run(instructions)}')
    pass

if __name__ == '__main__':
    main()
