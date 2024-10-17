数据预处理工作包含三个python文件：

step1(extract_state.py): 首先运行该文件，请预先创建好“extract_CA"文件夹，该部分代码是将原数据集中”state“为”CA“的数据提取出来，保存在“extract_CA"文件夹下；

step2(download_relevant_package.py): 因为后续需要用到nltk库中的停用词表，标点集合等工具，需要预先下载下来；

step3(dataset preprocessing.py): 该步骤是对提取出来的信息，某些特定的字段进行数据预处理，如转换大小写等，便于后续的搜索引擎开发工作。请先创建好”processed_data"文件夹，然后运行该文件。processed_data下的三个文件即为最后的数据处理结果。

备注：因为某些文件尺寸较大，并包含大量的写文件操作，所以部分代码运行需要等待一定时间。但是大部分是可以迅速完成的。