from flask import make_response

def base_response(result, code=200, error = ''):
    """Function with creste response"""
    response = dict(results = result)
    if(bool(len(error))):
        error = dict(message = error, code = code)
        response = dict(response, error = error)
    return make_response(response, code)

    
