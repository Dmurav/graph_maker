import os
from sys import path


script_dir = os.path.dirname(__file__)
path.insert(0, script_dir)

from graph_service.service.parametrs_service import load_config, VARIANTS, DESCRIPTION, make_selection
from graph_service.service.makers_service import GraphService


if __name__ == "__main__":

    path_to_config = os.path.join(script_dir, 'config.yaml')
    config = load_config(path_to_config)
    output_dir = config["OUTPUT_DIR"]
    graph_maker = None

    print(DESCRIPTION)
    graph_name = input()

    while True:
        if graph_name in VARIANTS:
            args_for_graphService = make_selection(graph_name, config)
            graph_name = args_for_graphService[0]
            graph_maker = args_for_graphService[1]

            graphService = GraphService(graph_name, output_dir, graph_maker)
            graphService.get_png_graph()
            graphService.show_graph()
        elif graph_name == "EXIT":
            break
        else:
            print("Please enter new graph.")
            graph_name = input()


