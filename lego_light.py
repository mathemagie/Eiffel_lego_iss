import logging
from curio import sleep
from bricknil import attach, start
from bricknil.hub import PoweredUpHub
from bricknil.sensor import Light

file = "lights.txt"


@attach(Light, name='light1')
@attach(Light, name='light2')

#@attach(ExternalMotor, name='motor')
# Report back when motor speed changes. You must have a motor_change method defined
#@attach(ExternalMotor, name='motor', capabilities=['sense_speed'])
class Eiffel(PoweredUpHub):

    async def motor_change(self):
         self.message_info("Running")


    async def run(self):
        self.message_info("Running")
        self.keep_running = True
        brightness = 0
        delta = 10

        while self.keep_running:
            # change the brightness up and down between -100 and 100
            brightness += delta
            if brightness >= 100:
                delta = -10
            elif brightness <= -100:
                delta = 10
            #self.message_info("Brightness: {}".format(brightness))
            light = open(file,'r')
            if light != "":
                light_resp = int(light.read())
            if light_resp:
                await self.light1.set_brightness(100)
                await self.light2.set_brightness(100)
                await sleep(0.3)
                await self.light1.set_brightness(0)
                await self.light2.set_brightness(0)
            else:
                await self.light1.set_brightness(0)
                await self.light2.set_brightness(0)


            #await self.motor.set_speed(100)   # Setting the speed
            #await self.motor.rotate(90, speed=-50) # Turn 60 degrees counter-clockwise from current position
            #await self.motor.set_pos(90, speed=20) # Turn clockwise to 3 o'clock position
            await sleep(0.3)


async def system():
    Eiffel('eiffel_light')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start(system)
