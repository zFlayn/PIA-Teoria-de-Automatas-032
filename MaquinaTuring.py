import tkinter as tk

def turing_machine(input_string):
    # Verificar la longitud de la cadena
    if len(input_string) % 4 != 0:
        return False

    # Definir la tabla de transiciones
    transitions = {
        ('q0', 'a'): ('q1', 'ƀ', 'R'),
        ('q0', 'b'): ('q1', 'ƀ', 'R'),
        ('q1', 'a'): ('q2', 'ƀ', 'R'),
        ('q1', 'b'): ('q2', 'ƀ', 'R'),
        ('q2', 'a'): ('q3', 'ƀ', 'R'),
        ('q2', 'b'): ('q3', 'ƀ', 'R'),
        ('q3', 'a'): ('q0', 'ƀ', 'R'),
        ('q3', 'b'): ('q0', 'ƀ', 'R'),
        ('q0', 'ƀ'): ('qAceptación', 'ƀ', 'S')
    }

    # Definir variables iniciales
    tape = list(input_string)
    tape.append('ƀ')  # Agregar el símbolo en blanco al final de la cinta
    state = 'q0'
    head_position = 0

    # Ejecutar la máquina de Turing
    while state != 'qAceptación':
        current_symbol = tape[head_position]
        if (state, current_symbol) not in transitions:
            return False  # La transición no está definida para el estado actual y el símbolo actual
        new_state, new_symbol, direction = transitions[(state, current_symbol)]
        tape[head_position] = new_symbol
        if direction == 'R':
            head_position += 1
        elif direction == 'L':
            head_position -= 1
        state = new_state

    return True

def check_input():
    input_string = input_entry.get()
    if turing_machine(input_string):
        result_label.config(text="La cadena es válida según las reglas de la máquina de Turing.")
    else:
        result_label.config(text="La cadena no es válida según las reglas de la máquina de Turing.")