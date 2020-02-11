from graphService.makers.cpuGraph import GraphCPUMaker
from graphService.service.Constants import MAKERS, load_config
from graphService.service.parametrServ import GraphService


from os import getcwd

if __name__ == "__main__":

    path_to_config = 'config.yaml'
    config = load_config(path_to_config)

    CPU = config['CPU']
    MEMORY = config["MEMORY"]
    NET = config["NET"]
    LOAD_AVG = config["LOAD_AVG"]
    UTIL_DISK_CPU = config["UTIL_DISK_CPU"]
    DISK_QUEUE = config["DISK_QUEUE"]
    DISK_AWG_RW = config["DISK_AWG_RW"]

    #CPU, MEMORY, NET, LOAD_AVG, UTIL_DISK_CPU, DISK_QUEUE, DISK_AWG_RW
    input = CPU

    #"CPU graph", "MEMORY graph","NET graph","Load avg graph","Util disk cpu graph","Disk queue graph","Disk avg rw graph"
    graph_maker = MAKERS["CPU graph"]

    graphService = GraphService(input, graph_maker)
    graphService.get_png_graph()
    graphService.show_graph()