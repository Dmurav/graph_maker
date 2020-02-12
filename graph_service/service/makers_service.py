
class GraphService:

    builder = None

    def __init__(self, source_file, output_dir, graph_maker):
        self.source_file = source_file
        self.builder = graph_maker(source_file, output_dir)

    def get_png_graph(self):
        self.builder.prepare_data()
        self.builder.make_graph()

    def show_graph(self):
        self.builder.prepare_data()
        self.builder.show()
