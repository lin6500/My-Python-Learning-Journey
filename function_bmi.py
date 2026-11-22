def fun_bmi(person, height, weight):
    if height <= 0 or weight <= 0:
        print("身高和体重必须大于0！")
        return

    print(person + "的身高：" + str(height) + "米")
    print(person + "的体重：" + str(weight) + "千克")

    bmi = weight / (height * height)
    print(person + "的BMI指数为：" + str(round(bmi, 2)))

    if bmi < 18.5:
        print("你这体型有点轻盈过头啦，快去吃点好吃的补一补！")

    if bmi >= 18.5 and bmi < 24.9:
        print("完美！你的身材管理很在线！")

    if bmi >= 24.9 and bmi < 29.9:
        print("最近伙食是不是有点太好了呀，适当运动一下吧！")

    if bmi >= 29.9:
        print("身体正在悄悄报警：该把减肥提上日程啦！")

    print("------------------------")


fun_bmi("路人甲", 1.83, 60)
fun_bmi("Lucy", 1.62, 50)
