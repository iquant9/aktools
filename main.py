from sanic import Sanic, json, SanicException, text
from sanic.log import logger

import akshare

app = Sanic(name='quant-api')

date_format = '%Y-%m-%d %H:%M:%S'


@app.get("/")
async def hello_world(request):
    return text("Hello, world.")


@app.get("rest")
def rest(request):
    cmd = request.args.get("cmd")
    logger.info('cmd is %s' % cmd)
    # import Ashare
    try:
        df = eval(str(cmd))
    except Exception as e:
        logger.error("eval is running at error:%s" % e)
        raise SanicException("Something went wrong.%s" % (e), status_code=501)
    logger.info('df len is %d' % len(df))

    # default is a function applied to objects that aren't serializable.
    # In this case it's str, so it just converts everything it doesn't know to strings.
    return json(df.dropna().to_dict('records'), headers={"charset": "utf-8"},
                default=str,
                ensure_ascii=False)

    # return JsonResponse(json.loads(response), json_dumps_params={'ensure_ascii': False}, safe=False)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
