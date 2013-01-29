from itertools import permutations
import operator

class SymbolSumSolver(object):
    def __init__(self, symbols):
        self.symbols = symbols

    def _concat_symbols(self, value_list, value_map):
        # Concatenate the symbol values into a whole int
        return int(''.join(map(str,[ value_map.get(x, '') for x in value_list ]))) 

    def solve(self, operand1, operator, operand2, result):
        # Assuming each symbol can only be a single digit [0-9]
        # Try every permutation, check the result and store all solutions

        solutions = []
        value_map = { symbol: 0 for symbol in self.symbols }

        for value_perm in permutations(range(10), len(self.symbols)):

            for i, symbol in enumerate(self.symbols):
                value_map[symbol] = value_perm[i]
            
            o1 = self._concat_symbols(operand1, value_map)
            o2 = self._concat_symbols(operand2, value_map)
            calculated_result = operator(o1, o2)
            expected_result = self._concat_symbols(result, value_map)
            
            if calculated_result == expected_result:
                solutions.append(value_map.copy())

        print "Found %d solutions:" % len(solutions)
        for solution in solutions:
            o1 = self._concat_symbols(operand1, solution)
            o2 = self._concat_symbols(operand2, solution)
            calculated_result = operator(o1, o2)
            
            print "  %05d" % o1
            print "- %05d" % o2
            print " %6d" % calculated_result
            print "Therefore: %s" % solution

if __name__ == "__main__":

    all_symbols = ['star', 'circle', 'hexagon', 'plus', 'triangle']
    operand1 = [ 'triangle', 'plus', 'plus', 'hexagon', 'hexagon' ]
    operand2 = [  0,  'plus', 'star', 'circle', 'star' ]
    result  = [ 'star', 'circle', 'hexagon', 'circle', 'star' ]

    solver = SymbolSumSolver(all_symbols)
    solver.solve(operand1, operator.sub, operand2, result)
