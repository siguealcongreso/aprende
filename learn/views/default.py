import os
import random
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from docutils.core import publish_parts
import quiz

quiz_file = 'encuesta'


def rst2html(text):
    'return HTML'

    return publish_parts(text, writer_name='html')['fragment']


def shuffle(t):
    for q in t.questions:
        random.shuffle(q.options)
        for i, o in enumerate(q.options):
            o.index = i + 1


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    global t, info
    passed = False
    session = request.session
    quiz_file = request.GET['n']
    if not os.path.exists('{}'.format(quiz_file)):
        raise HTTPNotFound()
    if 'counter' in session:
        pass
    else:
        session['counter'] = 0
        t = quiz.load(quiz_file)
        shuffle(t)
        info = quiz.get_info(quiz_file)
        # info['end'] = rst2html(info['end'])
    question = t.questions[session['counter']]
    if len(question.answers) >= 2:
        input_type = 'checkbox'
    else:
        input_type = 'radio'
    return {'project': 'Módulo 1', 'counter': session['counter'],
            'number': session['counter']+1,
            'input_type': input_type,
            'info': info,
            'passed': passed, 'n': quiz_file,
            'question': question}


@view_config(route_name='home', request_method='POST',
             renderer='../templates/mytemplate.jinja2')
def validate(request):
    global t, info
    passed = False
    session = request.session
    quiz_file = request.POST['n']
    if not os.path.exists('{}'.format(quiz_file)):
        raise HTTPNotFound()
    if 'counter' not in session:
        session['counter'] = 0
        t = quiz.load(quiz_file)
        shuffle(t)
        info = quiz.get_info(quiz_file)
    if request.POST.get('passed'):
        session['counter'] += 1
        if int(session['counter']) == len(t.questions):
            session['counter'] = 0
            return {'project': 'Módulo 1', 'counter': '',
                    'number': '',
                    'question': None,
                    'info': info,
                    'passed': '', 'n': quiz_file,
                    'feedback': ''}
    counter = session['counter']
    indexes = request.POST.getall(str(counter))
    int_indexes = list(map(int, indexes))
    feedback = ''
    if indexes:
        question = t.questions[int(counter)]
        question.incomplete_feedback = 'Respuesta incompleta'
        passed = question.evaluate(indexes)
        feedbacks = question.feedbacks()
        feedback = '\n\n'.join(feedbacks)
        # feedback = rst2html(feedback)
        if passed:
            if feedback:
                feedback = 'Correcto: ' + feedback
            else:
                feedback = 'Correcto.'
            # session['counter'] += 1
            if int(session['counter']) == len(t.questions):
                session['counter'] = 0
                return {'project': 'Módulo 1', 'counter': '',
                        'number': '',
                        'question': None,
                        'info': info, 'n': quiz_file,
                        'passed': passed,
                        'feedback': feedback}
        else:
            feeback = 'Incorrecto: ' + feedback

    question = t.questions[session['counter']]
    if len(question.answers) >= 2:
        input_type = 'checkbox'
    else:
        input_type = 'radio'
    return {'project': 'Módulo 1', 'counter': session['counter'],
            'number': session['counter']+1,
            'input_type': input_type,
            'question': question,
            'info': info,
            'passed': passed, 'n': quiz_file,
            'indexes': int_indexes,
            'feedback': feedback}
