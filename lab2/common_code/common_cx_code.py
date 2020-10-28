def is_for_me(command, who_i_am):
    print("I am: ", who_i_am)
    print("I recived command: ", command)
    for i in range(len(who_i_am)):
        if(command[i] != who_i_am[i] and command[i] != '*'):
            print("This command is not for me.")
            return False
    print("This command is for me")
    return True


def do_my_job(who, what, devices):
    """
     who: idicates which device is taking action:  1 means led1, 2 means led2
     what: one of actions: change, on, off
     devices: table of devices for which a board is responsible for (led1, led2)
    """
    if who == '*':
        device = devices
    else:
        device = devices[int(who)-1]
    
    for device in devices:
        if(what == 'change'):
            device.toggle()
        elif(what == 'on'):
            device.on()
        elif(what == 'off'):
            device.off()
        else:
            print("command is not known")


