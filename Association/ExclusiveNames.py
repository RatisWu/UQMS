SurveyUniqueName = "ExpParasSurvey"   # Generated by FBI, please do NOT change it.
ConfigUniqueName = "ExpConfigs"       # The folder contains hardware configs which you upload to server should have this keyword, like 'Test_ExpConfigs', 'My_QM_ExpConfigs', ...


if __name__ == "__main__":
    Correct_example = 'Test_ExpConfigs'
    print("Correct name: ",ConfigUniqueName.lower() in Correct_example.lower())
    Incorrect_example = 'Test_Exp_Config'
    print("Inorrect name: ",ConfigUniqueName.lower() in Incorrect_example.lower())