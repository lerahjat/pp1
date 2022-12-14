class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        

    def tur_off(self):
        self.is_on = False

    def tur_on(self):
        self.is_on = True
    
    def show_status(self):
         
        if self.is_on == True:
            print("TV is on", f"channel {self.channel_no}")
           
        else:
            print("TV is off")
    
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
    
    def set_channels(self,channels_list,new_channel_no):
        self.new_channel_no = new_channel_no

    def new_channel_no(self,channels_list):
          self.channels_list = channels_list

    def show_channels(self):
        print(self.channels_list)
      
    

tv1 = TV()
tv1.show_status()
tv1.tur_on()
tv1.show_status()
tv1.set_channel(5)
tv1.show_status()
tv1.set_array(["TVP1", "TVP2"])
tv1.show_channels()