from graph_service.makers.cpuGraph import GraphCPUMaker
from graph_service.makers.diskAvgRwGraph import GraphDiskAvgRwMaker
from graph_service.makers.diskQueueGraph import GraphDiskQueueCPUMaker
from graph_service.makers.loadAvgGraph import GraphLoadAvgMaker
from graph_service.makers.memoryGraph import GraphMemoryMaker
from graph_service.makers.netGraph import GraphNetMaker
from graph_service.makers.utilDiskCPUGraph import GraphUtilDiskCPUMaker
from yaml import load, SafeLoader

def load_config(path_to_config):
    """Загружает конфигурационный файл в формате словаря"""
    with open(path_to_config) as f:
        return load(f, Loader=SafeLoader)

MAKERS = {
    "CPU graph": GraphCPUMaker,
    "MEMORY graph": GraphMemoryMaker,
    "NET graph": GraphNetMaker,
    "Load avg graph": GraphLoadAvgMaker,
    "Util disk cpu graph": GraphUtilDiskCPUMaker,
    "Disk queue graph": GraphDiskQueueCPUMaker,
    "Disk avg rw graph": GraphDiskAvgRwMaker
}


