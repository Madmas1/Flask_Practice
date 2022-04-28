# Импортируем модуль фреймворка Flask и модуль основных методов Utils

import utils
from flask import Flask

# Создаем экземпляр app класса Flask
app = Flask(__name__)

# Загружаем данные из JSON
candidate_list = utils.get_candidates_list("candidates.json")

# Показываем основную страничку с кандидатами
@app.route("/")
def show_main_page():
    return utils.format_candidates_list(candidate_list)


# Показываем страничку кандидата по ID
@app.route("/candidates/<int:candidate_id>")
def show_candidate_page(candidate_id):
    return utils.get_candidate_page(candidate_id, candidate_list)


# Показываем страничку кандидата по его навыку
@app.route("/skills/<skill>")
def show_candidates_skills_page(skill):
    return utils.get_candidate_skills_page(skill, candidate_list)


app.run(host='127.0.0.1', port=5000)

