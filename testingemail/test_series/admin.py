from django.contrib import admin

# # Register your models here.
from .models import PsychometricProfile, PsychometricTestResult1, PsychometricTest1, \
    PsychometricQuestionSet1, PsychometricTestResult2, PsychometricTest2, PsychometricQuestionSet2, \
    PsychometricTestResult3, PsychometricTest3, PsychometricQuestionSet3, PsychometricTestResult4, PsychometricTest4, \
    PsychometricQuestionSet4, PsychometricTestResult5, PsychometricTest5, PsychometricQuestionSet5, \
    PsychometricTestResult6, PsychometricTest6, PsychometricQuestionSet6, DataBaseDataAnalystProfile, \
    VerbalAbilityTestResult1, VerbalAbilityTest1, VerbalAbilityQuestionSet1, VerbalAbilityTestResult2, \
    VerbalAbilityTest2, VerbalAbilityQuestionSet2, NumericalAbilityTestResult, NumericalAbilityTest, \
    NumericalQuestionSet, ClosureAbilityTestResult, ClosureAbilityTest, ClosureQuestionSet, SpatialQuestionSet, \
    SpatialAbilityTest, SpatialAbilityTestResult, MechanicalQuestionSet, MechanicalAbilityTest, \
    MechanicalAbilityTestResult, ClericalQuestionSet, ClericalAbilityTest, ClericalAbilityTestResult, \
    ReasoningQuestionSet, ReasoningAbilityTest, ReasoningAbilityTestResult, \
    ChoiceQuestionSet1, ChoiceQuestionSet2, ChoiceNumericalQuestionSet, ChoiceClosureQuestionSet, \
    ChoiceClericalQuestionSet, ChoiceReasoningQuestionSet, ChoiceSpatialQuestionSet, ChoiceMechanicalQuestionSet,Question


admin.site.register(PsychometricProfile)
admin.site.register(PsychometricTestResult1)
admin.site.register(PsychometricTest1)
admin.site.register(PsychometricQuestionSet1)
admin.site.register(PsychometricTestResult2)
admin.site.register(PsychometricTest2)
admin.site.register(PsychometricQuestionSet2)
admin.site.register(PsychometricTestResult3)
admin.site.register(PsychometricTest3)
admin.site.register(PsychometricQuestionSet3)
admin.site.register(PsychometricTestResult4)
admin.site.register(PsychometricTest4)
admin.site.register(PsychometricQuestionSet4)
admin.site.register(PsychometricTestResult5)
admin.site.register(PsychometricTest5)
admin.site.register(PsychometricQuestionSet5)
admin.site.register(PsychometricTestResult6)
admin.site.register(PsychometricTest6)
admin.site.register(PsychometricQuestionSet6)
admin.site.register(DataBaseDataAnalystProfile)
admin.site.register(VerbalAbilityTestResult1)
admin.site.register(VerbalAbilityTest1)
admin.site.register(VerbalAbilityQuestionSet1)
admin.site.register(VerbalAbilityTestResult2)
admin.site.register(VerbalAbilityTest2)
admin.site.register(VerbalAbilityQuestionSet2)

admin.site.register(NumericalQuestionSet)
admin.site.register(NumericalAbilityTest)
admin.site.register(NumericalAbilityTestResult)
admin.site.register(ClosureAbilityTest)
admin.site.register(ClosureQuestionSet)
admin.site.register(ClosureAbilityTestResult)
admin.site.register(SpatialQuestionSet)
admin.site.register(SpatialAbilityTest)
admin.site.register(SpatialAbilityTestResult)
admin.site.register(MechanicalAbilityTest)
admin.site.register(MechanicalAbilityTestResult)
admin.site.register(MechanicalQuestionSet)
admin.site.register(ClericalAbilityTest)
admin.site.register(ClericalAbilityTestResult)
admin.site.register(ClericalQuestionSet)
admin.site.register(ReasoningAbilityTest)
admin.site.register(ReasoningQuestionSet)
admin.site.register(ReasoningAbilityTestResult)
# admin.site.register(VerbalAbilityAnswerSet1)
admin.site.register(ChoiceQuestionSet1)
admin.site.register(ChoiceQuestionSet2)
admin.site.register(ChoiceNumericalQuestionSet)
admin.site.register(ChoiceClosureQuestionSet)
admin.site.register(ChoiceClericalQuestionSet)
admin.site.register(ChoiceReasoningQuestionSet)
admin.site.register(ChoiceSpatialQuestionSet)
admin.site.register(ChoiceMechanicalQuestionSet)
admin.site.register(Question)

