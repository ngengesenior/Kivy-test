__author__ = "Ngenge Senior"
__date__  = "August 1 2016"

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from functools import partial

class DemoBox(BoxLayout):
    """
    Class demonstrates various methods for binding to events
    """
    def __init__(self,**kwargs):
        super(DemoBox, self).__init__(**kwargs)
        self.orientation = "vertical"
        #bind to normal event
        btn = Button(text ="Normal binding to event")
        btn.bind(on_press = self.on_event )

        #Next we bind to a standard property change event
        #it typically needs two arguments ,object and value
        btn2 = Button(text = "Normal property change event")
        btn2.bind(state = self.on_property)

        #The use of lambdas or anonymous functions to avoid creation of more functions
        btn3 = Button(text = "Using anonymous functions")
        btn3.bind(on_press = lambda x : self.on_event(None))

        #A function can also be declared that accepts variable number of positional and
        # keyword arguments and use introspection to determine what is being passed in
        btn4 = Button(text = "Use a flexible function")
        btn4.bind(on_press = self.on_anything)

        #Use of partial functions

        btn5 = Button(text = "Use of partial functions")
        btn5.bind(on_press = partial(self.on_anything,"1","2",monty = "python"))

        for but in [btn,btn2,btn3,btn4,btn5]:
            self.add_widget(but)

    def on_event(self,obj):
        print("Typically from",obj)


    def on_property(self,obj,value):
        print("Typical property change from",obj,"to",value)


    def on_anything(self,*args,**kwargs):
        print("The flexible function has *args of",str(args),
                  "and **kwargs of",str(kwargs))
class DemoApp(App):
    def build(self):
        return   DemoBox()
if __name__ == '__main__':
    DemoApp().run()

