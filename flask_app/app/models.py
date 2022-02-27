from app.__init__ import db


class Survey(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    description = db.Column(db.String(100))
    single_choice = db.relationship('SingleChoice', backref='author', lazy='dynamic')
    free_text = db.relationship('FreeText', backref='author', lazy='dynamic')
    multiple_choice = db.relationship('MultipleChoice', backref='author', lazy='dynamic')





class SingleChoice(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100))
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
    single_choice_answer = db.relationship('SingleChoiceAnswers', backref='author', lazy='dynamic')



class SingleChoiceAnswers(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Boolean)
    other = db.Column(db.String(100))
    single_choice_id = db.Column(db.Integer, db.ForeignKey('single_choice.id'))



class FreeText(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100))
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
    free_text_answers = db.relationship('FreeTextAnswers', backref='author', lazy='dynamic')



class FreeTextAnswers(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(100))
    other = db.Column(db.String(100))
    free_text_id = db.Column(db.Integer, db.ForeignKey('free_text.id'))



class MultipleChoice(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100))
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
    multiple_choice_questions = db.relationship('MultipleChoiceQuestions', backref='author', lazy='dynamic')
    multiple_choice_answers = db.relationship('MultipleChoiceAnswers', backref='author', lazy='dynamic')

class MultipleChoiceQuestions(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100))
    multiple_choice_id = db.Column(db.Integer, db.ForeignKey('multiple_choice.id'))


class MultipleChoiceAnswers(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(100))
    other = db.Column(db.String(100))
    multiple_choice_id = db.Column(db.Integer, db.ForeignKey('multiple_choice.id'))


class StarRating(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer)


