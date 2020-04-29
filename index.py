#!C:/Users/Karem Huacota/AppData/Local/Programs/Python/Python38-32/python.exe
from flask import Flask, render_template, request
import pickle

print("Content-type: text/html\n")
app = Flask(__name__)

f = open('database/order.txt', 'rb')
handler = pickle.load(f)
f.close()


@app.route('/orders')
def get_orders():
    orders = handler.get_all()
    return render_template("order_list.html", orders=orders)


@app.route('/orders/<id>')
def get_order_by_id(id):
    items = handler.get_by_id(id).get_all()
    return render_template('order_detail.html', items=items, order_id=id)


@app.route('/orders/<order_id>/items/<item_id>/rate', methods=['POST'])
def rate_item(order_id, item_id):
    try:
        score = int(request.form['rate'])
        order = handler.get_by_id(order_id)
        item = order.get_by_id(item_id)
        item.set_score(score)
        f = open('database/order.txt', 'wb')
        pickle.dump(handler, f)
        f.close()
        return 'success'
    except Exception as e:
        return str(e)


@app.route('/orders/<order_id>/items/<item_id>/note', methods=['POST'])
def set_note_item(order_id, item_id):
    try:
        note = request.form['note']
        order = handler.get_by_id(order_id)
        item = order.get_by_id(item_id)
        item.set_note(note)
        f = open('database/order.txt', 'wb')
        pickle.dump(handler, f)
        f.close()
        return 'success'
    except Exception as e:
        return str(e)
