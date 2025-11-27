import json
from flask import Flask, jsonify, request

app = Flask(__name__)

with open('questions.json', 'r', encoding='utf-8') as file:
    quest_read = json.load(file)


@app.route('/start', methods=['GET'])
def get_quest():
    return quest_read


@app.route('/start/<int:q_id>')
def get_quests(q_id):
    for q in quest_read:
        if q['id'] == q_id:
            return jsonify(q)
    return jsonify({'error': 'Quest not found'}), 404

@app.route('/start/<int:q_id>', methods=['POST'])
def post_answer(q_id):
    global quest_read

    current_quest = None
    for i, que in enumerate(quest_read):
        if q_id == que['id']:
            current_quest = que
            quest_index = i
            break

    if not current_quest:
        return jsonify({'error': 'Quest not found'}), 404

    if not request.json or 'answer' not in request.json:
        return jsonify({'error': 'No answer provided'}), 400

    user_answer = request.json['answer']


    correct_answer = None
    for q in quest_read:
        if q['id'] == q_id:
            correct_answer = q['answer']
            break

    if correct_answer is None:
        return jsonify({'error': 'Correct answer not found'}), 500

    new_quest = current_quest.copy()
    new_quest['answer'] = user_answer
    new_quest['done'] = (user_answer.strip() == correct_answer.strip())

    quest_read[quest_index] = new_quest

    return jsonify(new_quest)


if __name__ == '__main__':
    app.run(debug=True, port= 1420)