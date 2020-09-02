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
    return 'Adding a new Transaction'

@app_router('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
