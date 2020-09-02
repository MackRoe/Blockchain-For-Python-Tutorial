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
