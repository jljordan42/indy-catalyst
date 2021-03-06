from unittest import mock, TestCase

from ..error import MessageParseError
from ..message_factory import MessageFactory

# from ..presentations.messages.proof_request import ProofRequest


class TestMessageFactory(TestCase):
    no_type_message = {"a": "b"}
    unknown_type_message = {"@type": 1}
    test_message_type = "PROTOCOL/MESSAGE"
    test_protocol = "PROTOCOL"
    test_protocol_queries = ["*", "PROTOCOL", "PROTO*"]
    test_protocol_queries_fail = ["", "nomatch", "nomatch*"]
    test_message_handler = "fake_handler"

    def setUp(self):
        self.factory = MessageFactory()

    def test_protocols(self):
        self.factory.register_message_types(
            {self.test_message_type: self.test_message_handler}
        )
        protocols = self.factory.protocols
        assert tuple(protocols) == (self.test_protocol,)

    def test_message_type_query(self):
        self.factory.register_message_types(
            {self.test_message_type: self.test_message_handler}
        )
        for q in self.test_protocol_queries:
            matches = self.factory.protocols_matching_query(q)
            assert tuple(matches) == (self.test_protocol,)
        for q in self.test_protocol_queries_fail:
            matches = self.factory.protocols_matching_query(q)
            assert matches == ()
