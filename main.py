from utils import filter_chars, select_high_score
from auto_complete_run import RunAutoComp

if __name__ == '__main__':
    print("loading the files and preparing the system...")
    t = RunAutoComp("2021-archive")
    t.initialize()
    user_in = ''
    print("the system is ready. enter your text:")
    while True:
        get_from_user = input(f"{user_in}")
        user_in = user_in + filter_chars(get_from_user)
        best_sentence = select_high_score(t.completion(user_in))  # find completion and select highest from
        if get_from_user.find('#') == -1:
            print(f'Here are {len(best_sentence)} suggestions')
            for i in range(len(best_sentence)):
                print(f'{i + 1}. {best_sentence[i].get_sentence().strip()}',
                      "(" + best_sentence[i].get_src()[str(best_sentence[i].get_src()).rindex("/")+1:]+")")
        user_in = '' if get_from_user.find('#') != -1 else user_in
