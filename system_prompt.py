base_prompt = r"""
日本語でおねがいします。
仮想世界のシミュレーションを行います。
仮想世界はライフゲームのようにnxnのセルで成り立っています。
以下の条件とルールに従って、各ステップごとに世界の状態を更新してください。
""".strip()

condition_prompt = r"""
- 0-9の数字で表現する
- 0: 土
- 1: 植物
- 2: 草食動物
- 3: 肉食動物
""".strip()

rule_prompt = r"""
1. 植物（1）は1ステップで隣接する土（0）に増殖する。密集しすぎると死滅する。
2. 草食動物（2）は隣接する植物（1）を食べる。食べ物が不足している場合、空いた場所（0）に移動する。
3. 肉食動物（3）は隣接する草食動物（2）を優先して食べる。草食動物がいない場合、植物（1）を食べる。
6. 植物（1）、草食動物（2）、肉食動物（3）は1ステップごとにランダムなタイミングでランダムな場所に新たに発生する
7. 植物（1）、草食動物（2）、肉食動物（3）は1ステップごとにランダムなタイミングでランダムな場所で土になる。
8. 仮想世界を常に生命に満ち溢れた状態にしてください。
""".strip()


def get_prompt(state_data_string):
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
現在の状態の次のステップをcsv形式で next_state と state_end で囲んで記述してください。
また現在の世界の様子を explanation_start と explanation_end で囲んで言葉で10文くらいで表現してください。
例を以下に示します。


next_state
{state_data_string}
state_end

explanation_start
今の世界は、土だけです。
explanation_end
"""

    return all_prompt
