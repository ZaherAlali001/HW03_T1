def div(request):
    request_json = request.get_json()
    x = request_json['X']
    y = request_json['Y']
    if y == 0:
        return {"error": "Division by zero is not allowed"}
    result = x / y
    return {
        "X": x,
        "Y": y,
        "Result": result
    }
