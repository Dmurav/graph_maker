import matplotlib.pyplot as plt

from graph_service.makers.dataMaker import graph_data_from_xlsx


class GraphCPUMaker:
    source_file = ""
    dates = []
    graph_data_1 = []
    graph_data_2 = []

    def __init__(self, source_file):
        self.source_file = source_file

    def prepare_data(self):
        list_data = graph_data_from_xlsx(self.source_file)
        self.dates = list_data[0]
        self.graph_data_1 = list_data[1]
        self.graph_data_2 = list_data[2]

    def make_graph(self):
        # Устанавливаем размер графика
        fig, ax = plt.subplots(figsize=(8, 4))
        # Устанавливаем подписи
        ax.set_title("Утилизация CPU", fontsize=16)
        ax.set_ylabel('Значение коэфициента', fontsize=10)
        ax.set_xlabel('Продолжительность теста, ч:мм', fontsize=10)
        fig.tight_layout()
        # Строим график
        plt.plot(self.dates, self.graph_data_1, label='Утилизация CPU')
        plt.plot(self.dates, self.graph_data_2, label='Длина очереди CPU')
        # Устанавливаем сетку
        plt.grid()
        # Устанавливаем легенду
        plt.legend(loc='upper right')
        plt.savefig("result/graph_cpu.png")


    def show(self):
        plt.show()