#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tkinter as tk
import math
small_font = ("Arial",16)
large_font = ("Arial",40,"bold")
digit_font_style = ("Arial",24,"bold")
default_font_style = ("Arial",20)

off_white = "#F8FAFF"
light_gray = "#F5F5F5"
light_blue = "#CCDDFF"
label_colour = "#25265E"
white = "#FFFFFF"


# In[6]:


'''
init is a default constructor to initialise the object's state
It initialises the data members of a class when an object is created
This is run as soon as the object of the class is created

Self is another object;
the address of the calling object is passed when we call a method
this address is stored in self object
'''


# In[10]:


class Calculator:
    
    def __init__(self):  
        #creating main window of calculator app here
        self.window = tk.Tk()  #creating main window of our calculator app
        #specify the width and ht of the window
        self.window.geometry("375x667")
        #disabling the resizing of the window
        #self.window.resizable(0,0)
        self.window.title("Calculator")
        
        #create labels to current and total expressions
        #total expression is the total string of expression that appears at top
        #current expression is the part where u type into
        self.current_expression = ""
        self.total_expression=""
        
        #create a display frame and button frame
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        
        #creating a dictionary for the digit values and their position
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            '.':(4,1),0:(4,2)
        }
        #\u00f7 is the unicode value for the line and 2 dots division symbol
        self.operators = {"/":"\u00F7","*":"\u00D7","-":"-","+":"+"}
        
        for x in range(0,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            if(x!=0): #don't know why we dont do column configure for 0?
                self.buttons_frame.columnconfigure(x,weight=1)
        
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_buttons()
        
        self.total_label, self.current_label = self.create_display_labels()
        
        #to use the calc from the keyboard, we bind the keys of the keyboard to the respective methods of the calculator class
        self.bind_keys()
    
    def create_buttons(self):
        button_sin = tk.Button(self.buttons_frame,text="sin",bg = off_white,fg=label_colour,font=default_font_style
                              ,command=lambda:self.sin())
        button_sin.grid(row=1,column=4,sticky=tk.NSEW)
        
        button_cos = tk.Button(self.buttons_frame,text="cos",bg = off_white,fg=label_colour,font=default_font_style
                               ,command=lambda:self.cos())
        button_cos.grid(row=2,column=4,sticky=tk.NSEW)
        
        button_tan = tk.Button(self.buttons_frame,text="tan",bg = off_white,fg=label_colour,font=default_font_style
                               ,command=lambda:self.tan())
        button_tan.grid(row=3,column=4,sticky=tk.NSEW)
        
        button_pi = tk.Button(self.buttons_frame,text="\u03c0",bg = off_white,fg=label_colour,font=default_font_style
                             ,command=lambda:self.pi())
        button_pi.grid(row=4,column=3,sticky=tk.NSEW)
        
        button_ob = tk.Button(self.buttons_frame,text="(",bg = off_white,fg=label_colour,font=default_font_style
                             ,command=lambda:self.ob())
        button_ob.grid(row=4,column=4,sticky=tk.NSEW)
        
        button_cb = tk.Button(self.buttons_frame,text=")",bg = off_white,fg=label_colour,font=default_font_style
                             ,command=lambda:self.cb())
        button_cb.grid(row=4,column=5,sticky=tk.NSEW)
        
        button_log = tk.Button(self.buttons_frame,text="log",bg = off_white,fg=label_colour,font=default_font_style
                               ,command=lambda:self.log())
        button_log.grid(row=5,column=1,sticky=tk.NSEW)
        
        button_ln = tk.Button(self.buttons_frame,text="ln",bg = off_white,fg=label_colour,font=default_font_style
                              ,command=lambda:self.ln())
        button_ln.grid(row=5,column=2,sticky=tk.NSEW)
        
        button_inv = tk.Button(self.buttons_frame,text="\u215fx",bg = off_white,fg=label_colour,font=default_font_style
                               ,command=lambda:self.inv())
        button_inv.grid(row=5,column=3,sticky=tk.NSEW)
    
    #ONLY SINE IS IMPLEMENTED UNDER SPECIAL FUNCTIONS OF THE SCIENTIFIC CALCULATOR
    
    def sin(self):
        self.current_expression+="sin"
        self.update_current_label()
        
    def cos(self):
        self.current_expression+="cos"
        self.update_current_label()
        
    def tan(self):
        self.current_expression+="tan"
        self.update_current_label()
     
    def log(self):
        self.current_expression+="log"
        self.update_current_label()
        
    def ln(self):
        self.current_expression+="ln"
        self.update_current_label()
        
    def inv(self):
        self.current_expression+="**-1"
        self.current_expression=str(eval(self.current_expression))
        self.update_current_label()
        
    def ob(self):
        self.current_expression+="("
        self.update_current_label()
    
    def cb(self):
        self.current_expression+=")"
        self.update_current_label()
    
    def pi(self):
        self.current_expression+="π" 
        self.update_current_label()
    
    def create_display_labels(self):
        #anchor=tk.E will place the label on the east most side of the frame
        total_label = tk.Label(self.display_frame,text=self.total_expression,anchor=tk.E,bg=light_gray,fg=label_colour,
                              font=small_font)  
        total_label.pack(expand=True, fill="both")
        
        current_label = tk.Label(self.display_frame,text=self.current_expression,anchor=tk.E,bg=light_gray,fg=label_colour,
                              font=large_font)  
        current_label.pack(expand=True, fill="both")
        return total_label,current_label
    
    def create_display_frame(self):
        #we are creating this frame inside main window so we specify self.window in the argument
        #then size of the frame and background colour
        frame = tk.Frame(self.window,height=221,bg=light_gray)
        #pack the frame to main window
        #the arguments will allow the frame to expand and fill any empty space around it
        frame.pack(expand=True, fill="both")
        return frame        
    
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
   
    def create_digit_buttons(self):
        
        for digit,grid_position in self.digits.items():
            button = tk.Button(self.buttons_frame, text = str(digit),bg=white,fg=label_colour,font=digit_font_style,
                               command=lambda x=digit : self.add_to_current_expression(x))
            #sticky to make sure all buttons fill up the space?
            button.grid(row=grid_position[0],column = grid_position[1],sticky=tk.NSEW)
            
    def create_operator_buttons(self):
        i=0
        for operator,symbol in self.operators.items():
            button = tk.Button(self.buttons_frame,text=symbol,bg = off_white,fg=label_colour,font=default_font_style,
                              command=lambda x=operator:self.append_operator(x))
            button.grid(row=i,column=5,sticky=tk.NSEW)
            i+=1
    
    def create_square_button(self):
        button = tk.Button(self.buttons_frame,text="x\u00b2",bg = off_white,fg=label_colour,font=default_font_style,
                              command=lambda :self.square())
        button.grid(row=0,column=3,sticky=tk.NSEW)
        
    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame,text="\u221ax",bg = off_white,fg=label_colour,font=default_font_style,
                              command=lambda :self.sqrt())
        button.grid(row=0,column=4,sticky=tk.NSEW)
            
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame,text="Clear",bg = off_white,fg=label_colour,font=default_font_style,
                          command=lambda: self.clear())
        button.grid(row=0,column=1,columnspan=2,sticky=tk.NSEW)
        
    def create_equal_button(self):
        button = tk.Button(self.buttons_frame,text="=",bg =light_blue,fg=label_colour,font=default_font_style,
                          command=lambda: self.evaluate())
        button.grid(row=5,column=4,columnspan=2,sticky=tk.NSEW)
    
    def square(self):
        self.current_expression+=" ** 2"
        self.current_expression=str(eval(self.current_expression))
        self.update_current_label()
    
    def sqrt(self):
        self.current_expression+="**0.5"
        self.current_expression=str(eval(self.current_expression))
        self.update_current_label()
    
    def evaluate(self):
        self.total_expression+=self.current_expression
        self.update_total_label()
        self.current_expression=""
        
        expression=self.total_expression
        expression = expression.replace("sin","math.sin")
        expression = expression.replace("cos","math.cos")
        expression = expression.replace("tan","math.tan")
        expression = expression.replace("log","math.log10")
        expression = expression.replace("ln","math.log")
        expression = expression.replace("π","3.141")
        
        try:
            self.current_expression += str(eval(expression))
        except Exception as e:
            self.current_expression="Error"
        finally:
            self.update_current_label()
            
        self.total_expression=""
        self.update_total_label()
        
    def clear(self):
        self.current_expression=""
        self.total_expression=""
        self.update_current_label()
        self.update_total_label()
        
    def add_to_current_expression(self,digit):
        self.current_expression+=str(digit)
        self.update_current_label()
        
    def append_operator(self,operator):
        self.current_expression+=operator
        self.total_expression+=self.current_expression
        self.current_expression=""
        self.update_current_label()
        self.update_total_label()
        
    def update_current_label(self):
        self.current_label.config(text=self.current_expression[:11])
        
    def update_total_label(self):
        #usinf f string to update the total label so that instead of * for multiplication x is seen
        #we use the f string to convert unicode values to symbols
        expression = self.total_expression
        for operator,symbol in self.operators.items():
            expression=expression.replace(operator,f' {symbol} ')
        self.total_label.config(text=expression)
        
    def bind_keys(self):
        self.window.bind("<Return>",lambda event:self.evaluate())
        
        for key in self.digits:
            self.window.bind(str(key),lambda event, digit = key:self.add_to_current_expression(digit))
            
        for key in self.operators:
            self.window.bind(key,lambda event,operator=key : self.append_operator(operator))
        
        self.window.bind("(",lambda event: self.ob())
        self.window.bind(")",lambda event: self.cb())
        
    #creating another method called run to start the calc app
    def run(self):
        self.window.mainloop()

if __name__ == "__main__": #__name__ = __main__ only when we run this program directly i.e. not being run after being imported
    calc = Calculator() 
    calc.run()


# In[ ]:


'''
console application is one like the terminal where we get output of out programs
the user cannot interact with the console environment

we are creating a gui application where the user can interact
its an event driven program
so it can have different widgets like buttons, labels, etc.
and on clicking a button, a click event starts and the code to be executed is fetched for that button
Each widget responds to a different kind of event 

mouse move event
double click event
the above two are user events

system event ex: at midnight backup all files
this event is tied to the clock and not dependent on the user 

if i have 3 buttons on my gui
I will have 3 bits of code to performing the task reqd. by each button or a code to handle each click event

say I click a button, an event is started and it goes to a MECHANISM that
decides which function to be called 
there is no order in which i will click the button or what i will do in the gui
this is opposite to a console application where the program is in control of the program flow i.e. in which order what line will be executed

when we don't do anything, the MECHANISM is waiting for an event to occur
some loop in the mechanism continuously runs while waiting for an event to occur

to setup this loop and mechanism, we use window.mainloop()
'''


# In[11]:


#eval("math.cos(1)")

