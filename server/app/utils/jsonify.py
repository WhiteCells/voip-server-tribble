from litestar import Response


def jsonify(code: int, data: dict, msg: str) -> Response:
    return Response(
        content={
            "code": code,
            "data": data,
            "msg": msg,
        },
        media_type="application/json",
        status_code=code,
    )