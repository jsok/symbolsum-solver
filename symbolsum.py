from itertools import permutations
import operator


def operator_repr(op):
    if op == operator.add:
        return "+"
    elif op == operator.sub:
        return "-"
    else:
        return "?"

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
            
            result_str = """
  {operand1}
{operator} {operand2}
{separator}
  {result}

{symbol_values} """

            print result_str.format(
                operand1=o1,
                operand2=o2,
                operator=operator_repr(operator),
                separator='-' * 8,
                result=calculated_result,
                symbol_values=solution)

if __name__ == "__main__":

    all_symbols = ['square', 'diamond', 'star', 'circle', 'hexagon', 'plus', 'triangle']

    #operand1 = ['triangle', 'plus', 'plus', 'hexagon', 'hexagon']
    #operand2 = [ 0,  'plus', 'star', 'circle', 'star']
    #result  = ['star', 'circle', 'hexagon', 'circle', 'star']

    operand1 = ['star', 'diamond', 'hexagon', 'square', 'triangle', 'circle']
    operand2 = ['square',  'circle', 'hexagon', 'star', 'triangle', 'plus']
    result  = ['circle', 'circle', 'plus', 'diamond', 'hexagon', 'star']

    solver = SymbolSumSolver(all_symbols)
    solver.solve(operand1, operator.add, operand2, result)
