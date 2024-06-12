from flask import request, jsonify, render_template
from app import app, db
from app.models import Customer, Product, CustomerDemand, TimeWindow
from app.optimization import run_optimization

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.json
    customer = Customer(name=data['name'], address=data['address'])
    db.session.add(customer)
    db.session.commit()
    return jsonify({"message": "Customer added successfully"})

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    product = Product(name=data['name'], weight=data['weight'])
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"})

@app.route('/add_command', methods=['POST'])
def add_command():
    data = request.json
    command = CustomerDemand(
        customer_id=data['customer_id'],
        product_id=data['product_id'],
        demand=data['quantity']
    )
    db.session.add(command)
    db.session.commit()
    return jsonify({"message": "Command added successfully"})

@app.route('/add_time_window', methods=['POST'])
def add_time_window():
    data = request.json
    time_window = TimeWindow(
        customer_id=data['customer_id'],
        day=data['day'],
        start_hour=data['start_hour'],
        end_hour=data['end_hour']
    )
    db.session.add(time_window)
    db.session.commit()
    return jsonify({"message": "Time window added successfully"})

@app.route('/submit_data', methods=['POST'])
def submit_data():
    data = request.json
    # Process data and insert into DB
    # Example: Insert data into the database
    # Run optimization
    results = run_optimization()
    return jsonify(results)

@app.route('/results')
def results():
    # Fetch results from DB or other source
    results = {}
    return render_template('results.html', results=results)
