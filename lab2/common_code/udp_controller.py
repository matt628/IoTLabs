import socket

def udp_controller(message):
    """
    sends a message to devices in format "floor;room;device;id;operation"
    floor: f0
    room: kitchen, bathroom, living_room, bedroom
    device: c2, c3, c1, c5
    id: 1 - Led1, 2 - Led2
    operation: on, off, change 
    in all cases * means all
    """
    MCAST_GRP = "236.0.0.0"
    MCAST_PORT = 3456

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)    
    sock.sendto(message.encode('utf-8'), (MCAST_GRP, MCAST_PORT))

    # while True:
    #     line = input('Prompt ("stop" to quit): ')
    #     if line == 'stop':
    #         break
    #     print('SENT: "%s"' % line)
        
