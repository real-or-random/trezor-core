# Automatically generated by pb2py
import protobuf as p


class NEMDecryptedMessage(p.MessageType):
    FIELDS = {
        1: ('payload', p.BytesType, 0),
    }
    MESSAGE_WIRE_TYPE = 76

    def __init__(
        self,
        payload: bytes = None,
        **kwargs,
    ):
        self.payload = payload
        p.MessageType.__init__(self, **kwargs)
