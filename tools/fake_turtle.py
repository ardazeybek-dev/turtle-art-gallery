"""A strict stand-in for the `turtle` module that records drawing operations.

Only a subset of the real API is implemented. Anything else raises, so every
script in drawings/ is guaranteed to use calls that exist in real turtle.
"""
import math
import re

CSS_NAMES = set("""aliceblue antiquewhite aqua aquamarine azure beige bisque black blanchedalmond
blue blueviolet brown burlywood cadetblue chartreuse chocolate coral cornflowerblue cornsilk
crimson cyan darkblue darkcyan darkgoldenrod darkgray darkgreen darkgrey darkkhaki darkmagenta
darkolivegreen darkorange darkorchid darkred darksalmon darkseagreen darkslateblue darkslategray
darkslategrey darkturquoise darkviolet deeppink deepskyblue dimgray dimgrey dodgerblue firebrick
floralwhite forestgreen fuchsia gainsboro ghostwhite gold goldenrod gray green greenyellow grey
honeydew hotpink indianred indigo ivory khaki lavender lavenderblush lawngreen lemonchiffon
lightblue lightcoral lightcyan lightgoldenrodyellow lightgray lightgreen lightgrey lightpink
lightsalmon lightseagreen lightskyblue lightslategray lightslategrey lightsteelblue lightyellow
lime limegreen linen magenta maroon mediumaquamarine mediumblue mediumorchid mediumpurple
mediumseagreen mediumslateblue mediumspringgreen mediumturquoise mediumvioletred midnightblue
mintcream mistyrose moccasin navajowhite navy oldlace olive olivedrab orange orangered orchid
palegoldenrod palegreen paleturquoise palevioletred papayawhip peachpuff peru pink plum
powderblue purple red rosybrown royalblue saddlebrown salmon sandybrown seagreen seashell sienna
silver skyblue slateblue slategray slategrey snow springgreen steelblue tan teal thistle tomato
turquoise violet wheat white whitesmoke yellow yellowgreen""".split())

# Colors whose meaning differs between Tk and CSS: Tk's "gray"/"green"/"maroon"/"purple"
# are lighter than CSS's. Forbid them so the browser shows the same thing as Python.
TK_CSS_MISMATCH = {"gray", "grey", "green", "maroon", "purple"}

HEX_RE = re.compile(r"^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")
MAX_OPS = 60000


class Rec:
    def reset(self):
        self.ops = []
        self.bg = "#000000"
        self.size = (700, 700)
        self.colormode = 1.0
        self.last_style = None
        self.poly = None       # (turtle id, op list) of the open polyline
        self.segments = 0


REC = Rec()
REC.reset()


def _q(v):
    v = round(v * 2) / 2
    return int(v) if v == int(v) else v


def _color(args):
    if len(args) == 1:
        c = args[0]
    elif len(args) == 3:
        c = tuple(args)
    else:
        raise TypeError(f"bad color arguments: {args!r}")
    if isinstance(c, str):
        if HEX_RE.match(c):
            return c.lower()
        low = c.lower()
        if low in TK_CSS_MISMATCH:
            raise ValueError(f"color '{c}' looks different in Tk and browsers, use hex")
        if low not in CSS_NAMES:
            raise ValueError(f"color '{c}' is not a CSS color name, use hex")
        return low
    if isinstance(c, (tuple, list)) and len(c) == 3:
        m = REC.colormode
        vals = []
        for v in c:
            if not 0 <= v <= m:
                raise ValueError(f"color value {v} out of range for colormode {m}")
            if m == 255 and not isinstance(v, int):
                raise ValueError("colormode 255 needs integers")
            vals.append(round(v * 255 / m))
        return "#%02x%02x%02x" % tuple(vals)
    raise TypeError(f"bad color: {c!r}")


class Vec2D(tuple):
    def __new__(cls, x, y):
        return tuple.__new__(cls, (x, y))

    def __add__(self, o):
        return Vec2D(self[0] + o[0], self[1] + o[1])

    def __sub__(self, o):
        return Vec2D(self[0] - o[0], self[1] - o[1])

    def __mul__(self, o):
        if isinstance(o, Vec2D):
            return self[0] * o[0] + self[1] * o[1]
        return Vec2D(self[0] * o, self[1] * o)

    __rmul__ = __mul__

    def __abs__(self):
        return math.hypot(*self)


class _Screen:
    def setup(self, width=700, height=700, startx=None, starty=None):
        REC.size = (int(width), int(height))

    def bgcolor(self, *args):
        if not args:
            return REC.bg
        REC.bg = _color(args)

    def tracer(self, n=None, delay=None):
        return None

    def update(self):
        return None

    def title(self, s):
        return None

    def colormode(self, m=None):
        if m is None:
            return REC.colormode
        if m not in (1.0, 255):
            raise ValueError("colormode must be 1.0 or 255")
        REC.colormode = m

    def delay(self, d=None):
        return None

    def mainloop(self):
        return None

    def exitonclick(self):
        return None

    def window_width(self):
        return REC.size[0]

    def window_height(self):
        return REC.size[1]


_SCREEN = _Screen()


def Screen():
    return _SCREEN


class Turtle:
    _ids = 0

    def __init__(self):
        Turtle._ids += 1
        self._id = Turtle._ids
        self._x = 0.0
        self._y = 0.0
        self._h = 0.0
        self._down = True
        self._pc = "#000000"
        self._fc = "#000000"
        self._w = 1
        self._fill = None
        self._fill_op = None

    # --- drawing core -------------------------------------------------------
    def _emit_style(self):
        style = (self._pc, self._w)
        if REC.last_style != style:
            REC.ops.append([1, self._pc, _q(self._w) or 1])
            REC.last_style = style
            REC.poly = None

    def _go(self, x, y):
        if self._down:
            self._emit_style()
            if REC.poly is None or REC.poly[0] != self._id or REC.poly[2] != (self._x, self._y):
                op = [0, _q(self._x), _q(self._y)]
                REC.ops.append(op)
                REC.poly = [self._id, op, None]
            REC.poly[1].extend((_q(x), _q(y)))
            REC.poly[2] = (x, y)
            REC.segments += 1
            if REC.segments > MAX_OPS:
                raise RuntimeError("too many segments")
        if self._fill is not None:
            self._fill.append((x, y))
        self._x, self._y = x, y

    def forward(self, d):
        a = math.radians(self._h)
        self._go(self._x + d * math.cos(a), self._y + d * math.sin(a))

    def backward(self, d):
        self.forward(-d)

    def left(self, a):
        self._h = (self._h + a) % 360

    def right(self, a):
        self._h = (self._h - a) % 360

    def goto(self, x, y=None):
        if y is None:
            x, y = x
        self._go(float(x), float(y))

    def setx(self, x):
        self._go(float(x), self._y)

    def sety(self, y):
        self._go(self._x, float(y))

    def setheading(self, a):
        self._h = a % 360

    def home(self):
        self._go(0.0, 0.0)
        self._h = 0.0

    def circle(self, radius, extent=None, steps=None):
        if extent is None:
            extent = 360
        if steps is None:
            frac = abs(extent) / 360
            steps = 1 + int(min(11 + abs(radius) / 6.0, 59.0) * frac)
        w = 1.0 * extent / steps
        w2 = 0.5 * w
        l = 2.0 * radius * math.sin(math.radians(w2))
        if radius < 0:
            l, w, w2 = -l, -w, -w2
        self.left(w2)
        for _ in range(steps):
            self.forward(l)
            self.left(w)
        self.left(-w2)

    def dot(self, size=None, *color):
        if size is None:
            size = max(self._w + 4, 2 * self._w)
        c = _color(color) if color else self._pc
        REC.ops.append([3, _q(self._x), _q(self._y), _q(size), c])
        REC.poly = None
        REC.segments += 1

    def write(self, arg, move=False, align="left", font=("Arial", 8, "normal")):
        REC.ops.append([5, _q(self._x), _q(self._y), str(arg), self._pc, font[1], align,
                        font[0], font[2] if len(font) > 2 else "normal"])
        REC.poly = None
        REC.segments += 1

    def begin_fill(self):
        # Tk creates the fill polygon at begin_fill, so it sits below the outline.
        self._fill = [(self._x, self._y)]
        self._fill_op = [4, None, []]
        REC.ops.append(self._fill_op)
        REC.poly = None

    def end_fill(self):
        pts = self._fill or []
        op = self._fill_op
        self._fill = self._fill_op = None
        if op is None:
            return
        if len(pts) > 2:
            for x, y in pts:
                op[2] += [_q(x), _q(y)]
            op[1] = self._fc
            REC.segments += 1
        else:
            REC.ops.remove(op)

    # --- state --------------------------------------------------------------
    def penup(self):
        self._down = False

    def pendown(self):
        self._down = True

    def isdown(self):
        return self._down

    def pensize(self, w=None):
        if w is None:
            return self._w
        self._w = w

    def speed(self, s=None):
        return 0

    def hideturtle(self):
        pass

    def showturtle(self):
        pass

    def pencolor(self, *args):
        if not args:
            return self._pc
        self._pc = _color(args)

    def fillcolor(self, *args):
        if not args:
            return self._fc
        self._fc = _color(args)

    def color(self, *args):
        if not args:
            return self._pc, self._fc
        if len(args) == 2:
            self._pc = _color(args[:1])
            self._fc = _color(args[1:])
        else:
            self._pc = self._fc = _color(args)

    def heading(self):
        return self._h

    def position(self):
        return Vec2D(self._x, self._y)

    def xcor(self):
        return self._x

    def ycor(self):
        return self._y

    def distance(self, x, y=None):
        if y is None:
            x, y = x
        return math.hypot(x - self._x, y - self._y)

    def towards(self, x, y=None):
        if y is None:
            x, y = x
        return math.degrees(math.atan2(y - self._y, x - self._x)) % 360

    def getscreen(self):
        return _SCREEN

    # aliases that exist in real turtle
    fd = forward
    bk = back = backward
    lt = left
    rt = right
    setpos = setposition = goto
    seth = setheading
    pu = up = penup
    pd = down = pendown
    width = pensize
    ht = hideturtle
    st = showturtle
    pos = position


def done():
    return None


mainloop = done


def bgcolor(*a):
    return _SCREEN.bgcolor(*a)


def tracer(*a):
    return _SCREEN.tracer(*a)


def update():
    return None


def setup(*a, **k):
    return _SCREEN.setup(*a, **k)


def colormode(*a):
    return _SCREEN.colormode(*a)


def title(*a):
    return None
