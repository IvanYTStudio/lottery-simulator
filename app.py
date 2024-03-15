import secrets
import streamlit as st
from time import sleep

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]

winnings = {0:0,1:0,2:0,3:100,4:1_000,5:22_000,6:730_000,7:600_000_000}

def check_numbers(player_numbers):
    if len(player_numbers) != 7:
        return False
    elif len(player_numbers) != len(list(dict.fromkeys(player_numbers))):
        return False
    else:
        return True

def draw():
    if check_numbers(player_numbers=player_numbers):
        drawn_numbers = []
        for _ in range(7):
            num = secrets.choice(numbers)
            drawn_numbers.append(num)
            numbers.remove(num)
        st.session_state['drawn_number_1'] = drawn_numbers[0]
        st.session_state['drawn_number_2'] = drawn_numbers[1]
        st.session_state['drawn_number_3'] = drawn_numbers[2]
        st.session_state['drawn_number_4'] = drawn_numbers[3]
        st.session_state['drawn_number_5'] = drawn_numbers[4]
        st.session_state['drawn_number_6'] = drawn_numbers[5]
        st.session_state['drawn_number_7'] = drawn_numbers[6]
        drawn_numbers = [int(num) for num in drawn_numbers]
        calculate_result(player_numbers=player_numbers, drawn_numbers=drawn_numbers)
        color_numbers(player_numbers=player_numbers, drawn_numbers=drawn_numbers)
    sleep(0.5)
    return None

def calculate_result(player_numbers, drawn_numbers):
    matched_numbers = [num for num in player_numbers if num in drawn_numbers]
    money_won = winnings[len(matched_numbers)]
    st.session_state['amount_won'] += money_won
    st.session_state['amount_bet'] += 100
    return None

def run_simulations():
    if check_numbers(player_numbers=simulation_player_numbers):
        for _ in range(runs):
            drawn_numbers = []
            for _ in range(7):
                num = secrets.choice(numbers)
                drawn_numbers.append(num)
                numbers.remove(num)
            matched_numbers = [num for num in player_numbers if num in drawn_numbers]
            st.session_state['simulations_amount_won'] += winnings[len(matched_numbers)]
            numbers.extend(drawn_numbers)
        st.session_state['simulations_amount_bet'] += runs * 100
    return None

def color_numbers(player_numbers, drawn_numbers):
    number_colors = ""
    for num in drawn_numbers:
        if num in player_numbers:
            number_colors += f"#drawn_number_{str(drawn_numbers.index(num)+1)} {{color:green}}"
        else:
            number_colors += f"#drawn_number_{str(drawn_numbers.index(num)+1)} {{color:red}}"
    st.markdown(f'<style>{number_colors}</style>', unsafe_allow_html=True)

def reset():
    st.session_state['drawn_number_1'] = 1
    st.session_state['drawn_number_2'] = 2
    st.session_state['drawn_number_3'] = 3
    st.session_state['drawn_number_4'] = 4
    st.session_state['drawn_number_5'] = 5
    st.session_state['drawn_number_6'] = 6
    st.session_state['drawn_number_7'] = 7
    st.session_state['amount_bet'] = 0
    st.session_state['amount_won'] = 0
    st.session_state['result'] = 0

def reset_simulations():
    st.session_state['simulations_amount_bet'] = 0
    st.session_state['simulations_amount_won'] = 0
    st.session_state['simulations_amount_results'] = 0

st.set_page_config(page_title='Lottery Simulator', page_icon='favicon.ico', layout='wide')

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

if 'drawn_number_1' not in st.session_state:
    st.session_state['drawn_number_1'] = 1

if 'drawn_number_2' not in st.session_state:
    st.session_state['drawn_number_2'] = 2

if 'drawn_number_3' not in st.session_state:
    st.session_state['drawn_number_3'] = 3

if 'drawn_number_4' not in st.session_state:
    st.session_state['drawn_number_4'] = 4

if 'drawn_number_5' not in st.session_state:
    st.session_state['drawn_number_5'] = 5

if 'drawn_number_6' not in st.session_state:
    st.session_state['drawn_number_6'] = 6

if 'drawn_number_7' not in st.session_state:
    st.session_state['drawn_number_7'] = 7

if 'amount_bet' not in st.session_state:
    st.session_state['amount_bet'] = 0

if 'amount_won' not in st.session_state:
    st.session_state['amount_won'] = 0

if 'result' not in st.session_state:
    st.session_state['result'] = 0

if 'simulations_runs' not in st.session_state:
    st.session_state['simulations_runs'] = 1000

if 'simulations_amount_bet' not in st.session_state:
    st.session_state['simulations_amount_bet'] = 0

if 'simulations_amount_won' not in st.session_state:
    st.session_state['simulations_amount_won'] = 0

if 'simulations_results' not in st.session_state:
    st.session_state['simulations_results'] = 0

if 'auto_numbers_checkbox' not in st.session_state:
    st.session_state['auto_numbers_checkbox'] = True

st.title("Lottery Simulator", anchor='title')

tab1, tab2 = st.tabs(['Play lottery', 'Simulations'])

with tab1:

    st.title("Enter your numbers", anchor='subtitle')

    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

    with col2:
        player_number_1 = st.number_input(label='A', min_value=1, max_value=39, value=1, label_visibility='hidden', key='number_1')
    with col3:
        player_number_2 = st.number_input(label='B', min_value=1, max_value=39, value=2, label_visibility='hidden', key='number_2')
    with col4:
        player_number_3 = st.number_input(label='C', min_value=1, max_value=39, value=3, label_visibility='hidden', key='number_3')
    with col5:
        player_number_4 = st.number_input(label='D', min_value=1, max_value=39, value=4, label_visibility='hidden', key='number_4')
    with col6:
        player_number_5 = st.number_input(label='E', min_value=1, max_value=39, value=5, label_visibility='hidden', key='number_5')
    with col7:
        player_number_6 = st.number_input(label='F', min_value=1, max_value=39, value=6, label_visibility='hidden', key='number_6')
    with col8:
        player_number_7 = st.number_input(label='G', min_value=1, max_value=39, value=7, label_visibility='hidden', key='number_7')

    player_numbers = [player_number_1, player_number_2, player_number_3, player_number_4, player_number_5, player_number_6, player_number_7]

    if not check_numbers(player_numbers=player_numbers):
        st.error('The numbers you enterd are not valid!')

    st.divider()

    st.title("Drawn numbers", anchor='subtitle')

    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

    with col2:
        st.title(st.session_state['drawn_number_1'], anchor='drawn_number_1')
    with col3:
        st.title(st.session_state['drawn_number_2'], anchor='drawn_number_2')
    with col4:
        st.title(st.session_state['drawn_number_3'], anchor='drawn_number_3')
    with col5:
        st.title(st.session_state['drawn_number_4'], anchor='drawn_number_4')
    with col6:
        st.title(st.session_state['drawn_number_5'], anchor='drawn_number_5')
    with col7:
        st.title(st.session_state['drawn_number_6'], anchor='drawn_number_6')
    with col8:
        st.title(st.session_state['drawn_number_7'], anchor='drawn_number_7')

    st.divider()

    col1, col2, col3, col4, col5, col6, col7 = st.columns([0.5,1,2,2,2,1,0.5])

    amount_bet = 0
    amount_won = 0
    result = amount_won - amount_bet

    with col2:
        st.title('Placeholder', anchor='placeholder')
        st.button('Reset', key='reset_button', on_click=reset)
    with col3:
        st.title(f'{st.session_state["amount_bet"]:,}', anchor='amount_bet')
        st.subheader('Money bet', anchor='amount_descriptions')
    with col4:
        st.title(f'{st.session_state["amount_won"]:,}', anchor='amount_won')
        st.subheader('Money won', anchor='amount_descriptions')
    with col5:
        st.title(f'{st.session_state["amount_won"] - st.session_state["amount_bet"]:,}', anchor='result')
        st.subheader('Result', anchor='amount_descriptions')
    with col6:
        st.title('Placeholder', anchor='placeholder')
        st.button('Play', key='play_button', on_click=draw)

with tab2:

    st.title("Enter your numbers", anchor='subtitle')

    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

    st.checkbox('Automatic number selection', help='If you check this, it will generate a random set of 7 numbers for each run. If you want to use the same set of numbers for all the runs, uncheck this and enter the numbers you want to use.', key='auto_numbers_checkbox')
    if st.session_state['auto_numbers_checkbox'] == True:
        with col2:
            simulations_player_number_1 = st.number_input(label='A', min_value=1, max_value=39, value=1, label_visibility='hidden', disabled=True, key='tab2_number_1')
        with col3:
            simulations_player_number_2 = st.number_input(label='B', min_value=1, max_value=39, value=2, label_visibility='hidden', disabled=True, key='tab2_number_2')
        with col4:
            simulations_player_number_3 = st.number_input(label='C', min_value=1, max_value=39, value=3, label_visibility='hidden', disabled=True, key='tab2_number_3')
        with col5:
            simulations_player_number_4 = st.number_input(label='D', min_value=1, max_value=39, value=4, label_visibility='hidden', disabled=True, key='tab2_number_4')
        with col6:
            simulations_player_number_5 = st.number_input(label='E', min_value=1, max_value=39, value=5, label_visibility='hidden', disabled=True, key='tab2_number_5')
        with col7:
            simulations_player_number_6 = st.number_input(label='F', min_value=1, max_value=39, value=6, label_visibility='hidden', disabled=True, key='tab2_number_6')
        with col8:
            simulations_player_number_7 = st.number_input(label='G', min_value=1, max_value=39, value=7, label_visibility='hidden', disabled=True, key='tab2_number_7')
    else:
        with col2:
            simulations_player_number_1 = st.number_input(label='A', min_value=1, max_value=39, value=1, label_visibility='hidden', key='tab2_number_1')
        with col3:
            simulations_player_number_2 = st.number_input(label='B', min_value=1, max_value=39, value=2, label_visibility='hidden', key='tab2_number_2')
        with col4:
            simulations_player_number_3 = st.number_input(label='C', min_value=1, max_value=39, value=3, label_visibility='hidden', key='tab2_number_3')
        with col5:
            simulations_player_number_4 = st.number_input(label='D', min_value=1, max_value=39, value=4, label_visibility='hidden', key='tab2_number_4')
        with col6:
            simulations_player_number_5 = st.number_input(label='E', min_value=1, max_value=39, value=5, label_visibility='hidden', key='tab2_number_5')
        with col7:
            simulations_player_number_6 = st.number_input(label='F', min_value=1, max_value=39, value=6, label_visibility='hidden', key='tab2_number_6')
        with col8:
            simulations_player_number_7 = st.number_input(label='G', min_value=1, max_value=39, value=7, label_visibility='hidden', key='tab2_number_7')

    simulation_player_numbers = [simulations_player_number_1, simulations_player_number_2, simulations_player_number_3, simulations_player_number_4, simulations_player_number_5, simulations_player_number_6, simulations_player_number_7]
    if not check_numbers(player_numbers=simulation_player_numbers):
        st.error('The numbers you enterd are not valid!')
    st.divider()

    col1, col2, col3, col4, col5 = st.columns([0.5,2,2,2,0.5])

    amount_bet = 0
    amount_won = 0
    result = amount_won - amount_bet
    
    st.divider()

    with col2:
        st.title(f'{st.session_state["simulations_amount_bet"]:,}', anchor='simulations_amount_bet')
        st.subheader('Amount bet', anchor='amount_descriptions')
    with col3:
        st.title(f'{st.session_state["simulations_amount_won"]:,}', anchor='simulations_amount_won')
        st.subheader('Amount won', anchor='amount_descriptions')
    with col4:
        st.title(f'{st.session_state["simulations_amount_won"] - st.session_state["simulations_amount_bet"]:,}', anchor='simulations_result')
        st.subheader('Result', anchor='amount_descriptions')

    col1, col2, col3, col4, col5 = st.columns([0.5, 1, 1, 1, 0.5])

    with col2:
        st.button(label='Reset', key='reset_simulations', on_click=reset_simulations)
    with col3:
        runs = st.number_input(label='AAAA',min_value=1, max_value=100000, label_visibility='hidden', key='simulations_runs')
    with col4:
        st.button(label='Run', key='run_simulations', on_click=run_simulations)