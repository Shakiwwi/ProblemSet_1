def convert(emotion):
    return emotion.replace(":)", "🙂").replace(":(", "🙁")



def main():
    emotion = input("how do you feel today? ")
    result = convert(emotion)
    print(result)

main()