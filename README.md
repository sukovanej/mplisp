# MPLisp

## Installation

```bash
$ git clone https://github.com/sukovanej/mplisp
$ cd mplisp
$ pip3 install -U .
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
(map (lambda (x) (list x (* x x))) (range -5 5))
```

Apply list values as function arguments

```lisp
(apply + (range 20))
```

## Run example code

```bash
./test/run.sh
...
```

## Specification

### REPL

```lisp
$ mplisp-repl
mplisp>
```

### Expressions, lambda, define

An expression is evaluated if first item in a list is a special form or a function. Other items are evaluated 
in unspecified order. Symbol is evaluated to it's value in it's environment and a number is evaluated to it's
value.

```lisp
mplisp> 1
-> 1
mplisp> 3
-> 3
```

Expression ```(lambda (param1 param2 ...) (body))``` creates a new function. 

```lisp
mplisp> (lambda (x) x)
-> <function create_lambda.<locals>.func at 0x10be461e0>
```

New symbol in an environment can be defined using a special form ```def```. As every list must be evaluated to
a value, applied ```def``` is evaluated to None.

```lisp
mplisp> (def a 3)
-> None
mplisp> a
-> 3
```

Every symbol can be defined only once.


```lisp
mplisp> (def a 3)
-> None
mplisp> (def a 4)
-> [ error : a already defined ]
```

Knowing ```lambda``` and ```def``` forms, one can easily create a function in local environment as follow.


```lisp
mplisp> (def double (lambda (x) (* 2 x)))
-> None
prompt> double
-> <function create_lambda.<locals>.func at 0x10be46268>
prompt> (double 3)
-> 6
```

```*``` is a builtin function, it simply multiplies all arguments and returns the result. There similar
functions for basic arithmetic:

- ```+``` plus operator
- ```-``` minus operator
- ```*``` multiply
- ```/``` divide
- ```%``` modulo

### Control statements, boolean algebra

An expression can be evaluated to *bool*. `False`, `#f` and `0` are
evaluated to *false* and every other value is evaluated to *true*.


