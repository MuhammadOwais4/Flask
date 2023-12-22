from flask import Flask, request

app = Flask(__name__)

# Sample data to simulate a database
customers = []
services = []
orders = []

# ... (Customer, Service, and Order classes remain the same)

# Create a customer
@app.route('/api/v1/create-customer', methods=['POST'])
def create_customer():
    data = request.form
    new_customer = {
        'id': len(customers)+1,
        'name': data.get('name'),
        'dob': data.get('dob'),
        'phone': data.get('phone')
    }
    customers.append(new_customer)
    return {'message': f'Customer created successfully'}, 201

# Get all customers
@app.route('/api/v1/get-all-customers', methods=['GET'])
def get_all_customers():
    return {'data': customers}, 200

# Update a customer
@app.route('/api/v1/update-customer/<int:id>', methods=['PUT'])
def update_customer(id):
    data = request.form
    for i in range(len(customers)):
        if customers[i]['id'] == id:
            customers[i] = {
                'id': id,
                'name': data.get('name'),
                'dob': data.get('dob'),
                'phone': data.get('phone')
            }
            break
    else:
        return {"error": "No such customer found"}, 404
    return {'message': f"Customer updated successfully"}

# Delete a customer 
@app.route('/api/v1/delete-customer/<int:id>', methods=['DELETE'])
def delete_customer(id):
    global customers
    for i in range(len(customers)):
        if customers[i]['id'] == id:
            del customers[i]
            break
    else:
        return {"error": "No such customer found"}, 404
    return {'message': f"Customer deleted successfully"}



# Create a service
@app.route('/api/v1/create-service', methods=['POST'])
def create_service():
    data = request.form
    new_service = {
        'id': len(services)+1,
        'type': data.get('type'),
        'price': data.get('price'),
        'duration': data.get('duration')
    }
    services.append(new_service)
    return {'message': f'Service created successfully'}, 201

# Get all services
@app.route('/api/v1/get-all-services', methods=['GET'])
def get_all_services():
    return {'data': services}, 200

# Update a service
@app.route('/api/v1/update-service/<int:id>', methods=['PUT'])
def update_service(id):
    data = request.form
    for i in range(len(services)):
        if services[i]['id'] == id:
            services[i] = {
                'id': id,
                'type': data.get('type'),
                'price': data.get('price'),
                'duration': data.get('duration')
            }
            break
    else:
        return {"error": "No such service found"}, 404
    return {'message': f"Service updated successfully"}

# Delete a service
@app.route('/api/v1/delete-service/<int:id>', methods=['DELETE'])
def delete_service(id):
    global services
    for i in range(len(services)):
        if services[i]['id'] == id:
            del services[i]
            break
    else:
        return {"error": "No such service found"}, 404
    return {'message': f"Service deleted successfully"}

# Create an Order
@app.route('/api/v1/create-order', methods=['POST'])
def create_order():
    data = request.form
    new_order = {
        'id': len(orders)+1,
        'customer_name': data.get('customer_name'),
        'phone_number': data.get('phone_number'),
        'email': data.get('email'),
        'address': data.get('address'),
        'date': data.get('date'),
        'time': data.get('time'),
        'total_cost': data.get('total_cost'),
        'status': data.get('status'),
        'services': data.get('services')
    }
    orders.append(new_order)
    return {'message': f'Order created successfully'}, 201

# Get all Orders
@app.route('/api/v1/get-all-orders', methods=['GET'])
def get_all_orders():
    return {'data': orders}, 200

# Get an order by ID
@app.route('/api/v1/get-order/<int:id>', methods=['GET'])
def get_order(id):
    for order in orders:
        if order['id'] == id:
            return order
    return {"error": "No such order found"}, 404

# Update an order
@app.route('/api/v1/update-order/<int:id>', methods=['PUT'])
def update_order(id):
    data = request.form
    global orders
    for i in range(len(orders)):
        if orders[i]['id'] == id:
            orders[i].update({
                'customer_name': data.get('customer_name'),
                'phone_number': data.get('phone_number'),
                'email': data.get('email'),
                'address': data.get('address'),
                'date': data.get('date'),
                'time': data.get('time'),
                'total_cost': data.get('total_cost'),
                'status': data.get('status'),
                'services': data.get('services')
            })
            return {'message': f"Order updated successfully"}
    return {"error": "No such order found"}, 404

# Delete an Order
@app.route('/api/v1/delete-order/<int:id>', methods=['DELETE'])
def delete_order(id):
    global orders
    for i in range(len(orders)-1, -1, -1):
        if orders[i]['id'] == id:
            del orders[i]
            return {'message': f"Order deleted successfully"}
    return {"error": "No such order found"}, 404

if __name__ == '__main__':
    app.run(
           port=5000,
           debug=True
    )
