# MPLisp

## Installation

```bash
git clone https://github.com/sukovanej/mplisp
cd mplisp
pip3 install .
```

## Examples

### Factorial

```lisp
(def fact
    (lambda (x)
        (if (> x 1)
            (* x (fact (- x 1)))
            1)))

(fact 20)
```

### Lists

Generating x^2 function

```lisp
(map (lambda (x) (list x (* x x))) (list-gen -5 5))
```

Apply list values as function arguments

```lisp
(apply + (list-gen 20))
```

## Run example code

```bash
mplisp tests/scripts/lambda.mplisp
mplisp tests/scripts/boolean.mplisp
mplisp tests/scripts/recursion.mplisp
...
```
