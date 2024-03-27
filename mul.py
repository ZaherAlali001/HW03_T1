def mul(request):
    request_json = request.get_json()
    x = request_json['X']
    y = request_json['Y']
    result = x * y
    return {
        "X": x,
        "Y": y,
        "Result": result
    }
