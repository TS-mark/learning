|名称|作用|参数|
|-|-|-|
|Conv2d|2维卷积|in_channels: int,<br>out_channels: int,<br>kernel_size: _size_2_t,<br>stride: _size_2_t = 1,<br>padding: Union[str, _size_2_t] = 0,<br>dilation: _size_2_t = 1,<br>groups: int = 1,<br>bias: bool = True,<br>padding_mode: str = 'zeros',  # TODO: refine this type<br>device=None,<br>dtype=None<br>|
|MaxPool2d|最大池化层|kernel_size: _size_2_t<br>stride: _size_2_t<br>padding: _size_2_t<br>dilation: _size_2_t|