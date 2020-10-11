from collections import OrderedDict

from utility.printable import Printable


class Transaction(Printable):
    """A transaction which can be added to a block in the blockchain.

    Attributes:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :signature: The signature of the transaction.
        :amount: The amount of coins sent.
    """

    def __init__(self, sender, recipient, signature, amount, msg_from, msg_to=''):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature
        self.msg_from = msg_from
        self.msg_to = msg_to

    def to_ordered_dict(self):
        """Converts this transaction into a (hashable) OrderedDict."""
        return OrderedDict([('sender', self.sender),
                            ('recipient', self.recipient),
                            ('amount', self.amount),
                            ('msg_from', self.msg_from),
                            ('msg_to', self.msg_to)])
