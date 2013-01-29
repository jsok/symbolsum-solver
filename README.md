SymbolSum Solver
================

I haven't figured out how to do these by hand yet, but who cares, let Python do
the job!

Problem
-------

You are given an arithmetic problem where the numbers have been replaced with
symbols. Your job is to determine the number values of the symbols.

The numbers are single digits, i.e. [0-9] and all unique.

![Problem](https://raw.github.com/jsok/symbolsum-solver/master/problem.jpg)

Usage
-----

For the above problem, enter it as:
```
    # List of symbols that appear in the problem
    all_symbols = ['star', 'circle', 'hexagon', 'plus', 'triangle']

    # Direct translation of symbols
    # If you know a number, e.g. 0, leave it in and it will help speed things up
    operand1 = [ 'triangle', 'plus', 'plus', 'hexagon', 'hexagon' ]
    operand2 = [  0,  'plus', 'star', 'circle', 'star' ]
    result  = [ 'star', 'circle', 'hexagon', 'circle', 'star' ]

    # Instatiate a SymbolSumSolver and kick it off
    solver = SymbolSumSolver(all_symbols)
    solver.solve(operand1, operator.sub, operand2, result)

```

Output:
```
    Found 1 solutions:
      53388
    - 03494
      49894
    Therefore: {'plus': 3, 'circle': 9, 'hexagon': 8, 'triangle': 5, 'star': 4}
```
