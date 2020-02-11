import matplotlib.pyplot as plt

from graphService.makers.dataMaker import prepareData


class GraphLoadAvgMaker:
    source_file = ""
    dates = []
    graph_data_1 = []
    graph_data_2 = []
    graph_data_3 = []

    def __init__(self, source_file):
        self.source_file = source_file

    def prepare_data(self):
        list_data = prepareData(self.source_file)
        self.dates = list_data[0]
        self.graph_data_1 = list_data[1]
        self.graph_data_2 = list_data[2]
        self.graph_data_3 = list_data[3]

    def make_graph(self):
        # Устанавливаем размер графика
        fig, ax = plt.subplots(figsize=(8, 4))

        # Устанавливаем подписи
        ax.set_title("Динамика Load Average", fontsize=16)
        ax.set_ylabel('Значение коэффициента', fontsize=10)
        ax.set_xlabel('Продолжительность теста, ч:мм', fontsize=10)

        fig.tight_layout()

        # Строим график
        plt.plot(self.dates, self.graph_data_1, label='за 1 минуту')
        plt.plot(self.dates, self.graph_data_2, label='за 5 минут')
        plt.plot(self.dates, self.graph_data_3, label='за 15 минут')
        # Устанавливаем сетку
        plt.grid()
        # Устанавливаем легенду
        plt.legend()
        plt.gcf()
        # создать файл с графиком
        plt.savefig("result/graph_load_avg.png")

    def show(self):
        plt.show()