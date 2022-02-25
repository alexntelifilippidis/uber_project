
def object_to_dict(object):
    data = {}
    for c in object.__table__.columns:
        data[f'{c.name}'] = f'{str(getattr(object, c.name))}'

    return data

