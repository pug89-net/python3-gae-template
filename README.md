# python3-gae-template

Describe your project here.

## Start devserver

`rye run serve`

## OpenAPI doc

http://127.0.0.1:8000/docs

## VS Code Tips

### Interpreter

`FastAPI`などが黄色波線になっている場合は、PythonのInterpreterが正しく指定できていないので、画面右下のInterpreterをクリックして以下のパスを使うように変更してください。

`/workspace/python3-gae-template/.venv/bin/python3.12`

## Development

- コンテナ作成後`gcloud init`が実行されるのでGoogleアカウントでログインする
- gcloud CLIの認証を行う
  - `gcloud auth application-default login`
- カレントディレクトリを移動して依存関係を取得する
  - `cd python3-gae-template/ && rye sync`
