from typing import Annotated

from app.prefecture import Prefecture
from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/login")
async def login(request: Request):
    """ログイン画面の表示処理です。

    Args:
        request (Request): リクエスト

    Returns:
        _TemplateResponse: ログイン画面
    """
    message = {"message": "Hello, GAE world."}
    return _create_response("login.html", request, message)


@router.post("/index")
async def login_auth(
    request: Request,
    user_id: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    """ダッシュボード画面表示処理です。
    ログイン画面で入力されたアカウント情報の認証を行います。

    Args:
        request (Request): リクエスト
        user_id (Annotated[str, Form): アカウントID
        password (Annotated[str, Form): パスワード

    Returns:
        _TemplateResponse: ダッシュボード画面
    """
    return _create_response(
        "index.html", request, {"prefecture_list": Prefecture.get_prefecture_list()}
    )


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
