from bridges.bridge import BridgeController
from bridges.devices import Tv, Radio

if __name__ == "__main__":
    # When: creating devices.
    tv = Tv()
    radio = Radio()

    # And: after creating controllers for these devices.
    tv_remote = BridgeController(tv)
    radio_remote = BridgeController(radio)

    # We should be able to control the devices the same way.
    tv_remote.toggle_power()
    # output: Turning on device..
    print(tv_remote.__str__())
    # output: I'm a TV remote
    print(f"Current tv volume: {tv.volume}")
    # output: Current tv volume: 9
    tv_remote.volume_up()
    print(f"tv volume after tv_remote.volume_up(): {tv.volume}")
    # output: tv volume after tv_remote.volume_up(): 10

    print("\n")
    radio_remote.toggle_power()
    # output: Turning on device..
    print(radio_remote.__str__())
    # output: I'm a Radio remote
    print(f"Current radio channel: {radio.channel}")
    # output: Current radio channel: 1
    radio_remote.channel_up()
    print(f"radio channel after radio_remote.channel_up(): {radio.channel}")
    # output: radio channel after radio_remote.channel_up(): 2
