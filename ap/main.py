from prompt_toolkit import Application, HTML
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout import Float
from prompt_toolkit.widgets import Box, Label, Frame, MenuContainer, Checkbox, RadioList
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout import HSplit
from prompt_toolkit.layout.dimension import Dimension as D
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
bindings = KeyBindings()
        
@bindings.add('c-c')
def _(event):
    get_app().exit()

bindings.add('tab')(focus_next)
bindings.add('s-tab')(focus_previous)


class AdventurePlanning:
    
    steps = [
        'plan',
        'prep',
        'set out',
        'midjourney',
        'way home',
        'reflect',
    ]

    
    def __init__(self):
        self.selections = [ Label(text=str(x)) for x in self.steps ]
        self.selected_item = 0
        self.selections[self.selected_item].text = HTML(f'<bold>{self.steps[self.selected_item]}</bold>')
        self.label = Label(text=HTML(f'<bold>{self.selected_item}</bold>'))
        self.app = self._create_app()

        self.app.run()
        # self.layout_manager = None

        
    
    def _create_app(self):
        @bindings.add('j')
        def _(event):
            p = self.selected_item
            n = self.selected_item = self.selected_item + 1 if self.selected_item + 1 < len(self.steps) else 0
            self.selections[p].text = self.steps[p]
            self.selections[n].text = HTML(f'<bold>{self.steps[n]}</bold>')
        
        @bindings.add('k')
        def _(event):
            p = self.selected_item
            n = self.selected_item = self.selected_item - 1 if self.selected_item - 1 >= 0 else len(self.steps) - 1
            self.selections[p].text = self.steps[p]
            self.selections[n].text = HTML(f'<bold>{self.steps[n]}</bold>')

        @bindings.add('enter')
        def _(event):
            get_app().exit(result=self.selections[self.selected_item])

        frame = Frame(body=HSplit(self.selections))
        root_ctr = HSplit([
           frame
        ])

        # root_ctr = MenuContainer(body=root_ctr, menu_items=)
        
        app = Application(
            full_screen=False,
            layout=Layout(container=root_ctr),
            mouse_support=False,
            style=None,
            key_bindings=bindings
        )
        
        return app

    