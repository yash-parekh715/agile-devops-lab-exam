from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/status', methods=['get'])
def status():
    return jsonify({'status': 'ok'}), 200


@app.route("/sum", methods=["GET"])
def sum_route():
    a = request.args.get("a")
    b = request.args.get("b")
    if a is None or b is None:
        return jsonify({"error": "missing query parameters a and b"}), 400
    try:
        def to_num(x):
            try:
                return int(x)
            except ValueError:
                return float(x)
        a_num = to_num(a)
        b_num = to_num(b)
    except ValueError:
        return jsonify({"error": "a and b must be numbers"}), 400

    return jsonify({"sum": a_num + b_num}), 200


if __name__ == '__main__':
    app.run(debug=True)
