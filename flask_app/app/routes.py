import datetime
import json
import os
from datetime import date
from app.defs import *
from flask import Flask, jsonify, request, flash
from functools import wraps
from app.models import *
from app import app
import logging
from app.database_creation import db_creation
from app.queries import *

# now we will Create and configure logger
logging.basicConfig(format='%(asctime)s %(message)s', filemode='w')
# Let us Create an object
logger = logging.getLogger()
# Now we are going to Set the threshold of logger to DEBUG
logger.setLevel(logging.INFO)


@app.route('/survey/create/', methods=['GET', 'POST'])
def survey_create():
    # Request json.
    request_data = request.get_json()
    request_data = {
        "survey_description": "xxxx"
    }
    json_dump = json.dumps(request_data)
    request_data = json.loads(json_dump)
    try:
        survey = Survey(date=date.today(),
                        description=request_data["survey_description"]
                        )
        db.session.add(survey)
        db.session.commit()

        payload = {"message": "200 Succesfully Edited."}

        return jsonify(success=True, payload=payload)
    except:
        payload = {"error": 500, "message": "Internal Server Error"}
        return jsonify(success=False, payload=payload)


@app.route('/question/create/', methods=['GET', 'POST'])
def question_create():
    # Request json.
    request_data = request.get_json()
    request_data = {
        "survey_id": 1,
        "single_choice": {"question": ["xxx", "xxx"],
                          },
        "free_text": {"question": ["xxx", "xxx"],
                      },
        "multiple_choice": [{"question": "xxx",
                             "multiple_question": ["xxx", "xxx"]
                             },
                            {"question": "xxx",
                             "multiple_question": ["xxx", "xxx"]
                             }
                            ]
    }
    json_dump = json.dumps(request_data)
    request_data = json.loads(json_dump)
    try:
        for i in request_data["single_choice"]['question']:
            question = SingleChoice(question=i,
                                    survey_id=request_data["survey_id"]
                                    )
            db.session.add(question)
            db.session.commit()

        for i in request_data["single_choice"]['question']:
            question = FreeText(question=i,
                                survey_id=request_data["survey_id"]
                                )
            db.session.add(question)
            db.session.commit()

        for i in request_data["multiple_choice"]:
            for j in i['multiple_question']:
                question1 = MultipleChoice(question=i['question'],
                                           survey_id=request_data["survey_id"]
                                           )
                db.session.add(question1)
                db.session.commit()

                multiple_choice = MultipleChoice.query.filter_by(survey_id=request_data["survey_id"]).first()
                question = MultipleChoiceQuestions(question=j,
                                                   multiple_choice_id=multiple_choice.id
                                                   )

                db.session.add(question)
                db.session.commit()

        payload = {"message": "200 Succesfully Edited."}

        return jsonify(success=True, payload=payload)
    except:
        payload = {"error": 500, "message": "Internal Server Error"}
        return jsonify(success=False, payload=payload)


@app.route('/retrieve/survey/', methods=['GET', 'POST'])
def retrieve_survey():
    # Request json.
    request_data = request.get_json()
    request_data = {
        "survey_id": 1
    }
    json_dump = json.dumps(request_data)
    request_data = json.loads(json_dump)
    try:
        single_choice = SingleChoice.query.filter_by(survey_id=request_data["survey_id"]).all()
        free_text = FreeText.query.filter_by(survey_id=request_data["survey_id"]).all()
        multiple_choice = MultipleChoice.query.filter_by(survey_id=request_data["survey_id"]).all()
        multiple_choice_q = MultipleChoiceQuestions.query.filter_by(multiple_choice_id=multiple_choice[0].id).all()

        single_question_list = []
        free_text_question_list = []
        multiple_choice_question_list = []
        mlist = []
        for i in single_choice:
            single_question_list.insert(0, i.question)
        for i in free_text:
            free_text_question_list.insert(0, i.question)
        for i in multiple_choice:
            for j in multiple_choice_q:
                multiple_choice_question_list.insert(0, j.question)
            x = {i.question: multiple_choice_question_list}
            mlist.insert(0, x)

        return jsonify(survey_id=request_data["survey_id"],
                       single_choice=single_question_list,
                       free_text=free_text_question_list,
                       multiple_choice=mlist)
    except:
        payload = {"error": 500, "message": "Internal Server Error"}
        return jsonify(success=False, payload=payload)


@app.route('/answer/survey/', methods=['GET', 'POST'])
def answer_survey():
    # Request json.
    request_data = request.get_json()
    request_data = {
        "survey_id": 1,
        "single_choice": [{"question": "xxx",
                           "answer": False,
                           "other": 'xxx'},
                          {"question": "xxx",
                           "answer": True,
                           "other": 'xxx'}],
        "free_text": [{"question": "xxx",
                       "answer": 'xxx',
                       "other": 'xxx'},
                      {"question": "xxx",
                       "answer": 'xxx',
                       "other": 'xxx'}],
        "multiple_choice": [{"question": "xxx",
                             "answer": 'answer1',
                             "other": 'xxx'},
                            {"question": "xxx",
                             "answer": 'answer2',
                             "other": 'xxx'}],
    }
    json_dump = json.dumps(request_data)
    request_data = json.loads(json_dump)
    try:
        for i in request_data["single_choice"]:
            single_choice = SingleChoice.query.filter_by(survey_id=request_data["survey_id"]).first()
            answer = SingleChoiceAnswers(answer=i['answer'],
                                         other=i['other'],
                                         single_choice_id=single_choice.id
                                         )
            db.session.add(answer)
            db.session.commit()

        for i in request_data["free_text"]:
            free_text = FreeText.query.filter_by(survey_id=request_data["survey_id"]).first()
            answer = FreeTextAnswers(answer=i['answer'],
                                     other=i['other'],
                                     free_text_id=free_text.id
                                     )
            db.session.add(answer)
            db.session.commit()
        for i in request_data["multiple_choice"]:
            multiple_choice = MultipleChoice.query.filter_by(survey_id=request_data["survey_id"]).first()
            answer = MultipleChoiceAnswers(answer=i['answer'],
                                           other=i['other'],
                                           multiple_choice_id=multiple_choice.id
                                           )
            db.session.add(answer)
            db.session.commit()

        payload = {"message": "200 Succesfully Edited."}

        return jsonify(success=True, payload=payload)
    except:
        payload = {"error": 500, "message": "Internal Server Error"}
        return jsonify(success=False, payload=payload)


@app.route('/statistics/survey/', methods=['GET', 'POST'])
def statistics_survey():
    # Request json.
    request_data = request.get_json()
    request_data = {
        "survey_id": 1
    }
    json_dump = json.dumps(request_data)
    request_data = json.loads(json_dump)
    # try:
    query1 = stat_single_choice(str(request_data["survey_id"]))
    query2 = stat_free_text(str(request_data["survey_id"]))
    query3 = stat_multiple_choice(str(request_data["survey_id"]))
    df1 = query_as_df(app.config['SQLALCHEMY_DATABASE_URI'], query1)
    df2 = query_as_df(app.config['SQLALCHEMY_DATABASE_URI'], query2)
    df3 = query_as_df(app.config['SQLALCHEMY_DATABASE_URI'], query3)

    return jsonify(stat_single_choice=df1.to_dict('records'), stat_free_text=df2.to_dict('records'),
                   stat_multiple_choice=df3.to_dict('records'))
    # except:
    #     payload = {"error": 500, "message": "Internal Server Error"}
    #     return jsonify(success=False, payload=payload)