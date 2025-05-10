from Get_Exercise_NLQ import GetExercise

def main():

    get_exercise_obj = GetExercise()
    get_exercise_obj.get_exercise_nlq()
    get_exercise_obj.saving_data_in_googlesheet()



if __name__ == "__main__":
    main()
