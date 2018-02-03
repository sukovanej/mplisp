"""
SE - number
SE - symbols
SE - (SE SE SE ...)


EXAMPLES:
    1 -> 1
    ahoj -> ahoj
    (a ahoj) -> ( -> a -> ahoj -> )
    ((ahoj a) (a) a) -> ( -> ( -> ahoj -> a -> ) -> ( -> ) -> )
"""


def lexer(value):
    """Yield token"""
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
