from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.app import App
from  kivy.properties import ListProperty

class MyWidget(BoxLayout):
    def __init__(self,**kwargs):

        super(MyWidget, self).__init__(**kwargs)
        cb = ButtonWidget()
        cb.bind(on_pressed = self.on_touch_down)
        self.add_widget(cb)

class ButtonWidget(Widget):
    pressed = ListProperty([0, 0])
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            return True
        return super(MyWidget, self).on_touch_down(touch)
    def on_pressed(self,instance,pos):
        print("pressed at {pos}".format(pos = pos))


class MyWidgetTest(App):
    def build(self):

        return MyWidget()
if __name__ == '__main__':
    MyWidgetTest().run()




