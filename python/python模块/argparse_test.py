import argparse
def main():
    # 创建 ArgumentParser 对象，用于解析命令行参数
    parser = argparse.ArgumentParser(description='一个简单的命令行参数示例')

    # 添加需要解析的命令行参数
    parser.add_argument('param1', type=str, help='第一个参数的说明')
    parser.add_argument('-param_2', type=int, help='第二个参数需要加-param2')
    parser.add_argument('-param3', type = int, default=66)
    parser.add_argument('-param4', action="store_true")    

    # 解析命令行参数
    args = parser.parse_args()
    print(type(args))

    # 访问解析后的参数值
    param1_value = args.param1
    param2_value = args.param_2
    param3_value = args.param3
    param4_value = args.param4
    # 在这里处理参数值
    print(f'参数 param1 的值为: {param1_value}')
    print(f'参数 param2 的值为: {param2_value+5}')
    print(f'参数 param3 的值为: {param3_value+5}')
    print(f'参数 param4 的值为: {param4_value}')
    

if __name__ == '__main__':
    """
    PS Z:\learning documents\python\python模块> 
    python .\argparse_test.py ggg -param2 52
    <class 'argparse.Namespace'>
    参数 param1 的值为: ggg
    参数 param2 的值为: 57
    参数 param3 的值为: 71
    参数 param4 的值为: False
    """
    main()