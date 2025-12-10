
class Cookie:
    def __init__(self, color):
        self.color = color
        
    def get_kelm(self):
        return self.color
    
    def set_color(self, color):
        self.color = color


cookie_new = Cookie('yellow')

print(cookie_new.get_kelm())