import openai

from .env import get_env


def gptclient(json=None, text=None):
    openai.api_key = get_env("OPENAI_API_KEY", "")
    # gptに渡すメッセージの構造
    message_structure = []
    if json is not None:
        message_structure = json
    elif text is not None:
        message_structure = [{"role": "system", "content": text}]
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message_structure,
    )

    return completion


# 返答をテキストとして返す
def gptchat(json=None, text=None):
    return gptclient(json, text).choices[0].message.content


# 返答をそのままの構造で返す
def gptchatjson(json=None, text=None):
    return gptclient(json, text)


if __name__ == "__main__":
    request_json = [{"role": "system",
                     "content": "あなたは気さくな上司として一人の部下のプログラマーの進捗を確認してください。定期報告を提出するように求めます。ただしあなたは教育係の代理の窓口なので、何らかの個別対応をするときは約束はせずにメッセージを担当者に取り次ぎます。文字数は150文字以内で"}]
    print(gptchat(json=request_json))
    request_json = [{"role": "system",
                     "content": "あなたは気さくな上司として一人の部下のプログラマーの進捗を確認してください。定期報告を提出するように求めます。ただしあなたは教育係の代理の窓口なので、何らかの個別対応をするときは約束はせずにメッセージを担当者に取り次ぐと伝えてください。文字数は150文字以内で。担当者への取次が必要だと判断した場合必ず文字列の先頭に\"helprequire\"と入れてください"},
                    {"role": "user",
                     "content": "はい、わかりました。今日は予定通り教材の３章と４章を学習し、演習問題を解きました。ただjavaのクラスの概念がうまく掴めていない気がします"}]
    print("ユーザー: " + request_json[1]["content"])
    print("自動応答: " + gptchat(json=request_json))
# gptに渡すメッセージの構造について
# role: system or user
# content: メッセージの内容
# 例: [{"role": "system", "content": "Hello, how are you?"}, {"role": "user", "content": "I'm good. What are you up to?"}]
# role は assistant:GPTによる返信 user:ユーザーとして対話 system:システムプロンプト が使える 基本的にsystemを優先してくれる。assistantの必要性としては会話の流れを覚えておくことにある
