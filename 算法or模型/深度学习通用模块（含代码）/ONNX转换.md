# ONNX转换

## pytorch ONNX转换
转换成onnx模型时，往往只需要`torch.onnx.export`就够了

```python
def export(model, args, f, export_params=True, verbose=False, training=TrainingMode.EVAL, 
           input_names=None, output_names=None, aten=False, export_raw_ir=False, 
           operator_export_type=None, opset_version=None, _retain_param_name=True, 
           do_constant_folding=True, example_outputs=None, strip_doc_string=True, 
           dynamic_axes=None, keep_initializers_as_inputs=None, custom_opsets=None, 
           enable_onnx_checker=True, use_external_data_format=False): 
```