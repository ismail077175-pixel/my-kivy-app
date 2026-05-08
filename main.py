from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.expression = ""
        layout = BoxLayout(orientation='vertical')
        
        self.screen = TextInput(font_size=32, readonly=True, halign='right')
        layout.add_widget(self.screen)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=32)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)
        
        clear_btn = Button(text='C', font_size=32, background_color=[1,0,0,1])
        clear_btn.bind(on_press=self.on_clear)
        layout.add_widget(clear_btn)
        
        return layout
    
    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += instance.text
        self.screen.text = self.expression
    
    def on_clear(self, instance):
        self.expression = ""
        self.screen.text = ""

if __name__ == '__main__':
    CalculatorApp().run()
