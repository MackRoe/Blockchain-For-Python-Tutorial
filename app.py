import requests
from blockchain import Blockchain
from flask import Flask, request, jsonify
from uuid import uuid4
# Create app node

app = Flask(__name__)
name_identifier = str(uuid4()).replace('-','')

# Initialize blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    '''Proof of Work calculation, forge new blockchain and add it to the chain,
    reward the miner for work completed'''
    # Proof of work
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    # Reward miner
    blockchain.new_transaction(
        sender = "0",
        recipient = node_identifier,
        amount = 1
    )
    # Create new block and add to chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)
    response = {
        'message': 'The new block has been forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    # check if required data is available
    required = ['sender','recipient','amount']
    if not all(k in values for k in required):
        return 'Missing Values', 400
    # create new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient', values['amount']])
    # NOTE - square bracket placement seems odd in line above
    response = {'message':f'Transaction is scheduled to be added to Block No.{index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
