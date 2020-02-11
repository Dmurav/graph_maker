from graphMakerFromXLS.makers.cpuGraph import GraphCPUBuilder


class GraphCPUService:

    builder = None

    def __init__(self, source_file):
        self.source_file = source_file
        self.builder = GraphCPUBuilder(source_file)

    def get_png_graph(self):
        self.builder.prepare_data()
        self.builder.make_graph_cpu()


    def show_graph(self):
        self.builder.prepare_data()
        self.builder.show_cpu_graph()
