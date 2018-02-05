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


STR_SURROUND = ["\"", "'"]
ESCAPE_CHAR = "\\"


def lexer(value):
    """Yield token"""
    buffer = list()
    last = ''
    state = 'normal'

    for ch in value:
        # comment
        if last == '\n' and ch == ';':
            state = 'comment'

        if state == 'comment':
            if ch == '\n':
                state = 'normal'

            continue

        # string
        if ch in STR_SURROUND and last != ESCAPE_CHAR:
            if state == 'normal':
                state = 'string'
            elif state == 'string':
                state = 'normal'

        if state == 'string':
            buffer.append(ch)
            continue

        # normal
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
