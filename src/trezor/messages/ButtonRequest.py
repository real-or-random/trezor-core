# Automatically generated by pb2py
import protobuf as p


class ButtonRequest(p.MessageType):
    FIELDS = {
        1: ('code', p.UVarintType, 0),
        2: ('data', p.UnicodeType, 0),
    }
    MESSAGE_WIRE_TYPE = 26

    def __init__(
        self,
        code: int = None,
        data: str = None,
        **kwargs,
    ):
        self.code = code
        self.data = data
        p.MessageType.__init__(self, **kwargs)
