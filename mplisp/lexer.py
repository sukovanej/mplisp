'''
SE - number
SE - symbols
SE - (SE SE SE ...)


EXAMPLES:
    1 -> 1
    ahoj -> ahoj
    (a ahoj) -> ( -> a -> ahoj -> )
    ((ahoj a) (a) a) -> ( -> ( -> ahoj -> a -> ) -> ( -> ) -> )
'''

def lexer(value):
    buffer = list()
    for ch in value:

        if ch == '(':
            yield ch
        elif ch in (' ', '\n', ')'):
            if buffer:
                yield ''.join(buffer)
                buffer = list()

            if ch == ')':
                yield ch
        else:
            buffer.append(ch)

    if buffer:
        yield ''.join(buffer)


def test():
    in1 = '()'
    in2 = '((1) 2)'
    in3 = '1'

    expected_out1 = ['(', ')']
    expected_out2 = ['(', '(', '1', ')', '2', ')']
    expected_out3 = ['1']

    out1 = list(lexer(in1))
    out2 = list(lexer(in2))
    out3 = list(lexer(in3))

    assert expected_out1 == out1, out1
    assert expected_out2 == out2, out2
    assert expected_out3 == out3, out3


if __name__ == '__main__':
    test()
