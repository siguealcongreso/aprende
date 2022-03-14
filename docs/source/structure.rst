=========
Structure
=========

Files
=====

::

   learn/static/
         templates/single.jinja2
	 views/
	 routes.py


Templates
=========

The `single.jinja2` template has this structure:

- Load the Tachyons CSS
- Load a shortcut icon
- Provide Open Graph and Twitter Card fields
- A `header` element similar to the ananke theme. `info.title`
  and `info.description` are used instead of the site title and
  description.
- A `main` element contains and `article` element.
- A `form` element with these elements:

  - The value of the `action` attribute is ``/quiz#main``.
  - displays `question.text` and the `question.options`
  - `input_type` selects radio or checkbox type.
  - There are hidden input elements for `counter` and `n`.

- A `footer` element similar to the anake theme.
- Load the Tachyons Javascript.
