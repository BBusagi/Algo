def visualize_list_horizontal(lst):
    # 计算每个盒子的宽度（基于最宽的元素）
    max_width = max(len(str(element)) for element in lst) + 2

    # 生成每个盒子的顶部、中间和底部部分
    box_top = '+' + '+'.join(['-' * max_width for _ in lst]) + '+'
    box_middle = '|' + '|'.join([str(element).center(max_width) for element in lst]) + '|'
    box_bottom = box_top

    # 打印盒子
    print(box_top)
    print(box_middle)
    print(box_bottom)

# 示例列表
my_list = [12, 345, 6789, 10]

# 横向可视化列表
visualize_list_horizontal(my_list)
