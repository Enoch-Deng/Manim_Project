from manim import *

class ManimCELogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)

class BraceAnnimation(Scene):
    def construct(self):
        #self.camera.background_color = "#ece6e2"
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line) # default direction is RIGHT
        b1text = b1.get_text("Horizontal distance") # get_text() returns a TextMobject and put it on the direction of the brace
        b2 = Brace(line, direction=line.copy().rotate(PI/2).get_unit_vector()) # direction is aligned with line
        b2text = b2.get_tex("x-x_1") #get_tex() returns a TexMobject and put it on the direction of the brace
        self.add(line, dot, dot2, b1, b1text, b2, b2text)

class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        self.add(numberplane, dot, arrow)
        origintext = Text('(0,0)').next_to(dot, DOWN)
        tip_text = Text('(2,2)').next_to(arrow, UP)
        self.add(origintext, tip_text)
        
class GradientImageFromArray(Scene):
    def construct(self):
        n = 256
        imageArray = np.uint8(
            [[i * 256 / n for i in range(0, n)] for _ in range(0, n)]
        )
        image = ImageMobject(imageArray).scale(2)
        image.background_rectangle = SurroundingRectangle(image, GREEN)
        self.add(image, image.background_rectangle)

