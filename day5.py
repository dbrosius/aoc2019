FILENAME = "input5.txt"


class IntCode:

    def __init__(self, program, inputs):
        self.program = program
        self.program_it = iter(self.program)
        self.inputs = iter(inputs)
        self.outputs = []
        self.ops = {
            1: self.add_op,
            2: self.mult_op,
            3: self.input_op,
            4: self.output_op
        }

    def run(self):
        opcode = next(self.program_it)
        opcode, modes = self.process_opcode(opcode)
        while opcode != 99:
            self.ops[opcode](modes)
            opcode = next(self.program_it)
            opcode, modes = self.process_opcode(opcode)
        return self.outputs

    def load_for_math(self, modes):
        op1, op2, loc = [next(self.program_it) for _ in range(0, 3)]
        op1 = op1 if modes[0] else self.program[op1]
        op2 = op2 if modes[1] else self.program[op2]
        return op1, op2, loc

    def add_op(self, modes):
        op1, op2, loc = self.load_for_math(modes)
        self.program[loc] = op1 + op2

    def mult_op(self, modes):
        op1, op2, loc = self.load_for_math(modes)
        self.program[loc] = op1 * op2

    def input_op(self, _):
        input_val = next(self.inputs)
        loc = next(self.program_it)
        self.program[loc] = input_val

    def output_op(self, modes):
        op1 = next(self.program_it)
        output_val = op1 if modes[0] else self.program[op1]
        self.outputs.append(output_val)

    @staticmethod
    def process_opcode(opcode):
        opcode_out = opcode % 100
        values = opcode // 100
        out_values = []
        for _ in range(0, 2):
            out_values.append(values % 10)
            values = values // 10
        return opcode_out, out_values


def main():
    with open(FILENAME) as f:
        line = f.readline()
    thelist = line.split(",")
    program = [int(it) for it in thelist]
    int_code = IntCode(program, [1])
    print(int_code.run())


if __name__ == "__main__":
    main()
