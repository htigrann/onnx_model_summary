import onnx
import argparse

#Parsing arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Generating onnx model summary.")
    parser.add_argument("-model", "--model_path", help="Path to the onnx model.", required=True)
    parser.add_argument("-out", "--output_path", help="Path to the output file.", default='model_summary.txt')
    args = parser.parse_args()
    return args

# Load the ONNX model
def load_model(onnx_model_path):
    model = onnx.load(onnx_model_path)
    return model

def write_model_summary(output_file_path, model_path):
    model = load_model(model_path)

    with open(output_file_path, "w") as output_file:
        output_file.write("ONNX Model Summary:\n")
        # Iterate through the nodes in the graph
        for i, node in enumerate(model.graph.node):
            output_file.write(f"Layer {i}: {node.name} (OpType: {node.op_type})\n")
    
            # Get input shapes
            input_shapes = []
            for input_name in node.input:
                for input_info in model.graph.input:
                    if input_info.name == input_name:
                        input_shape = [dim.dim_value for dim in input_info.type.tensor_type.shape.dim]
                        input_shapes.append(f"{input_name}: {input_shape}")
            output_file.write("Input Shapes: " + ", ".join(input_shapes) + "\n")
    
            # Get output shapes
            output_shapes = []
            for output_name in node.output:
                for output_info in model.graph.output:
                    if output_info.name == output_name:
                        output_shape = [dim.dim_value for dim in output_info.type.tensor_type.shape.dim]
                        output_shapes.append(f"{output_name}: {output_shape}")
            output_file.write("Output Shapes: " + ", ".join(output_shapes) + "\n")
    
            output_file.write("\n")
    
        # Example: Get information about the input and output nodes
        input_node = model.graph.input[0]
        output_node = model.graph.output[0]
        input_shape = [dim.dim_value for dim in input_node.type.tensor_type.shape.dim]
        output_shape = [dim.dim_value for dim in output_node.type.tensor_type.shape.dim]
        output_file.write("Input Node Name: " + input_node.name + "\n")
        output_file.write("Input Node Shape: " + str(input_shape) + "\n")
        output_file.write("Output Node Name: " + output_node.name + "\n")
        output_file.write("Output Node Shape: " + str(output_shape) + "\n")


if __name__ == "__main__":
    args = parse_arguments()
    
    model_path = args.model_path
    output_file_path = args.output_path
    write_model_summary(output_file_path, model_path)

    print("Summary saved to", output_file_path)
