from flask import Flask, jsonify
from flask_cors import CORS
from llama import Llama2, Llama3

app = Flask(__name__)
CORS(app)

@app.route('/leave-info/<int:id>', methods=['GET'])
def get_leave_info(id):
    position = Llama2.get_employee_position(id)
    leave_data = Llama3.get_leave_data(id)
    
    if position and leave_data:
        remainingLeaves = leave_data['totalLeaves'] - leave_data['usedLeaves']
        return jsonify({
            'position': position,
            'totalLeaves': leave_data['totalLeaves'],
            'usedLeaves': leave_data['usedLeaves'],
            'remainingLeaves': remainingLeaves,
        })
    else:
        return jsonify({'error': 'Employee not found!'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
