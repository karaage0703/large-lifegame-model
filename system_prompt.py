base_prompt = r"""
・ 日本語でおねがいします。
・ 仮想世界のシミュレーションを行います。
・ 仮想世界はライフゲームのようにnxnのセルで成り立っています。
・ セルは縦と横で隣接関係があります。
・ 以下の条件とルールに従って、各ステップごとに世界の状態を更新してください。
""".strip()

condition_prompt = r"""
- 0-9の数字で表現する
- 0: 土
- 1: 植物
- 2: 草食動物
- 3: 肉食動物
""".strip()


def get_prompt(state_data_string):
    text_file = open('rule.txt', 'r')
    rule_prompt = text_file.read()

    all_prompt = f"""
{base_prompt}

## 条件:
{condition_prompt}

## ルール:
{rule_prompt}

## 状態:
現在の状態は以下です。

current_state
{state_data_string}
state_end

#### 出力:
現在の状態の次のステップをcsv形式で「next_state」と「state_end」で囲んで記述してください。
また現在の世界の様子を「explanation_start」と「explanation_end」で囲んで言葉で10文くらいで表現してください。
例を以下に示します。


next_state
{state_data_string}
state_end

explanation_start
今の世界は、土だけです。
explanation_end
"""

    return all_prompt
