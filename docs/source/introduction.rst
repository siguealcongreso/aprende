------------
Introduction
------------

Learn is a web application that serves interactive documents a tool
for learning about topics.


Architecture
============

It is based on the Pyramid web framework. It was started from a
cookiecutter template with jinja2 as the template language and no
database backend. These extensions are used:

- `pyramid_beaker` to support cookie-based sessions to preserve the
  state.

It uses quiz, a library that handles the learning content.

It uses docutils to convert ReStructured text marks in the content into
HTML.

There is a single route at / that uses two functions, each for the GET
and POST HTTP methods.

There is a single template.

The `development.ini` or `production.ini` files store configuration
information:

- `quiz_folder`, the deault is quiz/ in the application folder
- session configuration like type, data_dir and lock_dir
- prefix where the application will be served, the default is `/quiz`

Operation
=========

A single HTTP route ``/`` is configured. This route is associated to a
view for requests using the GET method and to another view for
requests with the POST method.  All the responses use a single
template that includes a ``form`` element.

A test is started with a GET request that includes a query string
``?n=<file_name>`` that selects which test will be used.  The response
displays the first question and its options.  All subsequent requests
are started by a click in the form submit button and they use the POST
method.

The submit button of the form is labeled `submit`, to allow the user
to send the selected option or options to answer a question.  These
options are evaluated for correctness and the response provides
feedback. If the answer is not correct, this step  is repeated.

Once the answer is correct, the button is labeled `continue` to allow
the user to proceed to the next question.

This cycle continues until the last question is responded correctly.
At this point the response shows the final feedback, there is no
submit button and the test is ended.


Detailed steps
==============

GET request
-----------

A GET request runs `my_view`. The steps are:

#. Read from the request:

   - session, either a new one is created or the existing one is read.
   - `n`, the name of the quiz file to be used.  It is obtained from
     the query string.  If there is no query string it defaults to an
     empty string.

#. Check that the quiz file exists inside `quiz_folder`.  Respond
   `HTTPNotFound` and return if needed.

#. Check for `counter` in the session. If it does not exist, this is the
   start of a quiz:

   - Set `counter` to 0
   - Call `quiz.load` to get the quiz content as a `Quiz` instance
     and store it in `test` in the session
   - Call shuffle to reorder que options to each question
   - Call `quiz.load` to get information about the quiz and store it
     in `info` in the session
     
   If `counter` exists, the quiz is ongoing. Retrieve `test` and `info`
   from the session

#. Display a question

   - Use `counter` as index into `test.questions`
   - Define the input type to use based on the number of valid
     answers for the question:  Use checkbox for two or more required answers,
     radio button when a single answer is required.
   - return by rendering the `mytemplate.jinja2` template with this information:

     - counter, number (counter + 1), input_type, info
     - passed=False, n, question



POST request
------------

The POST request runs `validate` with these steps:

#. Read from the request:

   - session
   - `n`, the name of the quiz file. It is obtained from the POST
     data.

#. Check that the quiz file exists inside `quiz_folder`.  Respond
   `HTTPNotFound` and return if needed.

#. Check for `counter` in the session. If it does not exist, this is the
   start of a quiz:

   - Set `counter` to 0
   - Call `quiz.load` to get the quiz content as a `Quiz` instance
     and store it in `test` in the session
   - Call shuffle to reorder que options to each question
   - Call `quiz.load` to get information about the quiz and store it
     in `info` in the session
     
   If `counter` exists, the quiz is ongoin. Retrieve `test` and `info`
   from the session

#. Check the value of `passed` in the POST data.  If true, increment `counter`
   in the session and check if the last question is passed: `counter` is equal
   to the number of questions in the test.  If yes, prepare to render the
   end of the test using the same template, sending `question= None`, and
   return.

#. Get the indexes from the POST data and convert to integers.

#. Check if the answer or answers are correct using the indexes, and
   set `passed`.

#. Prepare the feedbacks for the question.

#. If `passed` is True, prepend `'Correcto: '` to the feedback, if it
   is not empty, then check if the last question, and if yes return to
   render the template.

#. If `passed` is False, prepend `'Incorrecto: '` to the feedback.

#. Display a question

   - Use `counter` as index into `test.questions`
   - Define the input type to use based on the number of valid
     answers for the question:  Use checkbox for two or more required answers,
     radio button when a single answer is required.
   - return by rendering the `mytemplate.jinja2` template with this information:

     - counter, number (counter + 1), input_type, info
     - passed, n, question, indexes, feedback

