class Blockchain(object):

    def __init__(self):

        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        # This function creates new blocks and then adds to the existing chain
        '''This function will contain two variables, proof & previous_hash'''
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            previous_hash: previous_hash or self.hash(self.chain[-1]),
        }
        # set the current transaction list to empty
        self.current_transactions = []
        self.chain.append(block)
        return block

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
        '''Creates a SHA256 block hash & ensures the dictionary is ordered'''
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

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
        return self.chain[-1]
