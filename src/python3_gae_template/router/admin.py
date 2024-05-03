from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/login")
async def login(request: Request):
    """ログイン画面の表示処理です。

    Args:
        request (Request): リクエスト

    Returns:
        _TemplateResponse: ログイン画面レスポンス
    """
    message = {"message": "Hello, GAE world."}
    return _create_response("login.html", request, message)


@router.get("/index")
async def login_auth(request: Request):
    return _create_response("index.html", request, {})


def _create_response(template_name: str, request: Request, args: dict):
    """テンプレートレスポンスを作成します。

    Args:
        template_name (str): テンプレート名
        request (Request): リクエスト
        args (dict): テンプレートに埋め込む値

    Returns:
        _TemplateResponse: テンプレートレスポンス
    """
    args["request"] = request
    return templates.TemplateResponse(template_name, args)
