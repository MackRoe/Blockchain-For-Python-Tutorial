class Blockchain(object):

    def __init__(self):

        self.chain = []

        self.current_transactions = []

    def new_block(self):

        # This function creates new blocks and then adds to the existing chain

        pass

    def new_transaction(self):
        ''' Create a new transaction that will be sent to the next block.
        Contains three variables: sender, recipient, amount '''
        # This function adds a new transaction to already existing transactions
        self.current_transactions.append(
            {‘sender’: sender, ‘recipient’: recipient, ‘amount’: amount}
                )
        return self.last_block[‘index’] + 1

    @staticmethod
    def hash(block):
        # Used for hashing a blocks
        pass

    def register_node(self):
        # To register a new node and add it to the network
        pass

    def valid_proof(self):
        # To ensure whether a submitted block to the blockchain solves the
        # problem
        pass

    def valid_chain(self):
        # Check if subsequent blocks in the chain are valid
        pass

    @property
    def last_block(self):
        # calls and returns the last block of the chain
        pass
