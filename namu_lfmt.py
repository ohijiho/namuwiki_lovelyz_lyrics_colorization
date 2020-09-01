#!/usr/bin/env python3

COLORS = ("DB5D5D", "FFB400", "8F28BD", "FF7D91", "EC005F", "EC3B00", "31CED2", "4EC32A")
IDS = ("베이비소울|소울|1", "유지애|지애|2", "서지수|지수|3", "이미주|미주|4", "Kei|케이|5", "JIN|명은|6", "류수정|수정|7", "정예인|예인|8")

color_map = dict(((k, COLORS[i]) for i in range(len(COLORS)) for k in IDS[i].split("|")), **{"": None})

def colorize_one(color, text):
    state = 0
    i1, i2 = 0, 0
    for i in range(len(text)):
        c = text[i]
        if not c.isspace():
            if state == 0:
                i1 = i
                i2 = len(text)
                state = 1
            elif state == 1:
                i2 = i + 1
    if i1 == i2:
        return text
    return f"{text[:i1]}{{{{{{#{color} {text[i1:i2]}}}}}}}{text[i2:]}"

def blend(colors, text):
    def p():
        i = 0
        for c in text:
            if c.isspace():
                yield c
            else:
                yield colorize_one(colors[i], c)
                i = (i + 1) % len(colors)
    return "".join(p())

def colorize(color, text):
    if type(color) in {tuple, list}:
        return blend(color, text)
    elif type(color) in {str}:
        return colorize_one(color, text)
    else:
        raise RuntimeError(f"BUG: {type(color)}")

def read_all():
    def p():
        while True:
            try:
                yield input()
            except EOFError:
                break
    return "\n".join(p()) + "\n"

def main():
    initial = True
    for x in read_all().split("{"):
        splt = x.split("}")
        if not initial and len(splt) < 2:
            raise RuntimeError("No matching '}'")
        initial = False
        if len(splt) > 2:
            raise RuntimeError("No matching '{'")
        color = None
        if len(splt) == 2:
            color_splt = splt[0].split(",")
            if len(color_splt) == 1:
                color = color_map[splt[0]]
            else:
                color = [color_map[k] for k in color_splt]
        if color:
            print(colorize(color, splt[-1]), end="")
        else:
            print(splt[-1], end="")

if __name__ == "__main__":
    main()
