from manim import *
from numpy import block
class Wall(Line):
    CONFIG={
        'tick_pacing':.4,
        'tick_length':.2,
        'tick_style':{
            'stroke_width':1,
            'stroke_color':WHITE,
        }
    }
    def __init__(self,height,**kwargs):
        Line.__init__(self,ORIGIN,height*UP,**kwargs)
        self.height=height
        self.add(self.CONFIG['tick'])
    def get_tick(self):
        n_lines=int(self.CONFIG['height']/self.CONFIG['tick_pacing'])
        lines=VGroup(*[
            Line(ORIGIN,self.CONFIG['tick_length']*UR).shift(
                n*self.CONFIG['tick_pacing']*UP
            )
            for n in range(n_lines)
        ])
        lines.set_style(**self.CONFIG['tick_style'])
        lines.move_to(self,DR)
        return lines
class Block(Square):
    CONFIG={
        'mass':1,
        'velocity':0,
        'width':None,
        'label_text':None,
        'label_scale_value':0.8,
        'fill_opacity':1,
        'stroke_width':2,
        'stroke_color':WHITE,
        'fill_color':None,
        'sheen_direction':UL,
        'sheen_factor':0.5,
        'sheen_direction':UL,
    }
    def __init__(self,**kwargs):
        if self.CONFIG['width'] is None:
            self.CONFIG['width']=7
        Square.__init__(self,**kwargs)
class BlocksScene(Scene):
    conf={
        
    }
    def construct(self):
        block=Block()
        block.stretch_to_fit_width(block.CONFIG['width'])
        self.play(Create(block))
        self.wait()