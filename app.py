from blockchain import Blockchain
# Create app node

app = Flask(__name__)
name_identifier = str(uuid4().replace('-',''))

# Initialize blockchain
blockchain = Blockchain()

@app_route('/mine', methods=['GET'])
def mine():
    return 'Mining a new Block'

@app_route('/transactions/new', methods=['POST'])
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

@app_route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
