times = 0
valid_count = 0
total = 0

print("注意力小测试开始啦！准备好了吗？")
print("接下来需要录入6次反应时，单位是毫秒。")
print("有效范围：100～1500毫秒")
print("------------------------")

while times < 6:
    reaction_time = float(input("请输入第" + str(times + 1) + "次反应时（毫秒）："))
    times += 1

    if reaction_time < 100 or reaction_time > 1500:
        print("这个数值有点超出范围啦，本次先不计入统计哦！")
        continue

    valid_count += 1
    total += reaction_time

print("\n六次录入结束，来看看结果～")
print("有效数据数量：" + str(valid_count))

if valid_count > 0:
    average = total / valid_count
    print("有效反应时的平均值是：" + str(average) + "毫秒")
    print("统计完成，辛苦啦！")
else:
    print("这次没有收集到有效数据，下次再试试吧！")
