# large-lifegame-model
LLM-as-a-Lifegame

## 共通のセットアップ
以下実行する。

```sh
$ pip install ollama
```

## Geminiを使うセットアップ

`.config`にGeminiのAPIを書き込む。

`llm_world.py`の`ai_type`を`'Gemini 1.5 Flash'`にする。

以下でGemini APIのセットアップをする。

```sh
$ pip install google-generativeai==0.5.4
```

## ローカルLLM(Llama 3)のセットアップ
[Ollama + Open WebUI でローカルLLMを手軽に楽しむ](https://zenn.dev/karaage0703/articles/c271ca65b91bdb)を参考にLlama 3をセットアップ

以下実行してOllamaを起動

```sh
$ docker stop $(docker ps -q)
$ docker rm $(docker ps -q -a)
```

```
$ docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

`llm_world.py`の`ai_type`を`'Llama 3'`にする。


## 使い方
GeminiかローカルLLMのセットアップをした上で以下を実行する。

```sh
$ python3 llm_wrold.py
```

リアルタイムの可視化は以下実行する。

```sh
$ python3 realtime_visualize.py
```

アニメ画像を生成する場合は以下実行する。

```sh
$ python3 visualize.py
```
