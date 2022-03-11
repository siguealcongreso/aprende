=========
Structure
=========

Files
=====

::

   learn/static/
         templates/layout.jinja2
	           mytemplate.jinja2
	 views/
	 routes.py


Templates
=========

These templates are used:

- `layout.jinja2`.  The base template, it uses:

  - Bootstrap CSS 3.3.7 from bootstrapcdn.com. Bootsrap JavaScript is
    loaded at the end of the document so the pages load faster.
  - html5shiv 3.7.0 and respond.js 1.4.2 from maxcdn.com
  - `static/theme.css` that loads Open Sans font family from
    fonts.googleapis.com
  - The `description`, `shortcut icon`, the logo, the Twitter and
    Facebook URLs and the copyright notice where customized for the
    use on the first site.

  
- `mytemplate.jinja2`. Extends the base layout by implementing the
  content block.  It uses:

  - info.title and info.description
  - number and question.text
  - Iterates on `question.options` to create the option check boxes or
    radio buttons using option.index, option.text, and input_type.
  - If there are no questions, it displays `info.end`.
  - It displays `feedback`.
  - Includes the hidden inputs `index` and `n`.
  - If passed is True, include a hidden input with this name and
    value.
