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

### Boolean

An expression can be evaluated to *bool*. `False`, `#f` and `0` are
evaluated to *false* and every other value is evaluated to *true*.

```lisp
mplisp> #t
-> True
mplisp> #f
-> False
```

An expression can be converted to *bool* using ```->bool?``` function.

```lisp
mplisp> (->bool? 3)
-> True
mplisp> (->bool? 0)
-> False
```

Type can be checked using ```bool?``` function.

```lip
mplisp> (bool? 0)
-> False
mplisp> (bool? #t)
-> True
mplisp> (bool? 1)
-> False
mplisp> (bool? #f)
-> True
mplisp> (bool? (->bool? 1))
-> True
```

Binary logical operators:

 - ```(and? a b)``` returns *a and b*
 - ```(or? a b)``` returns *a or b*
 - ```(== a b)``` returns *a equals b*
 - ```(!= a b)``` returns *a doesnt equal b*
 - ```(> a b)``` returns *a is greater than b*
 - ```(< a b)``` returns *a is smaller than b*
 
Unary logical operators:

 - ```(not? a)``` returns *a is ```#f```*

### Control statement

```if``` form evaluates an expression depending on the condition. General form is

```lisp
(if condition expr1 expr2)
```

If the condition is evaluated to *true*, `expr1` is evaluated, otherwise `expr2` is.
Simple example is `max` function.

```lisp
mplisp> (def max (lambda (a b) (if (> a b) a b)))
-> None
mplisp> (max 1 2)
-> 2
mplisp> (max 2 1)
-> 2
```


### Strings

String are recognized by apostrophe (`'` or `"`). For example

```lisp
mplisp> "hello world"
-> hello world
mplisp> 'hello world'
-> hello world
mplisp> hello world
[ error : hello not found ]
```
