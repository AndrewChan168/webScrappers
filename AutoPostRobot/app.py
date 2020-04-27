from flask import Flask, jsonify, request

from webplaces.uwantsAndDiscuss.uwants import uwants_browser
from webplaces.uwantsAndDiscuss.discuss import discuss_browser

# terminate browsers when the flask server is terminated
import atexit
def exit_hadler():
    uwants_browser.terminate()
    discuss_browser.terminate()

atexit.register(exit_hadler)

app = Flask(__name__)

# routes of API
#@app.route("/discuss", methods=['POST'])
#def post_response():
#    data = request.get_json()
#    print(data)
#    return jsonify({'message':'POST SUCCESS'})
@app.route("/discuss", methods=['POST'])
def post_on_discuss():
    print('Get POST request')
    if not discuss_browser.isOpen():
        discuss_browser.start()
    data = request.get_json()
    print("request body JSON")
    print(data)
    username = data.get("username")
    password = data.get("password")
    reply_content = data.get("replyContent")
    post_id = "thread_%s"%(str(data.get("postID")))
    _ = discuss_browser.login(username, password).post_comment(post_id, reply_content)
    return jsonify({"message": "Posted comment on %s"%(post_id)}), 200

#@app.route("/discuss/batch", methods=['POST'])
#def batch_post_on_discuss():
#    if not discuss_browser.isOpen():
#        discuss_browser.start()
#    data = request.get_json()
#    username = data.get("username")
#    password = data.get("password")
#    _ = discuss_browser.login(username, password).goto_sub_page()
#    batch = data.get("batch")
#    for json in batch:
#        reply_content = json.get("replyContent")
#        post_id = json.get("postID")
#        _ = discuss_browser.post_comment(post_id, reply_content)
#    return jsonify({"message":"Posted comment on batch"}), 200

@app.route("/uwants", methods=['POST'])
def post_on_wants():
    print('Get POST request')
    if not uwants_browser.isOpen():
        uwants_browser.start()
    data = request.get_json()
    print("request body JSON")
    print(data)
    username = data.get("username")
    password = data.get("password")
    reply_content = data.get("replyContent")
    post_id = "thread_%s"%(str(data.get("postID")))
    _ = uwants_browser.login(username, password).goto_sub_page().post_comment(post_id, reply_content)
    return jsonify({"message":"Posted comment on %s"%(post_id)}), 200

#@app.route("/uwants/batch", methods=['POST'])
#def batch_post_on_uwants():
#    if not uwants_browser.isOpen():
#        uwants_browser.start()
#    data = request.get_json()
#    username = data.get("username")
#    password = data.get("password")
#    _ = uwants_browser.login(username, password).goto_sub_page()
#    batch = data.get("batch")
#    for json in batch:
#        reply_content = json.get("replyContent")
#        post_id = json.get("postID")
#        _ = uwants_browser.post_comment(post_id, reply_content)
#    return jsonify({"message":"Posted comment on batch"}), 200

if __name__ == "__main__":
    app.run(debug=False)
