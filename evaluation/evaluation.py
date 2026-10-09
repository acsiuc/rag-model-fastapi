import json

from rag_model_fastapi.database import get_connection
from rag_model_fastapi.paths import eval_path
from rag_model_fastapi.retrieval.retrieval import retrieve


def evaluation():

    connection = get_connection()

    with open(eval_path) as f:
        questions_with_answer = json.load(f)

    correct_answers = 0
    missed_questions = []

    for dictionary in questions_with_answer: 
        question_got_wrong = {}
        file_paths = []
        content_file_path = retrieve(connection, dictionary['question'], 8)

        for content, file_path, distance in content_file_path:
            file_paths.append(file_path)

        if dictionary['eval_file_path'] in file_paths:
            correct_answers+=1
        else:
            question_got_wrong['question'] = (dictionary['question'])
            question_got_wrong['paths_retrieved'] = file_paths
            missed_questions.append(question_got_wrong)


    connection.close()

    return f'{correct_answers} / {len(questions_with_answer)}\nWrong answer for questions: {missed_questions}'


if __name__ == "__main__":
    print(evaluation())


            

    