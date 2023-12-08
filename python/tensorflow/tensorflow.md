tf.nn.embedding_lookup(

               params,

               ids,

               partition_strategy='mod',

               name=None,

              validate_indices=True,

              max_norm=None

)
params: 表示完整的嵌入张量，或者除了第一维度之外具有相同形状的P个张量的列表，表示经分割的嵌入张量

tf.nn.embedding_lookup(tensor,id)：即tensor就是输入的张量，id 就是张量对应的索引

tf.nn.embedding_lookup()就是根据input_ids中的id，寻找embeddings中的第id行。比如input_ids=[1,3,5]，则找出embeddings中第1，3，5行，组成一个tensor返回

一般做自然语言相关的。需要把每个词都映射成向量，这个向量可以是word2vec预训练好的，也可以是在网络里训练的，在网络里需要先把词的id转换成对应的向量，这个函数就是做这件事的

|函数名|用法|参数|
|---|---|---|
|tf.nn.embedding_lookup()|把每个词映射成向量。<br>（这个向量可以是word2vec预训练的，也可以是在网络中训练的）|params<br>ids<br>|