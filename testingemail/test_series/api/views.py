from django.shortcuts import render
from ..models import PsychometricTest1, PsychometricQuestionSet1, PsychometricTestResult1, \
    PsychometricProfile, PsychometricTest2, PsychometricQuestionSet2, PsychometricTestResult2, PsychometricTest3, \
    PsychometricQuestionSet3, PsychometricTestResult3, PsychometricTest4, PsychometricQuestionSet4, \
    PsychometricTestResult4, PsychometricTest5, PsychometricQuestionSet5, PsychometricTestResult5, PsychometricTest6, \
    PsychometricQuestionSet6, PsychometricTestResult6, DataBaseDataAnalystProfile, VerbalAbilityTest1, \
    VerbalAbilityQuestionSet1, VerbalAbilityTestResult1, VerbalAbilityTest2, VerbalAbilityTestResult2, \
    VerbalAbilityQuestionSet2, NumericalAbilityTestResult, NumericalAbilityTest, NumericalQuestionSet, \
    ClosureAbilityTestResult, ClosureAbilityTest, ClosureQuestionSet, SpatialQuestionSet, SpatialAbilityTest, \
    SpatialAbilityTestResult, MechanicalQuestionSet, MechanicalAbilityTest, MechanicalAbilityTestResult, \
    ClericalQuestionSet, ClericalAbilityTest, ClericalAbilityTestResult, ReasoningQuestionSet, ReasoningAbilityTest, \
    ReasoningAbilityTestResult, Question

from rest_framework import status
from .serializers import VerbalQuestion1Serializer, VerbalQuestion2Serializer, \
    NumericalQuestionSetSerializer, ClericalQuestionSetSerializer, ReasoningQuestionSetSerializer, \
    SpatialQuestionSetSetSerializer, MechanicalQuestionSetSerializer, ClosureQuestionSetSerializer

# from accounts.models import User
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from django.db.models import Count


# ============================================ Psychometric Test api================================
@permission_classes((permissions.AllowAny,))
class PsychometricTestView(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        psychometric_test = request.GET.get('test')
        if psychometric_test == '1':
            user_id = request.data.get('user_id')
            user = User.objects.filter(id=user_id)[0]

            data = request.data.get('data')

            for data1 in data:
                print(data1)
                psychometic_test1 = PsychometricTest1()
                psychometic_test1.user = user
                psychometic_test1.question = PsychometricQuestionSet1.objects.get(id=data1['q_id'])
                psychometic_test1.selected_option = data1['select_option']
                if data1['select_option'] == 'a':
                    psychometic_test1.answer = data1['select_option']
                    psychometic_test1.score = 2

                elif data1['select_option'] == 'b':
                    psychometic_test1.answer = data1['select_option']
                    psychometic_test1.score = 1
                elif data1['select_option'] == 'c':
                    psychometic_test1.answer = data1['select_option']
                    psychometic_test1.score = 0
                else:
                    pass

                psychometic_test1.save()

            a_count = PsychometricTest1.objects.filter(user=user, selected_option='a').count()

            b_count = PsychometricTest1.objects.filter(user=user, selected_option='b').count()
            c_count = PsychometricTest1.objects.filter(user=user, selected_option='c').count()
            total_score_test_series = a_count * 2 + b_count * 1 + c_count * 0
            print('total_score_test_series', total_score_test_series)
            psychometric_test_result = PsychometricTestResult1()

            psychometric_test_result.user = user
            psychometric_test_result.total_score = total_score_test_series
            psychometric_test_result.save()
            psychometric_test_result.test.set(PsychometricTest1.objects.filter(user=user))
            psychometric_test_result.save()

            user_profile = PsychometricProfile()

            user_profile.user = user

            user_profile.test_result_1 = psychometric_test_result
            user_profile.save()
            response_payload = {
                'is_authenticated': True,
                'status': True,
                'messages': [],
                'result': "test series one completed ",
                'additional_data': {}

            }
            return Response(response_payload)
        elif psychometric_test == '2':
            user_id = request.data.get('user_id')
            user = User.objects.filter(id=user_id)[0]

            data = request.data.get('data')

            for data1 in data:
                print(data1)
                psychometic_test = PsychometricTest2()
                psychometic_test.user = user
                psychometic_test.question = PsychometricQuestionSet2.objects.get(id=data1['q_id'])
                psychometic_test.selected_option = data1['select_option']
                if data1['select_option'] == 'a':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 2

                elif data1['select_option'] == 'b':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 1
                elif data1['select_option'] == 'c':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 0
                else:
                    pass

                psychometic_test.save()

            a_count = PsychometricTest2.objects.filter(user=user, selected_option='a').count()

            b_count = PsychometricTest2.objects.filter(user=user, selected_option='b').count()
            c_count = PsychometricTest2.objects.filter(user=user, selected_option='c').count()
            total_score_test_series = a_count * 2 + b_count * 1 + c_count * 0
            print('total_score_test_series', total_score_test_series)
            psychometric_test_result = PsychometricTestResult2()

            psychometric_test_result.user = user
            psychometric_test_result.total_score = total_score_test_series
            psychometric_test_result.save()
            psychometric_test_result.test.set(PsychometricTest2.objects.filter(user=user))
            psychometric_test_result.save()

            user_profile = PsychometricProfile()

            user_profile.user = user

            user_profile.test_result_2 = psychometric_test_result
            user_profile.save()
            response_payload = {
                'is_authenticated': True,
                'status': True,
                'messages': [],
                'result': "test series two end",
                'additional_data': {}

            }
            return Response(response_payload)
        elif psychometric_test == '3':
            user_id = request.data.get('user_id')
            user = User.objects.filter(id=user_id)[0]

            data = request.data.get('data')

            for data1 in data:
                print(data1)
                psychometic_test = PsychometricTest3()
                psychometic_test.user = user
                psychometic_test.question = PsychometricQuestionSet3.objects.get(id=data1['q_id'])
                psychometic_test.selected_option = data1['select_option']
                if data1['select_option'] == 'a':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 2

                elif data1['select_option'] == 'b':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 1
                elif data1['select_option'] == 'c':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 0
                else:
                    pass

                psychometic_test.save()

            a_count = PsychometricTest3.objects.filter(user=user, selected_option='a').count()

            b_count = PsychometricTest3.objects.filter(user=user, selected_option='b').count()
            c_count = PsychometricTest3.objects.filter(user=user, selected_option='c').count()
            total_score_test_series = a_count * 2 + b_count * 1 + c_count * 0
            print('total_score_test_series', total_score_test_series)
            psychometric_test_result = PsychometricTestResult3()

            psychometric_test_result.user = user
            psychometric_test_result.total_score = total_score_test_series
            psychometric_test_result.save()
            psychometric_test_result.test.set(PsychometricTest3.objects.filter(user=user))
            psychometric_test_result.save()

            user_profile = PsychometricProfile.objects.filter(user=user)[0]

            user_profile.user = user

            user_profile.test_result_3 = psychometric_test_result
            user_profile.save()
            response_payload = {
                'is_authenticated': True,
                'status': True,
                'messages': [],
                'result': "test series three completed",
                'additional_data': {}

            }
            return Response(response_payload)
        elif psychometric_test == '4':
            user_id = request.data.get('user_id')
            user = User.objects.filter(id=user_id)[0]

            data = request.data.get('data')

            for data1 in data:
                print(data1)
                psychometic_test = PsychometricTest4()
                psychometic_test.user = user
                psychometic_test.question = PsychometricQuestionSet4.objects.get(id=data1['q_id'])
                psychometic_test.selected_option = data1['select_option']
                if data1['select_option'] == 'a':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 2

                elif data1['select_option'] == 'b':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 1
                elif data1['select_option'] == 'c':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 0
                else:
                    pass

                psychometic_test.save()

            a_count = PsychometricTest4.objects.filter(user=user, selected_option='a').count()

            b_count = PsychometricTest4.objects.filter(user=user, selected_option='b').count()
            c_count = PsychometricTest4.objects.filter(user=user, selected_option='c').count()
            total_score_test_series = a_count * 2 + b_count * 1 + c_count * 0
            print('total_score_test_series', total_score_test_series)
            psychometric_test_result = PsychometricTestResult4()

            psychometric_test_result.user = user
            psychometric_test_result.total_score = total_score_test_series
            psychometric_test_result.save()
            psychometric_test_result.test.set(PsychometricTest4.objects.filter(user=user))
            psychometric_test_result.save()

            user_profile = PsychometricProfile.objects.filter(user=user)[0]

            user_profile.user = user

            user_profile.test_result_4 = psychometric_test_result
            user_profile.save()
            response_payload = {
                'is_authenticated': True,
                'status': True,
                'messages': [],
                'result': "test series four completed",
                'additional_data': {}

            }
            return Response(response_payload)
        elif psychometric_test == '5':
            user_id = request.data.get('user_id')
            user = User.objects.filter(id=user_id)[0]

            data = request.data.get('data')

            for data1 in data:
                print(data1)
                psychometic_test = PsychometricTest5()
                psychometic_test.user = user
                psychometic_test.question = PsychometricQuestionSet5.objects.get(id=data1['q_id'])
                psychometic_test.selected_option = data1['select_option']
                if data1['select_option'] == 'a':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 2

                elif data1['select_option'] == 'b':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 1
                elif data1['select_option'] == 'c':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 0
                else:
                    pass

                psychometic_test.save()

            a_count = PsychometricTest5.objects.filter(user=user, selected_option='a').count()

            b_count = PsychometricTest5.objects.filter(user=user, selected_option='b').count()
            c_count = PsychometricTest5.objects.filter(user=user, selected_option='c').count()
            total_score_test_series = a_count * 2 + b_count * 1 + c_count * 0
            print('total_score_test_series', total_score_test_series)
            psychometric_test_result = PsychometricTestResult5()

            psychometric_test_result.user = user
            psychometric_test_result.total_score = total_score_test_series
            psychometric_test_result.save()
            psychometric_test_result.test.set(PsychometricTest5.objects.filter(user=user))
            psychometric_test_result.save()

            user_profile = PsychometricProfile.objects.filter(user=user)[0]

            user_profile.user = user

            user_profile.test_result_5 = psychometric_test_result
            user_profile.save()
            response_payload = {
                'is_authenticated': True,
                'status': True,
                'messages': [],
                'result': "test series five completed",
                'additional_data': {}

            }
            return Response(response_payload)
        elif psychometric_test == '6':
            user_id = request.data.get('user_id')
            user = User.objects.filter(id=user_id)[0]

            data = request.data.get('data')

            for data1 in data:
                print(data1)
                psychometic_test = PsychometricTest6()
                psychometic_test.user = user
                psychometic_test.question = PsychometricQuestionSet6.objects.get(id=data1['q_id'])
                psychometic_test.selected_option = data1['select_option']
                if data1['select_option'] == 'a':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 2

                elif data1['select_option'] == 'b':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 1
                elif data1['select_option'] == 'c':
                    psychometic_test.answer = data1['select_option']
                    psychometic_test.score = 0
                else:
                    pass

                psychometic_test.save()

            a_count = PsychometricTest6.objects.filter(user=user, selected_option='a').count()

            b_count = PsychometricTest6.objects.filter(user=user, selected_option='b').count()
            c_count = PsychometricTest6.objects.filter(user=user, selected_option='c').count()
            total_score_test_series = a_count * 2 + b_count * 1 + c_count * 0
            print('total_score_test_series', total_score_test_series)
            psychometric_test_result = PsychometricTestResult6()

            psychometric_test_result.user = user
            psychometric_test_result.total_score = total_score_test_series
            psychometric_test_result.save()
            psychometric_test_result.test.set(PsychometricTest6.objects.filter(user=user))
            psychometric_test_result.save()

            user_profile = PsychometricProfile.objects.filter(user=user)[0]

            user_profile.user = user

            user_profile.test_result_6 = psychometric_test_result
            user_profile.save()
            response_payload = {
                'is_authenticated': True,
                'status': True,
                'messages': [],
                'result': "test series six completed",
                'additional_data': {}

            }
            return Response(response_payload)
        else:
            return Response({'response': 'no data found'})

    def list(self, request):
        test_list = request.GET.get('Test_list')
        if test_list == '1':
            user_id = request.data.get('user_id')
            user = User.objects.get(id=user_id)

            psychometric_test1_result = PsychometricTestResult1.objects.filter(user=user)[0]
            psychometric_test1_result = [{
                'user': user_id,
                'total_score': psychometric_test1_result.total_score,
            }]

            return Response({'response': psychometric_test1_result})


# =========================================================================DBDA=======================================
@permission_classes((permissions.AllowAny,))
class DBDATestView(viewsets.ViewSet):
    def get(self, request):
        query_set = request.GET.get('question')
        if query_set == '1':
            queryset = VerbalAbilityQuestionSet1.objects.all()
            serializer_data = VerbalQuestion1Serializer(queryset, many=True)
            return Response({'response': serializer_data.data})

        elif query_set == '2':
            queryset = VerbalAbilityQuestionSet2.objects.all()
            serializer_data = VerbalQuestion2Serializer(queryset, many=True)

            return Response({'response': serializer_data.data})

        elif query_set == '3':
            query_set = NumericalQuestionSet.objects.all()
            serializer = NumericalQuestionSetSerializer(query_set, many=True)
            return Response({'response': serializer.data})
        elif query_set == '4':
            query_set = ClericalQuestionSet.objects.all()
            serializer = ClericalQuestionSetSerializer(query_set, many=True)
            return Response({'response': serializer.data})
        elif query_set == '5':
            query_set = ReasoningQuestionSet.objects.all()
            serializer = ReasoningQuestionSetSerializer(query_set, many=True)
            return Response({'response': serializer.data})
        elif query_set == '6':
            query_set = SpatialQuestionSet.objects.all()
            serializer = SpatialQuestionSetSetSerializer(query_set, many=True)
            return Response({'response': serializer.data})
        elif query_set == '7':
            query_set = MechanicalQuestionSet.objects.all()
            serializer = MechanicalQuestionSetSerializer(query_set, many=True)
            return Response({'response': serializer.data})
        elif query_set == '8':
            query_set = ClosureQuestionSet.objects.all()
            serializer = ClosureQuestionSetSerializer(query_set, many=True)
            return Response({'response': serializer.data})

        else:
            return Response({'response': "saved data"})

    def create(self, request):
        test_quesry_set = request.GET.get('test')

        if test_quesry_set == '1':
            data = request.data.get('data')
            user = User.objects.get(id=request.data.get('user_id'))
            user_exist = VerbalAbilityTest1.objects.filter(user=user).exists()
            if not user_exist:
                for data1 in data:
                    print(data1['q_id'], data1['select_option'])
                    verbal_ability = VerbalAbilityTest1()
                    verbal_ability.user = user
                    verbal_ability.question = VerbalAbilityQuestionSet1.objects.get(id=data1['q_id'])
                    verbal_ability.select_option = data1['select_option']
                    if data1['q_id'] == '11' and data1['select_option'] == 'old':
                        verbal_ability.score = '2'
                    elif data1['q_id'] == '12' and data1['select_option'] == 'blunder':
                        verbal_ability.score = '2'
                    elif data1['q_id'] == '13' and data1['select_option'] == 'waste':
                        verbal_ability.score = '2'


                    else:
                        pass
                    verbal_ability.save()

                totol_score_count = VerbalAbilityTest1.objects.filter(user=user)
                totol_marks = 0
                for totol_score_count in totol_score_count:
                    total_score = totol_score_count.score if totol_score_count.score is not None else 0

                    totol_marks += total_score
                verbal_ability_test_result = VerbalAbilityTestResult1()

                verbal_ability_test_result.user = user

                verbal_ability_test_result.total_score = totol_marks
                verbal_ability_test_result.save()
                verbal_ability_test_result.test.set(VerbalAbilityTest1.objects.filter(user=user))
                verbal_ability_test_result.save()

                data_base_data_analysis_user_profile, created = DataBaseDataAnalystProfile.objects.get_or_create(
                    user=user)
                data_base_data_analysis_user_profile.user = user
                data_base_data_analysis_user_profile.verbal_ability_1_score = totol_marks
                data_base_data_analysis_user_profile.total_score_of_all_test += totol_marks
                data_base_data_analysis_user_profile.verbal_ability_1 = verbal_ability_test_result
                data_base_data_analysis_user_profile.save()

                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "verbal task 1 is completed",
                    'additional_data': {}

                }
                return Response(response_payload)
            else:
                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "task is already completed",
                    'additional_data': {}

                }
                return Response(response_payload)

        elif test_quesry_set == '2':
            data = request.data.get('data')
            user = User.objects.get(id=request.data.get('user_id'))
            user_exist = VerbalAbilityTest2.objects.filter(user=user).exists()
            if not user_exist:
                for data1 in data:
                    print(data1['q_id'], data1['select_option'])
                    verbal_ability = VerbalAbilityTest2()
                    verbal_ability.user = user
                    verbal_ability.question = VerbalAbilityQuestionSet2.objects.get(id=data1['q_id'])
                    verbal_ability.select_option = data1['select_option']
                    if data1['q_id'] == '1' and data1['select_option'] == 'old at tha time':
                        verbal_ability.score = '2'
                    elif data1['q_id'] == '2' and data1['select_option'] == 'cloud morning':
                        verbal_ability.score = '2'
                    elif data1['q_id'] == '3' and data1['select_option'] == 'do not keep':
                        verbal_ability.score = '2'


                    else:
                        pass
                    verbal_ability.save()

                totol_score_count = VerbalAbilityTest2.objects.filter(user=user)
                totol_marks = 0
                for totol_score_count in totol_score_count:
                    total_score = totol_score_count.score if totol_score_count.score is not None else 0

                    totol_marks += total_score
                verbal_ability_test_result = VerbalAbilityTestResult2()

                verbal_ability_test_result.user = user

                verbal_ability_test_result.total_score = totol_marks
                verbal_ability_test_result.save()
                verbal_ability_test_result.test.set(VerbalAbilityTest2.objects.filter(user=user))
                verbal_ability_test_result.save()

                data_base_data_analysis_user_profile, created = DataBaseDataAnalystProfile.objects.get_or_create(
                    user=user)
                data_base_data_analysis_user_profile.user = user
                data_base_data_analysis_user_profile.verbal_ability_2_score = totol_marks
                data_base_data_analysis_user_profile.total_score_of_all_test += totol_marks
                data_base_data_analysis_user_profile.verbal_ability_2 = verbal_ability_test_result
                data_base_data_analysis_user_profile.save()

                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "verbal task 2 is completed",
                    'additional_data': {}

                }
                return Response(response_payload)
            else:
                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "task is already completed",
                    'additional_data': {}

                }
                return Response(response_payload)
        elif test_quesry_set == '3':
            data = request.data.get('data')
            user = User.objects.get(id=request.data.get('user_id'))
            user_exist = NumericalAbilityTest.objects.filter(user=user).exists()
            if not user_exist:
                for data1 in data:
                    print(data1['q_id'], data1['select_option'])
                    numerical_ability = NumericalAbilityTest()
                    numerical_ability.user = user
                    numerical_ability.question = NumericalQuestionSet.objects.get(id=data1['q_id'])
                    numerical_ability.select_option = data1['select_option']
                    if data1['q_id'] == '1' and data1['select_option'] == '220':
                        numerical_ability.score = '2'
                    elif data1['q_id'] == '2' and data1['select_option'] == '532':
                        numerical_ability.score = '2'
                    elif data1['q_id'] == '3' and data1['select_option'] == '2822':
                        numerical_ability.score = '2'


                    else:
                        pass
                    numerical_ability.save()

                totol_score_count = NumericalAbilityTest.objects.filter(user=user)
                totol_marks = 0
                for totol_score_count in totol_score_count:
                    total_score = totol_score_count.score if totol_score_count.score is not None else 0

                    totol_marks += total_score
                numerical_ability_test_result = NumericalAbilityTestResult()

                numerical_ability_test_result.user = user

                numerical_ability_test_result.total_score = totol_marks
                numerical_ability_test_result.save()
                numerical_ability_test_result.test.set(NumericalAbilityTest.objects.filter(user=user))
                numerical_ability_test_result.save()

                data_base_data_analysis_user_profile, created = DataBaseDataAnalystProfile.objects.get_or_create(
                    user=user)
                data_base_data_analysis_user_profile.user = user
                data_base_data_analysis_user_profile.numerical_ability_score = totol_marks
                data_base_data_analysis_user_profile.total_score_of_all_test += totol_marks
                data_base_data_analysis_user_profile.numerical_ability = numerical_ability_test_result
                data_base_data_analysis_user_profile.save()

                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "numerical task is completed",
                    'additional_data': {}

                }
                return Response(response_payload)
            else:
                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "task is already completed",
                    'additional_data': {}

                }
                return Response(response_payload)

        elif test_quesry_set == '4':
            data = request.data.get('data')
            user = User.objects.get(id=request.data.get('user_id'))
            user_exist = ReasoningAbilityTest.objects.filter(user=user).exists()
            if not user_exist:
                for data1 in data:
                    print(data1['q_id'], data1['select_option'])
                    reasoning_ability = ReasoningAbilityTest()
                    reasoning_ability.user = user
                    reasoning_ability.question = ReasoningQuestionSet.objects.get(id=data1['q_id'])
                    reasoning_ability.select_option = data1['select_option']
                    if data1['q_id'] == '1' and data1['select_option'] == 'DEPD':
                        reasoning_ability.score = '2'
                    elif data1['q_id'] == '2' and data1['select_option'] == 'BLMB':
                        reasoning_ability.score = '2'
                    elif data1['q_id'] == '3' and data1['select_option'] == 'NLPQ':
                        reasoning_ability.score = '2'


                    else:
                        pass
                    reasoning_ability.save()

                totol_score_count = ReasoningAbilityTest.objects.filter(user=user)
                totol_marks = 0
                for totol_score_count in totol_score_count:
                    total_score = totol_score_count.score if totol_score_count.score is not None else 0

                    totol_marks += total_score
                reasoning_ability_test_result = ReasoningAbilityTestResult()

                reasoning_ability_test_result.user = user

                reasoning_ability_test_result.total_score = totol_marks
                reasoning_ability_test_result.save()
                reasoning_ability_test_result.test.set(ReasoningAbilityTest.objects.filter(user=user))
                reasoning_ability_test_result.save()

                data_base_data_analysis_user_profile, created = DataBaseDataAnalystProfile.objects.get_or_create(
                    user=user)
                data_base_data_analysis_user_profile.user = user
                data_base_data_analysis_user_profile.reasoning_ability_score = totol_marks
                data_base_data_analysis_user_profile.total_score_of_all_test += totol_marks
                data_base_data_analysis_user_profile.reasoning_ability = reasoning_ability_test_result
                data_base_data_analysis_user_profile.save()

                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "reasoning task is completed",
                    'additional_data': {}

                }
                return Response(response_payload)

        elif test_quesry_set == '5':
            data = request.data.get('data')
            user = User.objects.get(id=request.data.get('user_id'))
            user_exist = ClericalAbilityTest.objects.filter(user=user).exists()
            if not user_exist:
                for data1 in data:
                    print(data1['q_id'], data1['select_option'])
                    clerical_ability = ClericalAbilityTest()
                    clerical_ability.user = user
                    clerical_ability.question = ClericalQuestionSet.objects.get(id=data1['q_id'])
                    clerical_ability.select_option = data1['select_option']
                    if data1['q_id'] == '11' and data1['select_option'] == 'different':
                        clerical_ability.score = '2'
                    elif data1['q_id'] == '12' and data1['select_option'] == 'same':
                        clerical_ability.score = '2'
                    elif data1['q_id'] == '13' and data1['select_option'] == 'same':
                        clerical_ability.score = '2'
                    elif data1['q_id'] == '14' and data1['select_option'] == 'different':
                        clerical_ability.score = '2'


                    else:
                        pass
                    clerical_ability.save()

                totol_score_count = ClericalAbilityTest.objects.filter(user=user)
                totol_marks = 0
                for totol_score_count in totol_score_count:
                    total_score = totol_score_count.score if totol_score_count.score is not None else 0

                    totol_marks += total_score
                clerical_ability_test_result = ClericalAbilityTestResult()

                clerical_ability_test_result.user = user

                clerical_ability_test_result.total_score = totol_marks
                clerical_ability_test_result.save()
                clerical_ability_test_result.test.set(ClericalAbilityTest.objects.filter(user=user))
                clerical_ability_test_result.save()

                data_base_data_analysis_user_profile, created = DataBaseDataAnalystProfile.objects.get_or_create(
                    user=user)
                data_base_data_analysis_user_profile.user = user
                data_base_data_analysis_user_profile.clerical_ability_score = totol_marks
                data_base_data_analysis_user_profile.total_score_of_all_test += totol_marks
                data_base_data_analysis_user_profile.clerical_ability = clerical_ability_test_result
                data_base_data_analysis_user_profile.save()

                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "clerical task is completed",
                    'additional_data': {}

                }
                return Response(response_payload)


            else:
                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "task is already completed",
                    'additional_data': {}

                }
                return Response(response_payload)

        elif test_quesry_set == '6':
            data = request.data.get('data')
            user = User.objects.get(id=request.data.get('user_id'))
            user_exist = SpatialAbilityTest.objects.filter(user=user).exists()
            if not user_exist:
                for data1 in data:
                    print(data1['q_id'], data1['select_option'])
                    spatial_ability = SpatialAbilityTest()
                    spatial_ability.user = user
                    spatial_ability.question = SpatialQuestionSet.objects.get(id=data1['q_id'])
                    spatial_ability.select_option = data1['select_option']
                    if data1['q_id'] == '1' and data1['select_option'] == 'different':
                        spatial_ability.score = '2'
                    elif data1['q_id'] == '2' and data1['select_option'] == 'same':
                        spatial_ability.score = '2'
                    elif data1['q_id'] == '3' and data1['select_option'] == 'same':
                        spatial_ability.score = '2'
                    elif data1['q_id'] == '4' and data1['select_option'] == 'different':
                        spatial_ability.score = '2'
                    elif data1['q_id'] == '5' and data1['select_option'] == 'different':
                        spatial_ability.score = '2'
                    elif data1['q_id'] == '6' and data1['select_option'] == 'same':
                        spatial_ability.score = '2'
                    elif data1['q_id'] == '7' and data1['select_option'] == 'same':
                        spatial_ability.score = '2'
                    elif data1['q_id'] == '8' and data1['select_option'] == 'different':
                        spatial_ability.score = '2'
                    elif data1['q_id'] == '9' and data1['select_option'] == 'same':
                        spatial_ability.score = '2'
                    elif data1['q_id'] == '10' and data1['select_option'] == 'different':
                        spatial_ability.score = '2'
                    else:
                        pass
                    spatial_ability.save()

                totol_score_count = SpatialAbilityTest.objects.filter(user=user)
                totol_marks = 0
                for totol_score_count in totol_score_count:
                    total_score = totol_score_count.score if totol_score_count.score is not None else 0

                    totol_marks += total_score
                spatial_ability_test_result = SpatialAbilityTestResult()

                spatial_ability_test_result.user = user

                spatial_ability_test_result.total_score = totol_marks
                spatial_ability_test_result.save()
                spatial_ability_test_result.test.set(SpatialAbilityTest.objects.filter(user=user))
                spatial_ability_test_result.save()

                data_base_data_analysis_user_profile, created = DataBaseDataAnalystProfile.objects.get_or_create(
                    user=user)
                data_base_data_analysis_user_profile.user = user
                data_base_data_analysis_user_profile.spatial_ability_score = totol_marks
                data_base_data_analysis_user_profile.total_score_of_all_test += totol_marks
                data_base_data_analysis_user_profile.spatial_ability = spatial_ability_test_result
                data_base_data_analysis_user_profile.save()

                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "spatial task is completed",
                    'additional_data': {}

                }
                return Response(response_payload)
            else:
                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "task is already completed",
                    'additional_data': {}

                }
                return Response(response_payload)
        elif test_quesry_set == '7':
            data = request.data.get('data')
            user = User.objects.get(id=request.data.get('user_id'))
            user_exist = MechanicalAbilityTest.objects.filter(user=user).exists()
            if not user_exist:
                for data1 in data:
                    print(data1['q_id'], data1['select_option'])
                    mechanical_ability = MechanicalAbilityTest()
                    mechanical_ability.user = user
                    mechanical_ability.question = MechanicalQuestionSet.objects.get(id=data1['q_id'])
                    mechanical_ability.select_option = data1['select_option']
                    if data1['q_id'] == '1' and data1['select_option'] == 'wood':
                        mechanical_ability.score = '2'
                    elif data1['q_id'] == '2' and data1['select_option'] == 'c':
                        mechanical_ability.score = '2'
                    elif data1['q_id'] == '3' and data1['select_option'] == '50':
                        mechanical_ability.score = '2'

                    else:
                        pass
                    mechanical_ability.save()

                totol_score_count = MechanicalAbilityTest.objects.filter(user=user)
                totol_marks = 0
                for totol_score_count in totol_score_count:
                    total_score = totol_score_count.score if totol_score_count.score is not None else 0

                    totol_marks += total_score
                mechanical_ability_test_result = MechanicalAbilityTestResult()

                mechanical_ability_test_result.user = user

                mechanical_ability_test_result.total_score = totol_marks
                mechanical_ability_test_result.save()
                mechanical_ability_test_result.test.set(MechanicalAbilityTest.objects.filter(user=user))
                mechanical_ability_test_result.save()

                data_base_data_analysis_user_profile, created = DataBaseDataAnalystProfile.objects.get_or_create(
                    user=user)
                data_base_data_analysis_user_profile.user = user
                data_base_data_analysis_user_profile.mechanical_ability_score = totol_marks
                data_base_data_analysis_user_profile.total_score_of_all_test += totol_marks
                data_base_data_analysis_user_profile.mechanical_ability = mechanical_ability_test_result
                data_base_data_analysis_user_profile.save()

                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "mechanical task is completed",
                    'additional_data': {}

                }
                return Response(response_payload)
            else:
                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "task is already completed",
                    'additional_data': {}

                }
                return Response(response_payload)
        elif test_quesry_set == '8':
            data = request.data.get('data')
            user = User.objects.get(id=request.data.get('user_id'))
            user_exist = ClosureAbilityTest.objects.filter(user=user).exists()
            if not user_exist:
                for data1 in data:
                    print(data1['q_id'], data1['select_option'])
                    closure_ability = ClosureAbilityTest()
                    closure_ability.user = user
                    closure_ability.question = ClosureQuestionSet.objects.get(id=data1['q_id'])
                    closure_ability.select_option = data1['select_option']
                    if data1['q_id'] == '1' and data1['select_option'] == 'dderla':
                        closure_ability.score = '2'
                    elif data1['q_id'] == '2' and data1['select_option'] == 'joyen':
                        closure_ability.score = '2'
                    elif data1['q_id'] == '3' and data1['select_option'] == 'lows':
                        closure_ability.score = '2'

                    else:
                        pass
                    closure_ability.save()

                totol_score_count = ClosureAbilityTest.objects.filter(user=user)
                totol_marks = 0
                for totol_score_count in totol_score_count:
                    total_score = totol_score_count.score if totol_score_count.score is not None else 0

                    totol_marks += total_score
                closure_ability_test_result = ClosureAbilityTestResult()

                closure_ability_test_result.user = user

                closure_ability_test_result.total_score = totol_marks
                closure_ability_test_result.save()
                closure_ability_test_result.test.set(ClosureAbilityTest.objects.filter(user=user))
                closure_ability_test_result.save()

                data_base_data_analysis_user_profile, created = DataBaseDataAnalystProfile.objects.get_or_create(
                    user=user)
                data_base_data_analysis_user_profile.user = user
                data_base_data_analysis_user_profile.closure_ability_score = totol_marks
                data_base_data_analysis_user_profile.total_score_of_all_test += totol_marks
                data_base_data_analysis_user_profile.closure_ability = closure_ability_test_result
                data_base_data_analysis_user_profile.save()

                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "closure ability task is completed",
                    'additional_data': {}

                }
                return Response(response_payload)
            else:
                response_payload = {
                    'is_authenticated': True,
                    'status': True,
                    'messages': [],
                    'result': "task is already completed",
                    'additional_data': {}

                }
                return Response(response_payload)
        else:
            return Response({'response': 'query set does not exist '})


@permission_classes((permissions.AllowAny,))
class QuestionView(viewsets.ViewSet):

    def create(self, request):

        data = request.data.get('data')

        if data:
            for i in data:
                print(list(i.keys())[0])

                question = Question()
                question.question = list(i.keys())[0]
                question.question_type = list(i.values())[0]
                question.save()
        return Response({'response': 'save'})
