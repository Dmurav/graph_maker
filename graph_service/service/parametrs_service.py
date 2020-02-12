from graph_service.graph_makers.cpuGraph import GraphCPUMaker
from graph_service.graph_makers.diskAvgRwGraph import GraphDiskAvgRwMaker
from graph_service.graph_makers.diskQueueGraph import GraphDiskQueueCPUMaker
from graph_service.graph_makers.loadAvgGraph import GraphLoadAvgMaker
from graph_service.graph_makers.memoryGraph import GraphMemoryMaker
from graph_service.graph_makers.netGraph import GraphNetMaker
from graph_service.graph_makers.utilDiskCPUGraph import GraphUtilDiskCPUMaker
from yaml import load, SafeLoader


def load_config(path_to_config):
    """Загружает конфигурационный файл в формате словаря"""
    with open(path_to_config) as f:
        return load(f, Loader=SafeLoader)


def make_selection(graph_name, config):
    if graph_name == "CPU":
        graph_name = config[graph_name]
        graph_maker = MAKERS["CPU graph"]
        return [graph_name, graph_maker]
    elif graph_name == "MEMORY":
        graph_name = config[graph_name]
        graph_maker = MAKERS["MEMORY graph"]
        return [graph_name, graph_maker]
    elif graph_name == "NET":
        graph_name = config[graph_name]
        graph_maker = MAKERS["NET graph"]
        return [graph_name, graph_maker]
    elif graph_name == "LOAD_AVG":
        graph_name = config[graph_name]
        graph_maker = MAKERS["Load avg graph"]
        return [graph_name, graph_maker]
    elif graph_name == "UTIL_DISK_CPU":
        graph_name = config[graph_name]
        graph_maker = MAKERS["Util disk cpu graph"]
        return [graph_name, graph_maker]
    elif graph_name == "DISK_QUEUE":
        graph_name = config[graph_name]
        graph_maker = MAKERS["Disk queue graph"]
        return [graph_name, graph_maker]
    elif graph_name == "DISK_AWG_RW":
        graph_name = config[graph_name]
        graph_maker = MAKERS["Disk avg rw graph"]
        return [graph_name, graph_maker]

# Карта с классами, производящими графики
MAKERS = {
    "CPU graph": GraphCPUMaker,
    "MEMORY graph": GraphMemoryMaker,
    "NET graph": GraphNetMaker,
    "Load avg graph": GraphLoadAvgMaker,
    "Util disk cpu graph": GraphUtilDiskCPUMaker,
    "Disk queue graph": GraphDiskQueueCPUMaker,
    "Disk avg rw graph": GraphDiskAvgRwMaker
}

VARIANTS = ["CPU","MEMORY","NET","LOAD_AVG","UTIL_DISK_CPU","DISK_QUEUE","DISK_AWG_RW"]

DESCRIPTION = "Please select one graph, you want get:\n"\
                "\n"\
                "CPU - утилизация центрального процессора,\n"\
                "MEMORY - утилизация опертивной памяти,\n"\
                "NET - утилизаци сетевых ресурсов,\n"\
                "LOAD_AVG - динамика Load Average,\n"\
                "UTIL_DISK_CPU - утилизация CPU дисковой подсистемой,\n"\
                "DISK_QUEUE - очередь дисковой подсистемы,\n"\
                "DISK_AWG_RW - Среднее время чтения/записи дисковой подсистемы\n"\
                "\n"\
                "Please enter EXIT, if you want stop program"
