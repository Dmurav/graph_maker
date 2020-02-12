import matplotlib.pyplot as plt

from graph_service.makers.dataMaker import graph_data_from_xlsx


class GraphDiskAvgRwMaker:
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
        ax.set_title("Среднее время чтения/записи\n дисковой подсистемы", fontsize=16)
        ax.set_ylabel('Время, мс', fontsize=10)
        ax.set_xlabel('Продолжительность теста, ч:мм', fontsize=10)

        fig.tight_layout()

        # Строим график
        plt.plot(self.dates, self.graph_data_1, label='Среднее время выполнения чтения/записи')
        plt.plot(self.dates, self.graph_data_2, label='Среднее время обслуживания чтения/записи')
        # Устанавливаем сетку
        plt.grid()
        # Устанавливаем легенду
        plt.legend(loc='upper right')

        plt.gcf()
        # создать файл с графиком
        plt.savefig("result/graph_disk_avg_rw.png")

    def show(self):
        plt.show()