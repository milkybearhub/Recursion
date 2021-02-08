import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
    
    def getLength(self):
        return math.sqrt((self.endPoint.x - self.startPoint.x)**2 +
                         (self.endPoint.y - self.startPoint.y)**2)

    def getSlope(self):
        if self.endPoint.x - self.startPoint.x  == 0:
            return None  # y軸に平行
        return (self.endPoint.y - self.startPoint.y) / (self.endPoint.x - self.startPoint.x)

    def deltaX(self):
        return abs(self.endPoint.x - self.startPoint.x)
    
    def deltaY(self):
        return abs(self.endPoint.y - self.startPoint.y)

class QuadrilateralShape:
    def __init__(self, lineA, lineB, lineC, lineD):
        self.lineA = lineA
        self.lineB = lineB
        self.lineC = lineC
        self.lineD = lineD

    # 四辺形の名称を返す
    def getShapeType(self):
        if self.atLeastZeroLineLength() or self.atLeastOneCollinear():
            return "not a quadrilateral"

        if self.lineA.getLength() == self.lineB.getLength() == self.lineC.getLength() == self.lineD.getLength():
            return "square(正方形)" if self.getAngle("BAD") == 90 else "rhombus(ひし形)"

        if self.getAngle("BAD") == self.getAngle("ABC") == self.getAngle("ADC") == 90:
            return "rectangle(長方形)"

        if (self.lineA.getSlope() == self.lineC.getSlope() and
            self.lineB.getSlope() == self.lineD.getSlope()):
            return "parallelogram(平行四辺形)"

        if (self.lineA.getSlope() == self.lineC.getSlope() or
            self.lineB.getSlope() == self.lineD.getSlope()):
            return "trapezoid(台形)"

        # 隣り合う辺の長さが等しい
        if ((self.lineA.getLength() == self.lineB.getLength() and
             self.lineC.getLength() == self.lineD.getLength()) or
            (self.lineA.getLength() == self.lineD.getLength() and
             self.lineB.getLength() == self.lineC.getLength())):
            return "kite(凧)"

        return "other（その他）"

    # 同一座標の判定
    def atLeastZeroLineLength(self):
        self.lineA or self.lineB or self.lineC or self.lineD == 0

    # 3点が同一直線上に存在する判定
    def atLeastOneCollinear(self):
        all_angle = (
            self.getAngle("BAD"), self.getAngle("ABC"),
            self.getAngle("ADC"), self.getAngle("BCD"))
        return 0 in all_angle or 180 in all_angle

    # 四辺形の周囲の長さを返す
    def getPerimeter(self):
        return (self.lineA.getLength() +
                self.lineB.getLength() +
                self.lineC.getLength() +
                self.lineD.getLength())

    # 四辺形の面積を返す
    def getArea(self):
        if self.getShapeType() in ("square(正方形)", "rectangle(長方形)"):
            return self.lineA.getLength() * self.lineB.getLength()
        if self.getShapeType() == "rhombus(ひし形)":
            return # 対角線 * 対角線 / 2
        if self.getShapeType() == "parallelogram(平行四辺形)":
            return (self.lineA.endPoint.x - self.lineA.startPoint.x) * (self.lineB.endPoint.y - self.lineB.startPoint.y)
        if self.getShapeType() == "trapezoid(台形)":
            return (self.lineC.getLength() + self.lineA.getLength()) * (self.lineD.startPoint.y - self.lineD.endPoint.y) / 2
        if self.getShapeType() == "kite(凧)":
            return (self.lineC.startPoint.y - self.lineA.startPoint.y) * (self.lineB.startPoint.x - self.lineD.startPoint.x) / 2
        return "四辺形でないため面積を算出できません。"

    # BAD、ABC、ADC、BCDの角度を返す
    def getAngle(self, angleString):
        if angleString == "BAD":
            return self.calcAngle(self.lineA, self.lineD)
        elif angleString == "ABC":
            return self.calcAngle(self.lineB, self.lineA)
        elif angleString == "ADC":
            return self.calcAngle(self.lineD, self.lineC)
        elif angleString == "BCD":
            return self.calcAngle(self.lineC, self.lineB)

    # 角度の計算
    def calcAngle(self, line1, line2):
        inner_product = (
            (line1.endPoint.x - line1.startPoint.x) *
            (line2.startPoint.x - line1.startPoint.x) +
            (line1.endPoint.y - line1.startPoint.y) *
            (line2.startPoint.y - line1.startPoint.y))
        vector_magnitude_a = math.sqrt(
            (line1.endPoint.x - line1.startPoint.x)**2 +
            (line1.endPoint.y - line1.startPoint.y)**2)
        vector_magnitude_b = math.sqrt(
            (line2.startPoint.x - line1.startPoint.x)**2 +
            (line2.startPoint.y - line1.startPoint.y)**2)
        cos = inner_product / vector_magnitude_a / vector_magnitude_b
        return round(math.degrees(math.acos(cos)))

    # 四辺形をテキストとして描画する
    def draw(self):
        CAN_DRAW_ANGLE = (45, 90, 135)
        if ((self.getAngle("BAD") not in CAN_DRAW_ANGLE) or
            (self.getAngle("ABC") not in CAN_DRAW_ANGLE) or
            (self.getAngle("ADC") not in CAN_DRAW_ANGLE) or
            (self.getAngle("BCD") not in CAN_DRAW_ANGLE)):
            return print("描画に対応していない四辺形です。")

        map_size = self.createMap()
        self.replaceLine(map_size, lineA)
        self.replaceLine(map_size, lineB)
        self.replaceLine(map_size, lineC)
        self.replaceLine(map_size, lineD)
        for row in map_size[::-1]:
            for dot in row:
                print(dot, end="")
            print("")

    def createMap(self):
        # 描画の都合で上下両端を拡張するため+2
        width = (max([self.lineA.endPoint.x, self.lineC.startPoint.x]) -
                 min([self.lineA.startPoint.x, self.lineD.startPoint.x])) + 2
        height = (max([self.lineB.endPoint.y, self.lineD.startPoint.y]) -
                  min([self.lineA.startPoint.y, self.lineB.startPoint.y])) + 2
        return [["　　"] * width for i in range(height)]

    # 空のマップを辺に置換する
    def replaceLine(self, map_size, line):
        if line.deltaX() == 0:
            for i in range(line.deltaY()):
                if line.startPoint.x == 0:
                    map_size[line.endPoint.y+i+1][line.startPoint.x] = "｜　"
                else:
                    map_size[line.startPoint.y+i+1][line.startPoint.x+1] = "｜"
        else:
            for i in range(line.deltaX()):
                if line.getSlope() == -1:
                    if line == lineA:
                        map_size[i+1][line.endPoint.x-i] = "＼　"
                    elif line == lineB or line == lineC:
                        map_size[line.startPoint.y+i+1][line.startPoint.x-i] = "＼　"
                    else: # lineD
                        map_size[i+1][line.deltaX()-i] = "＼　"
                elif line.getSlope() == 0:
                    if line == lineA:
                        map_size[line.startPoint.y][line.startPoint.x+i+1] = "﹉　"
                    else: # lineC
                        map_size[line.endPoint.y+1][line.endPoint.x+i+1] = "﹍　"
                elif line.getSlope() == 1:
                    if line == lineA or line == lineB:
                        map_size[line.startPoint.y+i+1][line.startPoint.x+i+1] = "／　"
                    elif line == lineC:
                        map_size[line.endPoint.y+i+1][line.endPoint.x+i+1] = "／　"
                    else: # lineD
                        map_size[i+1][line.endPoint.x+i+1] = "／　"

        return map_size

    # 四辺形の情報をターミナルに出力
    def printInfo(self):
        return print(
            f"名称：{self.getShapeType()}\n",
            f"周囲の長さ：{self.getPerimeter()}\n",
            f"面積：{self.getArea()}\n",
            f"角BAD：{self.getAngle('BAD')}°\n",
            f"角ABC：{self.getAngle('ABC')}°\n",
            f"角ADC：{self.getAngle('ADC')}°\n",
            f"角BCD：{self.getAngle('BCD')}°",
        )


# square（正方形）
# 　　﹍　﹍　﹍　﹍　﹍　　
# ｜　　　　　　　　　　　｜
# ｜　　　　　　　　　　　｜
# ｜　　　　　　　　　　　｜
# ｜　　　　　　　　　　　｜
# ｜　　　　　　　　　　　｜
# 　　﹉　﹉　﹉　﹉　﹉　　
lineA = Line(Point(0, 0), Point(5, 0))
lineB = Line(Point(5, 0), Point(5, 5))
lineC = Line(Point(5, 5), Point(0, 5))
lineD = Line(Point(0, 5), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# rectangle（長方形）
# 　　﹍　﹍　﹍　﹍　﹍　﹍　﹍　﹍　　
# ｜　　　　　　　　　　　　　　　　　｜
# ｜　　　　　　　　　　　　　　　　　｜
# ｜　　　　　　　　　　　　　　　　　｜
# ｜　　　　　　　　　　　　　　　　　｜
# ｜　　　　　　　　　　　　　　　　　｜
# 　　﹉　﹉　﹉　﹉　﹉　﹉　﹉　﹉　　
lineA = Line(Point(0, 0), Point(8, 0))
lineB = Line(Point(8, 0), Point(8, 5))
lineC = Line(Point(8, 5), Point(0, 5))
lineD = Line(Point(0, 5), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo() 
quadrilateral.draw()

# 平行四辺形1
# 　　　　　　　
# 　　　　／　｜
# 　　／　　　｜
# ｜　　　　　｜
# ｜　　　　　｜
# ｜　　　／　　
# ｜　／　
#
lineA = Line(Point(0, 0), Point(2, 2))
lineB = Line(Point(2, 2), Point(2, 6))
lineC = Line(Point(2, 6), Point(0, 4))
lineD = Line(Point(0, 4), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# ｜　＼
# ｜　　　＼
# ｜　　　　　｜
# ｜　　　　　｜
# 　　＼　　　｜　
# 　　　　＼　｜　
#
lineA = Line(Point(0, 2), Point(2, 0))
lineB = Line(Point(2, 0), Point(2, 4))
lineC = Line(Point(2, 4), Point(0, 6))
lineD = Line(Point(0, 6), Point(0, 2))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()


# 平行四辺形
# parallelogram(平行四辺形)
# 　　　　﹍　﹍　﹍　﹍　　
# 　　／　　　　　　　／　　
# ／　　　　　　　／　　　　
# ﹉　﹉　﹉　﹉　　
#
lineA = Line(Point(0, 0), Point(4, 0))
lineB = Line(Point(4, 0), Point(6, 2))
lineC = Line(Point(6, 2), Point(2, 2))
lineD = Line(Point(2, 2), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 　　﹍　﹍　﹍　﹍　　　　　　　
# 　　＼　　　　　　　＼　　　　　
# 　　　　＼　　　　　　　＼　　　
# 　　　　　　﹉　﹉　﹉　﹉　
lineA = Line(Point(2, 0), Point(6, 0))
lineB = Line(Point(6, 0), Point(4, 2))
lineC = Line(Point(4, 2), Point(0, 2))
lineD = Line(Point(0, 2), Point(2, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# trapezoid(台形)
# 　　　　﹍　﹍　　　　　　
# 　　／　　　　　＼　　　　
# ／　　　　　　　　　＼　　
# ﹉　﹉　﹉　﹉　﹉　﹉　　
lineA=Line(Point(0, 0), Point(6, 0))
lineB=Line(Point(6, 0), Point(4, 2))
lineC=Line(Point(4, 2), Point(2, 2))
lineD=Line(Point(2, 2), Point(0, 0))
quadrilateral=QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# ｜　＼
# ｜　　　＼
# ｜　　　　　｜
# ｜　　　　　｜
# ｜　　　／　
# ｜　／　　
lineA = Line(Point(0, 0), Point(2, 2))
lineB = Line(Point(2, 2), Point(2, 4))
lineC = Line(Point(2, 4), Point(0, 6))
lineD = Line(Point(0, 6), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 　　　　　　　　　　　　／　｜
# 　　　　　　　　　　／　　　｜
# 　　　　　　　　／　　　　　｜
# 　　　　　　／　　　　　／　　　
# 　　　　／　　　　　／　　　　　
# 　　／　　　　　／　　　　　　　
# 　　﹉　﹉　﹉　　　　　　　　　　
lineA = Line(Point(0, 0), Point(3, 0))
lineB = Line(Point(3, 0), Point(6, 3))
lineC = Line(Point(6, 3), Point(6, 6))
lineD = Line(Point(6, 6), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 　　﹍　﹍　﹍　﹍　﹍　﹍　　　
# 　　＼　　　　　　　　　／　　　
# 　　　　＼　　　　　／　　　　　
# 　　　　　　﹉　﹉　　　
lineA = Line(Point(2, 0), Point(4, 0))
lineB = Line(Point(4, 0), Point(6, 2))
lineC = Line(Point(6, 2), Point(0, 2))
lineD = Line(Point(0, 2), Point(2, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 　　　　／　｜
# 　　／　　　｜
# ｜　　　　　｜
# ｜　　　　　｜
# 　　＼　　　｜
# 　　　　＼　｜
lineA = Line(Point(0, 2), Point(2, 0))
lineB = Line(Point(2, 0), Point(2, 6))
lineC = Line(Point(2, 6), Point(0, 4))
lineD = Line(Point(0, 4), Point(0, 2))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 直角台形
# 　　﹍　﹍　﹍　　　　　　　　　
# ｜　　　　　　　＼　　　　　　　
# ｜　　　　　　　　　＼　　　　　
# ｜　　　　　　　　　　　＼　
# 　　﹉　﹉　﹉　﹉　﹉　﹉　　
lineA = Line(Point(0, 0), Point(6, 0))
lineB = Line(Point(6, 0), Point(3, 3))
lineC = Line(Point(3, 3), Point(0, 3))
lineD = Line(Point(0, 3), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 　　　　　　　　﹍　﹍　﹍　　　
# 　　　　　　／　　　　　　　｜
# 　　　　／　　　　　　　　　｜
# 　　／　　　　　　　　　　　｜
# 　　﹉　﹉　﹉　﹉　﹉　﹉　　　
lineA = Line(Point(0, 0), Point(6, 0))
lineB = Line(Point(6, 0), Point(6, 3))
lineC = Line(Point(6, 3), Point(3, 3))
lineD = Line(Point(3, 3), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 　　　　　　／　｜
# 　　　　／　　　｜
# 　　／　　　　　｜
# ｜　　　　　　　｜
# ｜　　　　　　　｜
# ｜　　　　　　　｜
# 　　﹉　﹉　﹉　　　
lineA = Line(Point(0, 0), Point(3, 0))
lineB = Line(Point(3, 0), Point(3, 6))
lineC = Line(Point(3, 6), Point(0, 3))
lineD = Line(Point(0, 3), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# ｜　＼　　　　　　　
# ｜　　　＼　　　　　
# ｜　　　　　＼　　　
# ｜　　　　　　　｜
# ｜　　　　　　　｜
# ｜　　　　　　　｜
# 　　﹉　﹉　﹉　　
lineA = Line(Point(0, 0), Point(3, 0))
lineB = Line(Point(3, 0), Point(3, 3))
lineC = Line(Point(3, 3), Point(0, 6))
lineD = Line(Point(0, 6), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 　　　　　　　　　　　　／　｜
# 　　　　　　　　　　／　　　｜
# 　　　　　　　　／　　　　　｜
# 　　　　　　／　　　　　　　｜
# 　　　　／　　　　　　　　　｜
# 　　／　　　　　　　　　　　｜
# 　　＼　　　　　　　　　／　　　
# 　　　　＼　　　　　／　　　　　
# 　　　　　　＼　／　　　　　
lineA = Line(Point(3, 0), Point(6, 3))
lineB = Line(Point(6, 3), Point(6, 9))
lineC = Line(Point(6, 9), Point(0, 3))
lineD = Line(Point(0, 3), Point(3, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 　　﹍　﹍　﹍　﹍　﹍　﹍　　　
# ｜　　　　　　　　　　　／　　　
# ｜　　　　　　　　　／　　　　　
# ｜　　　　　　　／　　　　　　　
# 　　﹉　﹉　﹉　　　　
lineA = Line(Point(0, 0), Point(3, 0))
lineB = Line(Point(3, 0), Point(6, 3))
lineC = Line(Point(6, 3), Point(0, 3))
lineD = Line(Point(0, 3), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 　　﹍　﹍　﹍　﹍　﹍　﹍　　　
# 　　＼　　　　　　　　　　　｜
# 　　　　＼　　　　　　　　　｜
# 　　　　　　＼　　　　　　　｜
# 　　　　　　　　﹉　﹉　﹉　　
lineA = Line(Point(3, 0), Point(6, 0))
lineB = Line(Point(6, 0), Point(6, 3))
lineC = Line(Point(6, 3), Point(0, 3))
lineD = Line(Point(0, 3), Point(3, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 　　﹍　﹍　﹍　　　
# ｜　　　　　　　｜
# ｜　　　　　　　｜
# ｜　　　　　　　｜
# 　　＼　　　　　｜
# 　　　　＼　　　｜
# 　　　　　　＼　｜
# 　　　　　　　　　　
lineA = Line(Point(0, 3), Point(3, 0))
lineB = Line(Point(3, 0), Point(3, 6))
lineC = Line(Point(3, 6), Point(0, 6))
lineD = Line(Point(0, 6), Point(0, 3))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 　　﹍　﹍　﹍　　　
# ｜　　　　　　　｜
# ｜　　　　　　　｜
# ｜　　　　　　　｜
# ｜　　　　　／　　　
# ｜　　　／　　　　　
# ｜　／　　　
lineA = Line(Point(0, 0), Point(3, 3))
lineB = Line(Point(3, 3), Point(3, 6))
lineC = Line(Point(3, 6), Point(0, 6))
lineD = Line(Point(0, 6), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 　　　　　　／　＼　　　　　　　
# 　　　　／　　　　　＼　　　　　
# 　　／　　　　　　　　　＼　　　
# ｜　　　　　　　　　　　／　　　
# ｜　　　　　　　　　／　　　　　
# ｜　　　　　　　／　　　　　　　
# ｜　　　　　／　　　　　　　　　
# ｜　　　／　　　　　　　　　　　
# ｜　／　　　　　　　　　　　　　
# 　　　　
lineA = Line(Point(0, 0), Point(6, 6))
lineB = Line(Point(6, 6), Point(3, 9))
lineC = Line(Point(3, 9), Point(0, 6))
lineD = Line(Point(0, 6), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()


# # 凧
lineA = Line(Point(0, 0), Point(5, 3))
lineB = Line(Point(5, 3), Point(0, 8))
lineC = Line(Point(0, 8), Point(-5, 3))
lineD = Line(Point(-5, 3), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# # 四辺形ではない
lineA = Line(Point(1, 1), Point(2, 2))
lineB = Line(Point(2, 2), Point(3, 3))
lineC = Line(Point(3, 3), Point(4, 4))
lineD = Line(Point(4, 4), Point(1, 1))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()
