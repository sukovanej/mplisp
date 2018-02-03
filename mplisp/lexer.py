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
    last = ''
    state = ''

    for ch in value:
        if last == '\n' and ch == '#':
            state = 'comment'

        if state == 'comment':
            if ch == '\n':
                state = 'normal'

            continue

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

        last = ch

    if buffer:
        yield ''.join(buffer)
