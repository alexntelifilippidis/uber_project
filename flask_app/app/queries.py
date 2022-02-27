
def stat_single_choice(id):
    return """
    select a.id as survey_id,b.id as question_id,count(*) as answers
    from survey a
    left join single_choice b on a.id=b.survey_id 
    left join single_choice_answers c on b.id=c.single_choice_id
    where a.id = '""" + id + """'
    group by a.id,b.id
                """

def stat_free_text(id):
    return """
    select a.id as survey_id,b.id as question_id,count(*) as answers 
    from survey a
    left join free_text b on a.id=b.survey_id
    left join public.free_text_answers c on b.id=c.free_text_id
    where a.id = '""" + id + """'
    group by a.id,b.id
                """

def stat_multiple_choice(id):
    return """
    select a.id as survey_id,b.id as question_id,c.answer as multiple_choice_text ,count(answer) as answers
    from survey a
    left join multiple_choice b on a.id=b.survey_id
    left join public.multiple_choice_answers c on b.id=c.multiple_choice_id
    where a.id = '""" + id + """'
    group by a.id,b.id,c.answer
                """