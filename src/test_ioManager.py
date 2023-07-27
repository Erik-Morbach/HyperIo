import ioManager
import device
import pin
import debounce
import time


def test_manager():
    manager = ioManager.IoManager(0.01)

    dev = device.Device()
    
    out = pin.OutputPin(1, debounce.Debouncer(0,0,1), dev)
    out.setup()

    global currentValue
    currentValue = 0
    def notify_me(value):
        global currentValue
        currentValue = value

    manager.registerPin(out,notify_me)

    manager.startThread()
    time.sleep(0.02)
    out.set(1)
    time.sleep(0.02)
    assert currentValue == 1
    out.set(0)
    time.sleep(0.02)
    assert currentValue == 0

    manager.stopThread()

