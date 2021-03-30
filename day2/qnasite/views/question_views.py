from flask import Blueprint, render_template

from qnasite.models import Question

bp = Blueprint('question', __name__, url_prefix='/question')
@bp.route('/greet')
def hell_world():
    return 'Hell world! <a href="/">Return to index</a>'

@bp.route('/list/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)
