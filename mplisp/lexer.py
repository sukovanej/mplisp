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
    line = 1

    for ch in value:
        if ch == '\n':
            line += 1

        # comment
        if ch == ';':
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
            yield (ch, line)

            if last == '`':
                yield ('quote', line)
        elif ch in (' ', '\n', ')'):

            if buffer:
                yield (''.join(buffer), line)
                buffer = list()

            if ch == ')':
                yield (ch, line)
        elif ch != '`':
            buffer.append(ch)

        last = ch

    if buffer:
        yield (''.join(buffer), line)
