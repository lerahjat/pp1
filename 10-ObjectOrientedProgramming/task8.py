class TV():
    def __init__(self):
        self.is_on = False

    def tur_off(self):
        self.is_on = False

    def tur_on(self):
        self.is_on = True
    
    def show_status(self):
         
        if self.is_on == True:
            print("TV is on")
        else:
            print("TV is off")

tv1 = TV()
tv1.show_status()
tv1.tur_on()
tv1.show_status()

            



   

    

