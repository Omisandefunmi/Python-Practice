import unittest

from . import questionnaire


class QuestionnaireTest(unittest.TestCase):
    questions = []

    def test_that_questionnaire_exists(self):
        myers_briggs = questionnaire.Questionnaire
        self.assertIsNotNone(myers_briggs)

    def test_that_questionnaire_can_load_questions(self):
        # q = Questionnaire()
        myers_briggs = questionnaire.Questionnaire()
        myers_briggs.load_questions('1 --> A: plan, schedule  B: unplanned, spontaneous')
        self.assertEqual(1, myers_briggs.check_number_of_questions())
        self.assertTrue(myers_briggs.number_of_questions == 1)

    def test_that_question_can_serve_questions(self):
        myers_briggs = questionnaire.Questionnaire()
        myers_briggs.load_questions('1 --> A: plan, schedule  B: unplanned, spontaneous')
        self.assertEqual("1 --> A: plan, schedule  B: unplanned, spontaneous", myers_briggs.serve_question(1))

    def test_that_question_can_collect_answers(self):
        myers_briggs = questionnaire.Questionnaire()
        myers_briggs.load_questions('1 --> A: plan, schedule  B: unplanned, spontaneous')
        myers_briggs.serve_question(1)
        myers_briggs.collect_answers('b')
        self.assertEqual(1, myers_briggs.check_number_of_answers())

    def test_that_question_can_mark_answers(self):
        myers_briggs = questionnaire.Questionnaire()

        myers_briggs.load_questions("1 --> A: Interpret literal B: Look for meaning and possibilities")
        myers_briggs.load_questions("2 --> A: Interpret literally  B: Look for meaning and possibilities")
        myers_briggs.load_questions("3 --> A: logical, thinking, questioning  B: empathetic, feeling, accommodating")
        myers_briggs.load_questions("4 --> A: organised, orderly  B: flexible, adaptable")
        myers_briggs.load_questions("5 --> A: more outgoing, think out loud  B: more reserved, think to yourself")
        myers_briggs.load_questions("6 --> A: practical, realistic, experiential  B: imaginative, innovative, theoretical")
        myers_briggs.load_questions("7 --> A: candid, straight forward, frank  B: tactful, kind, encouraging")
        myers_briggs.load_questions("8 --> A: plan, schedule  B: unplanned, spontaneous")

        myers_briggs.serve_question(1)
        myers_briggs.serve_question(2)
        myers_briggs.serve_question(3)
        myers_briggs.serve_question(4)
        myers_briggs.serve_question(5)
        myers_briggs.serve_question(6)
        myers_briggs.serve_question(7)
        myers_briggs.serve_question(8)

        
        self.assertEqual()

