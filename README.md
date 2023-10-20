# ONNX Model Summary Generator

This script generates a summary of an ONNX model, providing information about the layers, input shapes, and output shapes. It is a useful tool for understanding the structure of ONNX models. 

The `onnx_model_summary.py` has two input parameters
`-model` or `--model_path` for specifing the input model's path
`-out` or `--output_path` the output filename where to be stored the model's summary, if not specify this it'll write the summary in `model_summary.txt` file.

For more information one can run 
``` 
python3 onnx_model_summary.py -help
```
## Installation

1. **Clone the Repository**:
  ```
git clone git@github.com:htigrann/onnx_model_summary.git
```
2. **Change to that directory**
```
cd onnx_model_summary
```
3. **Install the requried library**
```
pip3 install onnx
```

## How to run
Simply change `$PATH_TO_ONNX_MODEL` and `$OUTPUT_FILENAME` to your specific paths and run the following:

``` 
python3 onnx_model_summary.py -model $PATH_TO_ONNX_MODEL -out $OUTPUT_FILENAME
