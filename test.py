import PiRelay6
import time


r1 = PiRelay6.Relay("RELAY1")
r2 = PiRelay6.Relay("RELAY2")
r3 = PiRelay6.Relay("RELAY3")
r4 = PiRelay6.Relay("RELAY4")
r5 = PiRelay6.Relay("RELAY5")
r6 = PiRelay6.Relay("RELAY6")

r7 = PiRelay6.Relay("RELAY7")
r8 = PiRelay6.Relay("RELAY8")
r9 = PiRelay6.Relay("RELAY9")
r10 = PiRelay6.Relay("RELAY10")
r11 = PiRelay6.Relay("RELAY11")
r12 = PiRelay6.Relay("RELAY12")


r1.off()
time.sleep(0.5)

r2.on()
time.sleep(0.5)
r2.off()
time.sleep(0.5)

r3.on()
time.sleep(0.5)
r3.off()
time.sleep(0.5)

r4.on()
time.sleep(0.5)
r4.off()
time.sleep(0.5)

r5.on()
time.sleep(0.5)
r5.off()
time.sleep(0.5)

r6.on()
time.sleep(0.5)
r6.off()
time.sleep(0.5)

r7.on()
time.sleep(0.5)
r7.off()
time.sleep(0.5)

r8.on()
time.sleep(0.5)
r8.off()
time.sleep(0.5)

r9.on()
time.sleep(0.5)
r9.off()
time.sleep(0.5)

r10.on()
time.sleep(0.5)
r10.off()
time.sleep(0.5)

r11.on()
time.sleep(0.5)
r11.off()
time.sleep(0.5)

r12.on()
time.sleep(0.5)
r12.off()
time.sleep(0.5)

