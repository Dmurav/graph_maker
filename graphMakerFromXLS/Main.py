from graphMakerFromXLS.services.graphCPUService import GraphCPUService


if __name__ == "__main__":

    SOURCE_FILE = '../data_source/CPU_data.xlsx'

    graphService = GraphCPUService(SOURCE_FILE)

    graphService.get_png_graph()
    graphService.show_graph()