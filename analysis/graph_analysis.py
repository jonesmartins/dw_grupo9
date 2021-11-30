import sqlite3
import matplotlib.pyplot as plt
from dictionaries.paths_dict import database_root_path


def plot_barh(title, marks, names, fig_size=(9, 5)):
    plt.rcParams["figure.figsize"] = fig_size
    plt.barh(names["values"], marks["values"])
    plt.ylabel(names["label"])
    plt.xlabel(marks["label"])
    plt.title(title)
    plt.show()


def plot_bar(title, marks, names, fig_size=(5, 9)):
    plt.rcParams["figure.figsize"] = fig_size
    plt.bar(names["values"], marks["values"])
    plt.xlabel(names["label"])
    plt.ylabel(marks["label"])
    plt.title(title)
    plt.show()


# Qual a diferença percentual entre capacidade de testes para população e para profissionais
def capacidade_profissionais_populacao(connection_cursor):
    result = connection_cursor.execute(
        "SELECT avg(capacidade_teste_profissionais), avg(capacidade_teste_populacao)"
        "as avgnota FROM capacidade_teste_populacao, capacidade_teste_profissionais"
    ).fetchall()
    profissionais = result[0][0] / (result[0][0] + result[0][1])
    populacao = result[0][1] / (result[0][0] + result[0][1])
    plot_bar("Capacidades de testes média entre população e profissionais",
             {"label": "sexo", "values": [profissionais, populacao]},
             {"label": "capacidade média", "values": ['medicos', 'populacao']})


def generate_plots(connection_cursor):
    print('Starting loading plots')
    capacidade_profissionais_populacao(connection_cursor)
    print('Finishing loading plots')


if __name__ == '__main__':
    print('Starting connection')
    connection = sqlite3.connect(database_root_path)
    generate_plots(connection.cursor())
    print('Closing connection')
    connection.close()
