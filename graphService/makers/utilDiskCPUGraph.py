import matplotlib.pyplot as plt

from graphService.makers.dataMaker import prepareData


class GraphUtilDiskCPUMaker:
    source_file = ""
    dates = []
    graph_data_1 = []

    def __init__(self, source_file):
        self.source_file = source_file

    def prepare_data(self):
        list_data = prepareData(self.source_file)
        self.dates = list_data[0]
        self.graph_data_1 = list_data[1]

    def make_graph(self):
        # Устанавливаем размер графика
        fig, ax = plt.subplots(figsize=(8, 4))

        # Устанавливаем подписи
        ax.set_title("Утилизация CPU дисковой подсистемой", fontsize=16)
        ax.set_ylabel('Утилизация диска, %', fontsize=10)
        ax.set_xlabel('Продолжительность теста, ч:мм', fontsize=10)

        fig.tight_layout()

        # Строим график
        plt.plot(self.dates, self.graph_data_1, label='Утилизация диска')
        # Устанавливаем сетку
        plt.grid()
        # Устанавливаем легенду
        plt.legend()

        plt.gcf()
        # создать файл с графиком
        plt.savefig("result/graph_util_disk.png")

    def show(self):
        plt.show()