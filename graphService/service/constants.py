from graphService.makers.cpuGraph import GraphCPUMaker
from graphService.makers.diskAvgRwGraph import GraphDiskAvgRwMaker
from graphService.makers.diskQueueGraph import GraphDiskQueueCPUMaker
from graphService.makers.loadAvgGraph import GraphLoadAvgMaker
from graphService.makers.memoryGraph import GraphMemoryMaker
from graphService.makers.netGraph import GraphNetMaker
from graphService.makers.utilDiskCPUGraph import GraphUtilDiskCPUMaker
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


