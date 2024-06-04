import ollama
import csv
import configparser
import re
import shutil
import os

from system_prompt import get_prompt

current_state_filename = './data/current_state.csv'
rows, cols = 10, 10
max_step = 100

# ai_type = 'Llama 3'
ai_type = 'Gemini 1.5 Flash'

if ai_type == 'Gemini 1.5 Flash':
    import google.generativeai as genai
    config = configparser.ConfigParser()
    config.read('.config')
    gemini_api_key = config.get('gemini_api_key', 'key')
    genai.configure(
        api_key=gemini_api_key
    )
    client_google = genai.GenerativeModel(
        'gemini-1.5-flash-latest')


def generate_zero_state(rows, cols):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    formatted_list = [','.join(map(str, row)) for row in matrix]
    return formatted_list


def get_current_state():
    with open(current_state_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        state_data = list(reader)

    state_data_string = '\n'.join([','.join(row) for row in state_data])

    return state_data_string


def save_current_state(state_data):
    with open(current_state_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in state_data:
            csv_writer.writerow(row.split(','))
    print("csv file is saved.")


def extract_state(prompt):
    match = re.search(r'next_state(.*?)state_end', prompt, re.DOTALL)

    if match:
        state_data = match.group(1).strip().split('\n')
    else:
        state_data = []

    state_data = [line for line in state_data if line.strip()]

    return state_data


def is_correct_format(matrix_list, rows, cols):
    if len(matrix_list) != rows:
        return False

    for row in matrix_list:
        elements = row.split(',')
        if len(elements) != cols:
            return False
        if any(not elem.isdigit() for elem in elements):
            return False

    return True


os.makedirs('data', exist_ok=True)

state_data = generate_zero_state(rows, cols)
save_current_state(state_data)

state_data_string = get_current_state()
all_prompt = get_prompt(state_data_string)
print(all_prompt)


for step in range(max_step):
    state_data_string = get_current_state()
    all_prompt = get_prompt(state_data_string)

    if ai_type == 'Gemini 1.5 Flash':
        print("I am Gemini 1.5 Flash")
        response = client_google.generate_content(
            all_prompt
        )
        message = response.text

    if ai_type == 'Llama 3':
        print("I am Llama 3")
        response = ollama.chat(
            model='llama3',
            messages=[{'role': 'user', 'content': all_prompt}],
        )

        message = response['message']['content']

    print(message)
    state_data = extract_state(message)

    if is_correct_format(state_data, rows, cols):
        step_str = str(step).zfill(6)
        new_filename = f'./data/state_{step_str}.csv'
        shutil.copy(current_state_filename, new_filename)
        print(f'Copied {current_state_filename} to {new_filename}')
        print(state_data)
        save_current_state(state_data)
        print("save current data")
    else:
        print('error not correct format.')
