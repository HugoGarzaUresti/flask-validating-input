from flask import render_template, redirect, url_for, flash, request, current_app as app
from .forms import PersonForm  # Correct import path


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PersonForm()
    if form.validate_on_submit():
        flash('Form successfully validated')
        return redirect(url_for('results'))
    return render_template('form.html', form=form)

@app.route('/results')
def results():
    return render_template('results.html')
