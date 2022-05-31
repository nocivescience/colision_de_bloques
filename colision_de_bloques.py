from manim import *
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
        if self.CONFIG['label_text'] is None:
            self.CONFIG['label_text']=self.mass_to_label_text(self.CONFIG['mass'])
        Square.__init__(self,**kwargs)
        self.label=self.get_label()
        self.add(self.label)
    def get_label(self):
        label=Text(self.CONFIG['label_text'])
        label.scale(self.CONFIG['label_scale_value'])
        label.next_to(self,UP,SMALL_BUFF)
        return label
    def mass_to_label_text(self,mass):
        return '{:,}kg'.format(int(mass))
class ClackFlashes(VGroup):
    CONFIG={
        'flash_config':{
            'run_time':0.5,
            'line_length':0.1,
            'flash_radius':0.2,
        },
        'start_up_time':0,
        'min_time_between_flashes':1/30,
    }
    def __init__(self,clack_data,**kwargs):
        VGroup.__init__(self,**kwargs)
        self.flashes=[]
        last_time=0
        for location, time in clack_data:
            if (time-last_time)<self.CONFIG['min_time_between_flashes']:
                continue
            last_time=time
            flash=Flash(location,self.CONFIG['flash_config'])
            flash.begin()
            for sm in flash.mobject.family_members_with_points():
                if isinstance(sm,VMobject):
                    sm.set_stroke(YELLOW,3)
                    sm.set_stroke(WHITE,6,0.5,backgorund=True)
            flash.start_time=time
            flash.end_time=time+flash.run_time
class BlocksScene(Scene):
    CONFIG={
        'block1_config':{
            'mass':10,
            'distance':9,
            'velocity':-1,
            'width':1.6,    
        },
        'block2_config':{
            'mass':1,
            'distance':4,
            'velocity':1,
        },
    }
    def construct(self):
        blocks=self.get_blocks()
        self.play(FadeIn(blocks))
        self.wait()
    def get_blocks(self):
        blocks=self.blocks=VGroup()
        block1=self.block1=Block(**self.CONFIG['block1_config'])
        block2=self.block2=Block(**self.CONFIG['block2_config'])
        blocks.add(block1,block2)
        return blocks