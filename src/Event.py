from enum import Enum

class Event(Enum):
    IDENTIFY = 0
    USERS = 1
    MESSAGE = 2
    PUBLICMESSAGE = 3
    CREATEROOM = 4
    INVITE = 5
    JOINROOM = 6
    ROOMESSAGE = 7
    DISCONNECT = 8
    INVALID = -1

    @classmethod
    def get_event(cls, msg):
        instructions = msg.split()
        event = instructions[0]

        if (event == 'IDENTIFY'):
            return cls.IDENTIFY

        elif (event == 'USERS'):
            return cls.USERS

        elif (event == 'MESSAGE'):
            return cls.MESSAGE

        elif (event == 'PUBLICMESSAGE'):
            return cls.PUBLICMESSAGE

        elif (event == 'CREATEROOM'):
            return cls.CREATEROOM

        elif (event == 'INVITE'):
            return cls.INVITE

        elif (event == 'JOINROOM'):
            return cls.JOINROOM

        elif (event == 'ROOMESSAGE'):
            return cls.ROOMESSAGE

        elif (event == 'DISCONNECT'):
            return cls.DISCONNECT

        else:
            return cls.INVALID
