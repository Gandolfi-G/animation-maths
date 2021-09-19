from manim import *

class MovingFrameBox(Scene):
    def construct(self):
        text=MathTex(
            "\\text{Déterminer le PGDC de deux nombres}"
        )
        self.play(Write(text), run_time=2)
        self.wait()
        
        underline = Underline(mobject=text[0],buff=0.2)
        self.play (Create (underline),run_time=2)        
       
        self.wait(2)  
                
        self.play(
            FadeOut(text),      
            FadeOut(underline)              
        )  
#1 decomposition en nomnre premiers        
        text=MathTex(
            "\\text{1. Décomposition en facteurs premiers}"
        )
        underline = Underline(mobject=text[0],buff=0.2)
        self.play(Write(text),Create (underline), run_time=2)
        self.wait()
        self.play(
            FadeOut(text),      
            FadeOut(underline)              
        ) 
        
        nombre1=MathTex(
            "24", "="," 2"," \cdot"," 2"," \cdot"," 2"," \cdot"," 3"
        )
        nombre1.set_color_by_tex( " 2",BLUE)
        nombre1.set_color_by_tex( " 3",GREEN)
        
        nombre2=MathTex(
            "132", "="," 2"," \cdot"," 2"," \cdot"," 3"," \cdot"," 11"
        )
        nombre2.set_color_by_tex( " 2",BLUE)
        nombre2.set_color_by_tex( " 3",GREEN)
        nombre2.set_color_by_tex( "11",RED)
        VGroup(nombre1, nombre2).arrange(DOWN)
        
        self.play(Write(nombre1[0]), run_time=0.5)
        self.wait()
        self.play(Write(nombre1[1:9]), run_time=1)
        self.wait()
        self.play(Write(nombre2[0]), run_time=0.5)
        self.wait()
        self.play(Write(nombre2[1:9]), run_time=1)
        self.wait()
        
        nombre1_haut=MathTex(
             "24", "="," 2"," \cdot"," 2"," \cdot"," 2"," \cdot"," 3"
        )
        nombre1_haut.set_color_by_tex( " 2",BLUE)
        nombre1_haut.set_color_by_tex( " 3",GREEN)
        nombre2_haut=MathTex(
            "132", "="," 2"," \cdot"," 2"," \cdot"," 3"," \cdot"," 11"
        )
        nombre2_haut.set_color_by_tex( " 2",BLUE)
        nombre2_haut.set_color_by_tex( " 3",GREEN)
        nombre2_haut.set_color_by_tex( "11",RED)
        nombre1_haut.to_corner(UP + LEFT)
        nombre2_haut.to_corner(UP + RIGHT)
        self.play(
            Transform(nombre1, nombre1_haut),
            Transform(nombre2, nombre2_haut),
        )
        self.wait()
#  2 Calcul du PGDC        
        text=MathTex(
            "\\text{2. Calcul du PGDC}"
        )
        underline = Underline(mobject=text[0],buff=0.2)
        self.play(Write(text),Create (underline), run_time=2)
        self.wait()
        self.play(
            FadeOut(text),      
            FadeOut(underline)              
        ) 
        
        nombre11=MathTex(
            "24", "="," 2"," \cdot"," 2"," \cdot"," 2"," \cdot"," 3"
        )
        nombre11.set_color_by_tex( " 2",BLUE)
        nombre11.set_color_by_tex( " 3",GREEN)
        
        nombre21=MathTex(
            "132", "="," 2"," \cdot"," 2"," \cdot"," 3"," \cdot"," 11"
        )
        nombre21.set_color_by_tex( " 2",BLUE)
        nombre21.set_color_by_tex( " 3",GREEN)
        nombre21.set_color_by_tex( "11",RED)
        
        nombre21.move_to([5,1,0])
        nombre11.move_to([-5,1,0])
        self.play(
            FadeOut(nombre1),  
            FadeOut(nombre2),  
            Transform(nombre1_haut,nombre11),
            Transform(nombre2_haut,nombre21),
        ) 
        self.wait(2)
        text1=MathTex(
            "\\text{On prend les facteurs premiers }", "\\text{ en commun}"
        )   

        pgdc=MathTex(
            "PGDC(24;132) =", " 2"," \cdot"," 2"," \cdot"," 3"," = ", "12"
        )
        pgdc.move_to([0,-2,0]) 
        pgdc.set_color_by_tex( " 2",BLUE)     
        pgdc.set_color_by_tex( " 3",GREEN)   
        
               
        underline = Underline(mobject=text1[1],buff=0.2)
        self.play(Write(text1), run_time=1)
        self.play (Create (underline),run_time=2)   
        self.wait()
        
        self.play(
            FadeIn (pgdc[0])
        )        
        
        framebox1 = SurroundingRectangle(nombre11[2], buff = .1)
        framebox2 = SurroundingRectangle(nombre21[2], buff = .1)
        self.play(
            FadeOut(text1),      
            FadeOut(underline),
            Create(framebox1),
            Create(framebox2),
        )
        self.wait(1)
        self.play(            
            Transform(nombre21[2], pgdc[1]),
            Transform(nombre11[2], pgdc[1]),              
        )
        self.wait(1)
        framebox1 = SurroundingRectangle(nombre11[4], buff = .1)
        framebox2 = SurroundingRectangle(nombre21[4], buff = .1)
        self.play(            
            Create(framebox1),
            Create(framebox2),
        )    
        self.wait(1)        
        self.play(    
            FadeIn (pgdc[2]),      
            Transform(nombre21[4], pgdc[3]),
            Transform(nombre11[4], pgdc[3]),       
        )
        self.wait(1)
        self.play(  
            FadeIn (pgdc[4])
        )
        
        framebox1 = SurroundingRectangle(nombre11[8], buff = .1)
        framebox2 = SurroundingRectangle(nombre21[6], buff = .1)
        self.play(            
            Create(framebox1),
            Create(framebox2),
        )    
        self.wait(1)      
        self.play(              
            Transform(nombre21[6], pgdc[5]),
            Transform(nombre11[8], pgdc[5]),       
        )
        self.wait(1)
        self.play(  
            FadeIn (pgdc[6]),
            FadeIn (pgdc[7])
        )
        self.wait(3)
       
    
      
         
         