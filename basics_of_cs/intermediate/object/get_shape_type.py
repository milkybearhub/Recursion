import math

def getShapeType(ax, ay, bx, by, cx, cy, dx, dy):
    a = {"x": ax, "y": ay}
    b = {"x": bx, "y": by}
    c = {"x": cx, "y": cy}
    d = {"x": dx, "y": dy}

    ab = math.sqrt((b["x"] - a["x"])**2 + (b["y"] - a["y"])**2)
    bc = math.sqrt((c["x"] - b["x"])**2 + (c["y"] - b["y"])**2)
    cd = math.sqrt((d["x"] - c["x"])**2 + (d["y"] - c["y"])**2)
    da = math.sqrt((a["x"] - d["x"])**2 + (a["y"] - d["y"])**2)

    if atLeastOneSameCoordinate(a, b, c, d) or atLeastOne180Degrees(a, b, c, d):
        return "not a quadrilateral"

    abc = getAngle(a, b, c)
    bcd = getAngle(b, c, d)
    cda = getAngle(c, d, a)

    if ab == bc == cd == da:
        return "square(正方形)" if abc == 90 else "rhombus(ひし形)"

    if abc == bcd == cda == 90:
        return "rectangle(長方形)"

    slope_ab = getSlope(a, b)
    slope_bc = getSlope(b, c)
    slope_cd = getSlope(c, d)
    slope_ad = getSlope(a, d)

    if slope_ab == slope_cd and slope_bc == slope_ad:
        return "parallelogram(平行四辺形)"

    if slope_ab == slope_cd or slope_bc == slope_ad:
        return "trapezoid(台形)"

    if (ab == bc and cd == da) or (ab == da and bc == cd):
        return "kite(凧)"

    return "other（その他）"

# 同一座標の判定
def atLeastOneSameCoordinate(p1, p2, p3, p4):
    return isSameCoordinate(p1, p2) or isSameCoordinate(p1, p3) or isSameCoordinate(p1, p4) or isSameCoordinate(p2, p3) or isSameCoordinate(p2, p4) or isSameCoordinate(p3, p4)

def isSameCoordinate(p1, p2):
    return p1 == p2

# 3点が同一直線上に存在する判定
def atLeastOne180Degrees(p1, p2, p3, p4):
    return isStraightLine(p1, p2, p3) or isStraightLine(p2, p3, p4) or isStraightLine(p3, p4, p1) or isStraightLine(p4, p1, p2)

def isStraightLine(p1, p2, p3):
    return getAngle(p1, p2, p3) in (0, 180)

def getAngle(p1, p2, p3):
    inner_product = (p1["x"] - p2["x"])*(p3["x"] - p2["x"]) + \
        (p1["y"] - p2["y"])*(p3["y"] - p2["y"])
    vector_magnitude_p2p1 = math.sqrt(
        (p1["x"] - p2["x"])**2 + (p1["y"] - p2["y"])**2)
    vector_magnitude_p2p3 = math.sqrt(
        (p3["x"] - p2["x"])**2 + (p3["y"] - p2["y"])**2)
    cos = inner_product / vector_magnitude_p2p1 / vector_magnitude_p2p3
    return round(math.degrees(math.acos(cos)))

def getSlope(p1, p2):
    if p2["x"] - p1["x"] == 0:
        return None  # y軸に平行
    return (p2["y"] - p1["y"]) / (p2["x"] - p1["x"])

print("四角形ではない")
print(getShapeType(1, 1, 2, 2, 3, 3, 4, 4))
print(getShapeType(1, 1, 2, 2, 3, 3, -1, -1))
print(getShapeType(0, 0, 1, 1, 0, 0, 1, 1))
print(getShapeType(0, 1, 2, 3, 3, 4, 2, 1))
print(getShapeType(-2, 1, 2, 6, 3, 4, 4, 2))
print(getShapeType(-3, 0, -2, 6, -1, 2, -2, 1))

print("\n正方形")
print(getShapeType(0, 2, 2, 2, 2, 4, 0, 4))
print(getShapeType(3, 3, 3, -3, -3, -3, -3, 3))
print(getShapeType(0, 0, 5, 5, 10, 0, 5, -5))

print("\nひし形")
print(getShapeType(0, 0, 5, 0, 8, 4, 3, 4))
print(getShapeType(-1, 2, 8, 5, 5, -4, -4, -7))
print(getShapeType(2, 7, 1, 3, -3, 2, -2, 6))

print("\n長方形")
print(getShapeType(0, 0, 5, 0, 5, 8, 0, 8))
print(getShapeType(-7, 2, 5, 6, 7, 0, -5, -4))
print(getShapeType(1, 6, -5, -2, -1, -5, 5, 3))

print("\n平行四辺形")
print(getShapeType(0, 0, 5, 0, 8, 8, 3, 8))
print(getShapeType(-1, 5, 3, 3, 6, -4, 2, -2))
print(getShapeType(-4, 3, 5, 6, 2, -2, -7, -5))

print("\n台形")
print(getShapeType(-2, 0, 5, 0, 8, 8, -1, 8))
print(getShapeType(-1, 5, -3, 1, 3, -2, 3, 3))
print(getShapeType(-3, 3, 1, 5, 4, -1, 1, -5))

print("\n凧")
print(getShapeType(0, 0, 5, 3, 0, 8, -5, 3))
print(getShapeType(-5, 7, 2, 6, 5, -3, -4, 0))
print(getShapeType(-1, 5, 3, 1, -1, -1, -5, 1))

print("\nその他")
print(getShapeType(0, 0, 1, 0, 1, 1, 4, -5))
print(getShapeType(0, 0, 8, 0, 10, 12, 2, 6))
print(getShapeType(-2, 5, 4, 2, 4, -4, -4, -4))
print(getShapeType(0, 0, 1, 2, 3, 2, 1, 1))
