questions = [
    ['Who is the Owner of Fb?', 'Elon Musk', 'Mark Zuckerberg', 'Bill Gates', 'None', 2],
    ['Who is the Owner of MS?', 'Elon Musk', 'Mark Zuckerberg', 'Bill Gates', 'None', 3],
    ['Who is the Owner of X?', 'Elon Musk', 'Mark Zuckerberg', 'Bill Gates', 'None', 1],
    ['Who is the Owner of Tiktok?', 'Elon Musk', 'Mark Zuckerberg', 'Bill Gates', 'None', 4],
    ['Who is the Owner of Instagram?', 'Elon Musk', 'Mark Zuckerberg', 'Bill Gates', 'None', 2]
]
levels = [1000, 2000,3000,4000,5000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f'\nQuestion for Tk. {levels[i]}')
    print(f"{i}. {question[0]}")
    print(f'a. {question[1]}            b.{question[2]}')
    print(f'c. {question[3]}            d.{question[4]}')
    reply = int(input("Enter Your answer (1-4) of 0 for quit: "))
    if reply == 0:
        money = levels[i-1]
        break

    if reply == question[-1]:
        print(f'Correct answer, You have won Tk. {levels[i]} ')
        money = levels[i]

    else:
        print('Wrong answer!')
        break
print(f"Your take home money is Tk. {money}")
