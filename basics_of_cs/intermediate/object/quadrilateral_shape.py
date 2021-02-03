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


class QuadrilateralShape:
    def __init__(self, lineA, lineB, lineC, lineD):
        self.lineA = lineA
        self.lineB = lineB
        self.lineC = lineC
        self.lineD = lineD

    # 四角形の名称を返す
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

    # 四角形の周囲の長さを返す
    def getPerimeter(self):
        return (self.lineA.getLength() +
                self.lineB.getLength() +
                self.lineC.getLength() +
                self.lineD.getLength())

    # 四角形の面積を返す
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
        return "四角形でないため面積を算出できません。"

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
        if self.getShapeType() == "square(正方形)": return self.drawSquare()
        if self.getShapeType() == "rectangle(長方形)": return self.drawRectangle()
        if self.getShapeType() == "parallelogram(平行四辺形)": return self.drawParallelogram()
        if self.getShapeType() == "trapezoid(台形)": return self.drawTrapezoid()
        return print("描画に対応していない四辺形です。")

    # 正方形の描画
    def drawSquare(self):
        length_line_a = round(self.lineA.getLength())
        print("　　" + "﹍　" * length_line_a + "　　")
        for _ in range(length_line_a):
            print("｜" + "　" * length_line_a * 2 + "　｜")
        print("　　" + "﹉　" * length_line_a + "　　")

    # 長方形の描画
    def drawRectangle(self):
        width = round(self.lineA.getLength())
        height = round(self.lineB.getLength())
        print("　　" + "﹍　" * width + "　　")
        for _ in range(height):
            print("｜" + "　" * width * 2 + "　｜")
        print("　　" + "﹉　" * width + "　　")

    # 平行四辺形の描画
    def drawParallelogram(self):
        if self.getAngle("BAD") not in (45, 135):
            return print("描画に対応していない平行四辺形です。")

        if self.getAngle("ADC") == 45:
            # x軸に平行な辺がある場合
            if self.lineC.startPoint.y == self.lineC.endPoint.y:
                return self.drawParallelogram1()
            # y軸に平行な辺がある場合
            if self.lineD.startPoint.x == self.lineD.endPoint.x:
                return self.drawParallelogram2()

        if self.getAngle("ADC") == 135:
            # x軸に平行な辺がある場合
            if self.lineC.startPoint.y == self.lineC.endPoint.y:
                return self.drawParallelogram3()
            # y軸に平行な辺がある場合
            if self.lineD.startPoint.x == self.lineD.endPoint.x:
                return self.drawParallelogram4()

    # 角ADCが45°かつx軸に平行な辺がある平行四辺形
    def drawParallelogram1(self):
        width = round(self.lineC.getLength())
        height = round(self.lineD.startPoint.y - self.lineD.endPoint.y)
        print("﹍　" * width)
        for i in range(height):
            print("　　" * i + "＼　" + "　" * width + "　＼")
        print("　" * height + "　﹉" * width)
    
    # 角ADCが45°かつy軸に平行な辺がある平行四辺形
    def drawParallelogram2(self):
        width = round(self.lineA.endPoint.x - self.lineA.startPoint.x)
        delta_y = self.lineC.endPoint.y - self.lineC.startPoint.y
        for i in range(delta_y):
            print("｜　" + "　　" * i + "＼　" + "　" * width)
        for i in range(delta_y):
            print("｜　" + "　　" * width + "｜")
        for i in range(delta_y):
            print("　　" + "　　"*i + "＼　" + "　　" * (width-i-1) + "｜")

    # 角ADCが135°かつx軸に平行な辺がある平行四辺形
    def drawParallelogram3(self):
        width = round(self.lineA.getLength())
        height = round(self.lineB.endPoint.y - self.lineB.startPoint.y)
        print("　　" * height + "﹍　" * width)
        for i in range(1, height+1):
            print("　　" * (height-i) + "／　" + "　　" * (width-1) + "／")
        print("﹉　" * width)

    # 角ADCが135°かつy軸に平行な辺がある平行四辺形
    def drawParallelogram4(self):
        width = self.lineA.endPoint.x - self.lineA.startPoint.x
        delta_y = self.lineA.endPoint.y - self.lineA.startPoint.y
        for i in range(delta_y):
            print("　　" + "　　" * (width-i-1) + "／　" + "　　" * i + "｜")
        for i in range(delta_y):
            print("｜　" + "　　" * width + "｜")
        for i in range(delta_y):
            print("｜　" + "　　" * (width-i-1) + "／　" + "　　" * i)

    # 台形の描画
    def drawTrapezoid(self):
        if self.getAngle("ADC") not in (45, 90, 135):
            return "描画に対応していない台形です。"

        # 等脚台形の描画
        if self.getAngle("ADC") == 45:
            # x軸に平行な辺がある場合
            if self.lineC.startPoint.y == self.lineC.endPoint.y:
                return self.drawTrapezoid1()
            # y軸に平行な辺がある場合
            if self.lineD.startPoint.x == self.lineD.endPoint.x:
                return self.drawTrapezoid2()

        if self.getAngle("ADC") == 135:
            # x軸に平行な辺がある場合
            if self.lineC.startPoint.y == self.lineC.endPoint.y:
                return self.drawTrapezoid3()
            # y軸に平行な辺がある場合
            if self.lineD.startPoint.x == self.lineD.endPoint.x:
                return self.drawTrapezoid4()

        # TODO: 直角台形の描画

    # 角ADCが45°かつx軸に平行な辺がある等脚台形
    def drawTrapezoid1(self):
        delta_x = abs(self.lineD.startPoint.x - self.lineD.endPoint.x)
        print("﹍　" * round(self.lineC.getLength()))
        for i in reversed(range(delta_x)):
            print("　　" * (delta_x-i-1) + "＼" + "　　" *
                  (round(self.lineA.getLength()) * (i+1)) + "　／")
        print("　　" * delta_x + "﹉　" * round(self.lineA.getLength()))

    # 角ADCが45°かつy軸に平行な辺がある等脚台形
    def drawTrapezoid2(self):
        height = abs(self.lineA.endPoint.x - self.lineA.startPoint.x)
        delta_y = abs(self.lineC.endPoint.y - self.lineC.startPoint.y)
        for i in range(delta_y):
            print("｜　" + "　　" * i + "＼")
        for i in range(round(self.lineB.getLength())):
            print("｜　" + "　　" * height + "｜")
        for i in range(delta_y):
            print("｜　" + "　　" * (height-i-1) + "／　" + "　　" * i)

    # 角ADCが135°かつx軸に平行な辺がある等脚台形
    def drawTrapezoid3(self):
        delta_x = abs(self.lineD.startPoint.x - self.lineD.endPoint.x)
        print("　　" * delta_x + "﹍　" * round(self.lineC.getLength()))
        for i in range(delta_x):
            print("　　" * (delta_x-i-1) + "／" + "　　" * (round(self.lineC.getLength()) * (i+1)) + "　＼")
        print("﹉　" * round(self.lineA.getLength()))

    # 角ADCが135°かつy軸に平行な辺がある等脚台形
    def drawTrapezoid4(self):
        height = abs(self.lineA.endPoint.x - self.lineA.startPoint.x)
        delta_y = abs(self.lineC.startPoint.y - self.lineC.endPoint.y)
        for i in range(delta_y):
            print("　　" + "　　" * (height-i-1) + "／　" + "　　" * i + "｜")
        for i in range(round(self.lineD.getLength())):
            print("｜　" + "　　" * height + "｜")
        for i in range(delta_y):
            print("　　" + "　　"*i + "＼　" + "　　" * (height-i-1) + "｜")

    # 四角形の情報をターミナルに出力
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
#
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
# ｜
# ｜　＼
# ｜　　　＼
# ｜　　　　　｜
# 　　＼　　　｜　
# 　　　　＼　｜　
# 　　　　　　｜
# 
lineA = Line(Point(0, 0), Point(2, 2))
lineB = Line(Point(2, 2), Point(2, 6))
lineC = Line(Point(2, 6), Point(0, 4))
lineD = Line(Point(0, 4), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

lineA = Line(Point(0, 2), Point(2, 0))
lineB = Line(Point(2, 0), Point(2, 4))
lineC = Line(Point(2, 4), Point(0, 6))
lineD = Line(Point(0, 6), Point(0, 2))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()


# 平行四辺形2
# parallelogram(平行四辺形)
# 　　　　﹍　﹍　﹍　﹍　　
# 　　／　　　　　　　／　　
# ／　　　　　　　／　　　　
# ﹉　﹉　﹉　﹉　　
#
# ﹍　﹍　﹍　﹍
# ＼　　　　　　＼　　
# 　　＼　　　　　　＼　　　　
# 　　　﹉　﹉　﹉　﹉
lineA = Line(Point(0, 0), Point(4, 0))
lineB = Line(Point(4, 0), Point(6, 2))
lineC = Line(Point(6, 2), Point(2, 2))
lineD = Line(Point(2, 2), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

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

# ﹍　﹍　﹍　﹍　﹍　﹍　
# ＼　　　　　　　　　／
# 　　＼　　　　　／
# 　　　　﹉　﹉　
lineA = Line(Point(0, 0), Point(2, 0))
lineB = Line(Point(2, 0), Point(4, 2))
lineC = Line(Point(4, 2), Point(-2, 2))
lineD = Line(Point(-2, 2), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 　　　　／　｜
# 　　／　　　｜
# ｜　　　　　｜
# ｜　　　　　｜
# 　　＼　　　｜
# 　　　　＼　｜
lineA = Line(Point(0, 0), Point(2, -2))
lineB = Line(Point(2, -2), Point(2, 4))
lineC = Line(Point(2, 4), Point(0, 2))
lineD = Line(Point(0, 2), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

lineA = Line(Point(0, 0), Point(6, 0))
lineB = Line(Point(6, 0), Point(3, 3))
lineC = Line(Point(3, 3), Point(0, 3))
lineD = Line(Point(0, 3), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()

# 凧
lineA = Line(Point(0, 0), Point(5, 3))
lineB = Line(Point(5, 3), Point(0, 8))
lineC = Line(Point(0, 8), Point(-5, 3))
lineD = Line(Point(-5, 3), Point(0, 0))
quadrilateral = QuadrilateralShape(lineA, lineB, lineC, lineD)
quadrilateral.printInfo()
quadrilateral.draw()
