from __future__ import print_function
import keyboard
from time import sleep

from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

temp = False


def discord_volume_down():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process:
            if not session.Process.name() == "Discord.exe":
                print(session.Process.name())
                print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
                volume.SetMasterVolume(0, None)


def discord_volume_up():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process:
            if not session.Process.name() == "Discord.exe":
                print(session.Process.name())
                print("volume.GetMasterVolume(): %s 2" % volume.GetMasterVolume())
                volume.SetMasterVolume(1, None)


while True:
    try:
        if keyboard.is_pressed('ctrl'):
            if keyboard.is_pressed(';'):
                print(" hot key pressed!")
                print(temp)
                if temp:
                    discord_volume_down()
                    temp = False
                else:
                    discord_volume_up()
                    temp = True
                sleep(0.6)
            else:
                pass
        else:
            pass
    except:
        break