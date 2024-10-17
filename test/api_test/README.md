# MyObservatory API test

## Requirements

- python >= 3.9

## Run

```sh
# install deps
pip install -r requirements.txt

# run test
export http_proxy=http://127.0.0.1:1087;export https_proxy=http://127.0.0.1:1087;
python test.py
```

## Develop

```sh
# check out rsp body example
cat rsp_body.json

# request latest rsp body
make curl
```