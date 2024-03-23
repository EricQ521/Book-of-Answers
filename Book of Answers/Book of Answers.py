import random
import time

# 定义答案之书中的答案列表
answers = [
    "毫无疑问，你的想法是正确的，去做吧！",
    "或许你应该考虑所有可能性，再做决定。",
    "有时候，最好的答案来自于内心的平静，深呼吸，放松。",
    "这是一个值得尝试的选择，不要害怕冒险，勇敢一点。",
    "你可能需要更多的时间来思考这个问题，不要急于求成。",
    "信任你的直觉，它通常不会误导你，除非你有确切的理由怀疑。",
    "现在不是做决定的最佳时机，等待更好的时机吧。",
    "你的朋友和家人会给你提供有价值的见解，不妨和他们聊聊。",
    "跟随你的梦想，它们可能会带你走向正确的道路，只要你愿意付出努力。",
    "有时候，最简单的解决方案往往是最有效的，不要忽视基础的方法。",
    "不要害怕寻求专业的建议，他们可能会给你一个全新的视角。",
    "你已经知道答案，只是还没有准备好面对它，是时候正视问题了。",
    "这是一个学习和成长的机会，拥抱变化，让自己变得更强。",
    "保持耐心，答案会在最意想不到的时刻出现，有时候需要的只是时间。",
    "你的道路可能不会一帆风顺，但每一步都是必要的，坚持下去。",
    "有时候，放慢脚步，享受旅程比到达目的地更重要。",
    "你可能正处在人生的十字路口，选择哪条路，你需要仔细权衡。",
    "不要让恐惧阻碍你的步伐，相信自己的能力，你能够克服困难。",
    "答案可能并不是你期望的那样，但请保持开放的心态，接受可能的结果。",
    "你的内心已经知道答案，倾听它，不要被外界的声音干扰。",
    "这是一个新开始的标志，放下过去，勇敢地迈出下一步。"
]

# 答案之书查询函数
def answer_book(question):
    positive_keywords = ["是", "想要", "应该", "希望", "可以"]
    negative_keywords = ["不", "担心", "害怕", "怀疑", "犹豫"]

    # 检查问题中是否包含积极的语气
    is_positive = any(keyword in question.lower() for keyword in positive_keywords)
    # 检查问题中是否包含消极的语气
    is_negative = any(keyword in question.lower() for keyword in negative_keywords)

    # 根据问题的语气选择不同的答案
    if is_positive and not is_negative:
        positive_answers = [ans for ans in answers if "去做" in ans or "尝试" in ans or "梦想" in ans]
        return random.choice(positive_answers)
    elif is_negative and not is_positive:
        negative_answers = [ans for ans in answers if "等待" in ans or "思考" in ans or "害怕" in ans]
        return random.choice(negative_answers)
    else:
        # 如果问题既不积极也不消极，或者两者都有，随机选择答案
        return random.choice(answers)

# 清理控制台
def clear_console():
    # 对于Windows系统
    if os.name == 'nt':
        os.system('cls')
    # 对于Unix/Linux/macOS系统
    else:
        os.system('clear')

# 主程序
def main():
    print("欢迎来到答案之书！在这里，你可以找到你心中的答案。")
    while True:
        clear_console()
        question = input("请提出你的问题（如果你想要结束提问，请输入'结束'）：")
        if question.lower() == '结束':
            print("感谢你的访问，希望下次再见！")
            break
        time.sleep(1)  # 增加等待时间，模拟翻书效果
        result = answer_book(question)
        print("\n答案之书的回答是：" + result)
        time.sleep(1)  # 增加等待时间，模拟翻书效果

# 导入os模块以清空控制台
import os
# 运行主程序
if __name__ == "__main__":
    main()
