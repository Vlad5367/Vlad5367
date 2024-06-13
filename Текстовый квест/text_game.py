def start_quest():
    print("Добро пожаловать в квест 'Новенький в школе'!")
    print("Вы - новенький в школе и сегодня ваш первый день. Вы входите в класс и видите неочень приятного нового одноклассника, который подходит к вам.")

    print("\nВыберите действие:")
    print("1. Попытаться уйти мирным путем")
    print("2. Сказать что-то смешное, чтобы разрядить обстановку")
    print("3. Встать в защитную позицию и сказать, чтобы он не приближался")
    print("4. Попробовать подружиться, предложив помощь в чем-то")

    user_choice = input("Ваш выбор (1-4): ")

    if user_choice == "1":
        print("\nВы пытаетесь уйти мирным путем, избегая конфликта.")
        peaceful_resolution()
    elif user_choice == "2":
        print("\nВы говорите что-то смешное, пытаясь разрядить обстановку.")
        funny_comment()
    elif user_choice == "3":
        print("\nВы встаете в защитную позицию и говорите, чтобы он не приближался.")
        defend_yourself()
    elif user_choice == "4":
        print("\nВы предлагаете помощь в чем-то, пытаясь подружиться.")
        make_friends()

def peaceful_resolution():
    print("Ваше стремление избежать конфликта вызывает уважение некоторых одноклассников.")
    print("Они видят, что вы не ищете проблем, и начинают вас уважать.")
    print("Вы становитесь частью дружной компании.")

def funny_comment():
    print("Ваша шутка смешивает одноклассников, включая новенького.")
    print("Он начинает смеяться и говорит, что вы веселый человек.")
    print("Вы смогли избежать конфликта и создать позитивное впечатление.")

def defend_yourself():
    print("Ваша защитная позиция заставляет новенького задуматься.")
    print("Он решает отступить, не желая вступать в драку.")
    print("Однако в будущем могут возникнуть сложности с другими одноклассниками после уроков.")

def make_friends():
    print("Ваше предложение помощи в чем-то вызывает у одноклассника удивление.")
    print("Он соглашается, и вы начинаете общаться.")
    print("Вы смогли подружиться и даже получить поддержку от некоторых одноклассников.")

if __name__ == "__main__":
    start_quest()
class Character:
    def __init__(self):
        self.respect = 0
        self.loneliness = 0
        self.conflict_with_classmate = False
        self.conflict_resolution = False
        self.romantic_interest = False
        self.relationship_status = "Single"

def start_quest(character):
    print("Добро пожаловать в квест 'Новенький в школе'!")
    print("Вы - новенький в школе и сегодня ваш первый день. Вы входите в класс и видите неочень приятного нового одноклассника, который подходит к вам.")

    print("\nВыберите действие:")
    print("1. Попытаться уйти мирным путем")
    print("2. Сказать что-то смешное, чтобы разрядить обстановку")
    print("3. Встать в защитную позицию и сказать, чтобы он не приближался")
    print("4. Попробовать подружиться, предложив помощь в чем-то")

    user_choice = input("Ваш выбор (1-4): ")

    if user_choice == "1":
        peaceful_resolution(character)
    elif user_choice == "2":
        funny_comment(character)
    elif user_choice == "3":
        defend_yourself(character)
    elif user_choice == "4":
        make_friends(character)

def peaceful_resolution(character):
    print("\nВы пытаетесь уйти мирным путем, избегая конфликта.")
    character.respect += 1
    after_school(character)

def funny_comment(character):
    print("\nВы говорите что-то смешное, пытаясь разрядить обстановку.")
    character.respect += 2
    after_school(character)

def defend_yourself(character):
    print("\nВы встаете в защитную позицию и говорите, чтобы он не приближался.")
    character.respect += 1
    character.conflict_with_classmate = True
    after_school(character)

def make_friends(character):
    print("\nВы предлагаете помощь в чем-то, пытаясь подружиться.")
    character.respect += 3
    after_school(character)

def after_school(character):
    print("\nПосле уроков у вас есть несколько вариантов действий.")
    print("Выберите, как вы хотите провести время:")
    print("1. Присоединиться к группе детей, занимающихся каким-то видом активности")
    print("2. Пойти в библиотеку и почитать книгу")
    print("3. Просто прогуляться по школьному двору")
    print("4. Проигнорировать всех и отправиться домой")

    user_choice = input("Ваш выбор (1-4): ")

    if user_choice == "1":
        join_activity(character)
    elif user_choice == "2":
        read_book(character)
    elif user_choice == "3":
        take_a_walk(character)
    elif user_choice == "4":
        ignore_everyone(character)

def join_activity(character):
    print("\nВы присоединились к группе, занимающейся активностью.")
    character.respect += 2
    on_the_way_home(character)

def read_book(character):
    print("\nВ библиотеке вы нашли интересную книгу и провели время с пользой.")
    character.respect += 1
    on_the_way_home(character)

def take_a_walk(character):
    print("\nПрогулка по школьному двору позволила вам расслабиться и насладиться свежим воздухом.")
    character.respect += 1
    on_the_way_home(character)

def ignore_everyone(character):
    print("\nВы решили проигнорировать всех и отправиться домой.")
    character.loneliness += 1
    on_the_way_home(character)

def on_the_way_home(character):
    print("\nПо пути домой вы встречаете одноклассника, с которым ранее были проблемы.")
    print("Выберите, как вы хотите поступить:")
    print("1. Проигнорировать его и идти дальше")
    print("2. Попытаться поговорить и разрешить конфликт")
    print("3. Подарить ему что-то, чтобы попытаться помириться")

    user_choice = input("Ваш выбор (1-3): ")

    if user_choice == "1":
        print("Вы проигнорировали его и пошли дальше.")
    elif user_choice == "2":
        resolve_conflict(character)
    elif user_choice == "3":
        make_peace_with_gift(character)

    love_story(character)

def resolve_conflict(character):
    print("\nВы решаете поговорить и разрешить конфликт.")
    character.conflict_resolution = True

def make_peace_with_gift(character):
    print("\nВы решаете подарить ему что-то, чтобы попытаться помириться.")
    character.respect += 2
    character.conflict_resolution = True
def love_story(character):
    print("\nТакже вы замечаете новенькую девушку в школе, которая привлекла ваше внимание.")
    print("Выберите, как вы хотите развивать отношения с ней:")
    print("1. Попробовать завести дружбу")
    print("2. Проявить романтический интерес")
    print("3. Сконцентрироваться на учебе и не заводить отношений")

    user_choice = input("Ваш выбор (1-3): ")

    if user_choice == "1":
        make_friendship(character)
    elif user_choice == "2":
        express_romantic_interest(character)
    elif user_choice == "3":
        focus_on_studies(character)

def make_friendship(character):
    print("\nВы пытаетесь завести дружбу с новенькой девушкой.")
    character.respect += 2
    character.romantic_interest = True
    character.relationship_status = "Friendship"

def express_romantic_interest(character):
    print("\nВы проявляете романтический интерес к новенькой девушке.")
    character.respect += 3
    character.romantic_interest = True
    character.relationship_status = "In a Relationship"

def focus_on_studies(character):
    print("\nВы решаете сконцентрироваться на учебе и не заводить отношений.")
    character.loneliness += 1
    character.romantic_interest = False
    character.relationship_status = "Single"

if __name__ == "__main__":
    player = Character()
    start_quest(player)