from django.contrib.auth.models import User
# from accounts.models import User
from django.db import models


class PsychometricProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.SET_NULL,
                                related_name='psychometric_test_user',
                                null=True,
                                blank=True,
                                unique=True,
                                )
    test_result_1 = models.OneToOneField('PsychometricTestResult1',
                                         on_delete=models.SET_NULL,
                                         related_name='psychometric_test_profile_1',
                                         null=True,
                                         blank=True,
                                         unique=True,
                                         )
    test_result_2 = models.OneToOneField('PsychometricTestResult2',
                                         on_delete=models.SET_NULL,
                                         related_name='psychometric_test_profile_2',
                                         null=True,
                                         blank=True,
                                         unique=True,
                                         )
    test_result_3 = models.OneToOneField('PsychometricTestResult3',
                                         on_delete=models.SET_NULL,
                                         related_name='psychometric_test_profile_3',
                                         null=True,
                                         blank=True,
                                         unique=True,
                                         )
    test_result_4 = models.OneToOneField('PsychometricTestResult4',
                                         on_delete=models.SET_NULL,
                                         related_name='psychometric_test_profile_4',
                                         null=True,
                                         blank=True,
                                         unique=True,
                                         )
    test_result_5 = models.OneToOneField('PsychometricTestResult5',
                                         on_delete=models.SET_NULL,
                                         related_name='psychometric_test_profile_5',
                                         null=True,
                                         blank=True,
                                         unique=True,
                                         )
    test_result_6 = models.OneToOneField('PsychometricTestResult6',
                                         on_delete=models.SET_NULL,
                                         related_name='psychometric_test_result6',
                                         null=True,
                                         blank=True,
                                         unique=True,
                                         )

    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email


class PsychometricTestResult1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    total_score = models.PositiveIntegerField(null=True,
                                              blank=True
                                              )
    z_score = models.DecimalField(max_digits=3,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  )
    test = models.ManyToManyField('PsychometricTest2',
                                  related_name='psychometric_test_result_1',
                                  blank=True,
                                  )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.user.email


class PsychometricTestResult2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.PositiveIntegerField(null=True,
                                              blank=True,
                                              )
    z_score = models.DecimalField(max_digits=3,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  )
    test = models.ManyToManyField('PsychometricTest2',
                                  related_name='psychometric_test_result_2',

                                  )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.user.email


class PsychometricTestResult3(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.PositiveIntegerField(null=True,
                                              blank=True,
                                              )
    z_score = models.DecimalField(max_digits=3,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  )
    test = models.ManyToManyField('PsychometricTest3',
                                  related_name='psychometric_test_result_3',
                                  blank=True,
                                  )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.user.email


class PsychometricTestResult4(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.PositiveIntegerField(null=True,
                                              blank=True,
                                              )
    z_score = models.DecimalField(max_digits=3,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  )
    test = models.ManyToManyField('PsychometricTest4',
                                  related_name='psychometric_test_result_4',
                                  blank=True,
                                  )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.user.email


class PsychometricTestResult5(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.PositiveIntegerField(null=True,
                                              blank=True,
                                              )
    z_score = models.DecimalField(max_digits=3,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  )
    test = models.ManyToManyField('PsychometricTest5',
                                  related_name='psychometric_test_result_5',
                                  blank=True,
                                  )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.user.email


class PsychometricTestResult6(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.PositiveIntegerField(null=True,
                                              blank=True,
                                              )
    z_score = models.DecimalField(max_digits=3,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  )
    test = models.ManyToManyField('PsychometricTest6',
                                  related_name='psychometric_test_result_6',
                                  blank=True,
                                  )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.user.email


class PsychometricTest1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('PsychometricQuestionSet1',
                                 on_delete=models.SET_NULL,
                                 related_name='psychometric_test_1',
                                 null=True,
                                 blank=True,
                                 )

    selected_option = models.CharField(max_length=100,
                                       null=True,
                                       blank=True,
                                       )
    score = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    # def __str__(self):
    #     return self.question.question_text


class PsychometricQuestionSet1(models.Model):
    question_text = models.TextField(null=True,
                                     blank=True,
                                     )
    option_a = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                default='0'
                                )

    option_b = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )

    option_c = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.question_text


class PsychometricTest2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('PsychometricQuestionSet2',
                                 on_delete=models.SET_NULL,
                                 related_name='psychometric_test_2',
                                 null=True, blank=True

                                 )
    choice_type = (
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),

    )
    selected_option = models.CharField(max_length=1, choices=choice_type,
                                       null=True,
                                       blank=True,
                                       )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.question.question_text


class PsychometricQuestionSet2(models.Model):
    question_text = models.TextField(null=True,
                                     blank=True,
                                     )
    option_a = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )

    option_b = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )

    option_c = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.question_text


class PsychometricTest3(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('PsychometricQuestionSet3',
                                 on_delete=models.SET_NULL,

                                 related_name='psychometric_test_3',
                                 null=True,
                                 blank=True,
                                 )
    choice_type = (
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),

    )
    selected_option = models.CharField(max_length=1, choices=choice_type,
                                       null=True,
                                       blank=True,
                                       )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.question.question_text


class PsychometricQuestionSet3(models.Model):
    question_text = models.TextField(null=True,
                                     blank=True,
                                     )
    option_a = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )

    option_b = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )

    option_c = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.question_text


class PsychometricTest4(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('PsychometricQuestionSet4',
                                 on_delete=models.SET_NULL,
                                 related_name='psychometric_test_4',
                                 null=True,
                                 blank=True,
                                 )
    selected_option = models.CharField(max_length=1,
                                       null=True,
                                       blank=True,
                                       )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.question.question_text


class PsychometricQuestionSet4(models.Model):
    question_text = models.TextField(null=True,
                                     blank=True,
                                     )
    option_a = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )

    option_b = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )

    option_c = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.question_text


class PsychometricTest5(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('PsychometricQuestionSet5',
                                 on_delete=models.SET_NULL,
                                 related_name='psychometric_test_5',
                                 null=True,
                                 blank=True,
                                 )
    selected_option = models.CharField(max_length=1,
                                       null=True,
                                       blank=True,
                                       )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.question.question_text


class PsychometricQuestionSet5(models.Model):
    question_text = models.TextField(null=True,
                                     blank=True,
                                     )
    option_a = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )
    option_b = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )
    option_c = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.question_text


class PsychometricTest6(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('PsychometricQuestionSet6',
                                 on_delete=models.SET_NULL,
                                 related_name='psychometric_test_6',
                                 null=True,
                                 blank=True,
                                 )
    selected_option = models.CharField(max_length=1,
                                       null=True,
                                       blank=True,
                                       )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.question.question_text


class PsychometricQuestionSet6(models.Model):
    question_text = models.TextField(null=True,
                                     blank=True,
                                     )
    option_a = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )

    option_b = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )

    option_c = models.CharField(max_length=15,
                                null=True,
                                blank=True,
                                )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return self.question_text


class DataBaseDataAnalystProfile(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             related_name='data_base_data_analyst_user',
                             null=True,
                             blank=True,

                             )
    verbal_ability_1 = models.OneToOneField('VerbalAbilityTestResult1',
                                            on_delete=models.SET_NULL,
                                            related_name='verbal_ability_test_user_profile_1',
                                            null=True,
                                            blank=True,
                                            unique=True,
                                            )
    verbal_ability_2 = models.OneToOneField('VerbalAbilityTestResult2',
                                            on_delete=models.SET_NULL,
                                            related_name='verbal_ability_test_user_profile_2',
                                            null=True,
                                            blank=True,
                                            unique=True,
                                            )

    numerical_ability = models.OneToOneField('NumericalAbilityTestResult', on_delete=models.SET_NULL,
                                             related_name='numerical_ability_test_profile',
                                             null=True,
                                             blank=True,
                                             unique=True, )
    closure_ability = models.OneToOneField('ClosureAbilityTestResult', on_delete=models.SET_NULL,
                                           related_name='closure_ability_test_profile',
                                           null=True,
                                           blank=True,
                                           unique=True, )

    spatial_ability = models.OneToOneField('SpatialAbilityTestResult', on_delete=models.SET_NULL,
                                           related_name='closure_ability_test_profile',
                                           null=True,
                                           blank=True,
                                           unique=True, )

    mechanical_ability = models.OneToOneField('MechanicalAbilityTestResult', on_delete=models.SET_NULL,
                                              related_name='mechanical_ability_test_profile',
                                              null=True,
                                              blank=True,
                                              unique=True, )
    clerical_ability = models.OneToOneField('ClericalAbilityTestResult', on_delete=models.SET_NULL,
                                            related_name='clerical_ability_test_profile',
                                            null=True,
                                            blank=True,
                                            unique=True, )

    reasoning_ability = models.OneToOneField('ReasoningAbilityTestResult', on_delete=models.SET_NULL,
                                             related_name='reasoning_ability_test_profile',
                                             null=True,
                                             blank=True,
                                             unique=True, )
    clerical_ability_score = models.IntegerField(default=0, null=True, blank=True)
    closure_ability_score = models.IntegerField(default=0, null=True, blank=True)
    mechanical_ability_score = models.IntegerField(default=0, null=True, blank=True)
    numerical_ability_score = models.IntegerField(default=0, null=True, blank=True)
    reasoning_ability_score = models.IntegerField(default=0, null=True, blank=True)
    spatial_ability_score = models.IntegerField(default=0, null=True, blank=True)
    verbal_ability_1_score = models.IntegerField(default=0, null=True, blank=True)
    verbal_ability_2_score = models.IntegerField(default=0, null=True, blank=True)
    total_score_of_all_test = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class VerbalAbilityTestResult1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.PositiveIntegerField(null=True,
                                              blank=True
                                              )
    z_score = models.DecimalField(max_digits=3,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  )
    test = models.ManyToManyField('VerbalAbilityTest1',
                                  related_name='verbal_ability_test_result_1',
                                  blank=True,
                                  )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.user)


class VerbalAbilityTest1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('VerbalAbilityQuestionSet1',
                                 on_delete=models.SET_NULL,
                                 related_name='verbal_ability_test_1',
                                 null=True,
                                 blank=True,
                                 )

    select_option = models.CharField(max_length=100,
                                     null=True,
                                     blank=True,
                                     )

    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.question) + " " + str(self.user) + " " + str(self.score)


class VerbalAbilityQuestionSet1(models.Model):
    question_text = models.CharField(max_length=500, null=True, blank=True)
    question_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.question_text)


class ChoiceQuestionSet1(models.Model):
    question = models.ForeignKey(VerbalAbilityQuestionSet1, on_delete=models.DO_NOTHING, related_name='options')
    option = models.CharField(max_length=2048, null=False, blank=False)
    option_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.question.question_text) + " ," + str(self.option)


class VerbalAbilityTestResult2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.PositiveIntegerField(null=True,
                                              blank=True
                                              )
    z_score = models.DecimalField(max_digits=3,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  )
    test = models.ManyToManyField('VerbalAbilityTest2',
                                  related_name='verbal_ability_test_result_2',
                                  blank=True,
                                  )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.user)


class VerbalAbilityTest2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('VerbalAbilityQuestionSet2',
                                 on_delete=models.SET_NULL,
                                 related_name='option',
                                 null=True,
                                 blank=True,
                                 )
    # choice_type = (
    #     ('a', 'a'),
    #     ('b', 'b'),
    #     ('c', 'c'),
    #     ('d', 'd'),
    #     ('e', 'e'),
    #
    # )
    score = models.IntegerField(null=True, blank=True)
    select_option = models.CharField(max_length=250,
                                     null=True,
                                     blank=True,
                                     )

    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.question) + " " + str(self.user)


class VerbalAbilityQuestionSet2(models.Model):
    question_text = models.CharField(max_length=500, null=True, blank=True)
    question_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.question_text)


class ChoiceQuestionSet2(models.Model):
    question = models.ForeignKey(VerbalAbilityQuestionSet2, on_delete=models.DO_NOTHING, related_name='options')
    option = models.CharField(max_length=2048, null=False, blank=False)
    option_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.question.question_text) + " ," + str(self.option)


################################################

class NumericalAbilityTestResult(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    total_score = models.PositiveIntegerField(null=True,
                                              blank=True
                                              )
    z_score = models.DecimalField(max_digits=3,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  )
    test = models.ManyToManyField('NumericalAbilityTest',
                                  related_name='numerical_ability_test_result',
                                  blank=True,
                                  )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.user)


class NumericalAbilityTest(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    question = models.ForeignKey('NumericalQuestionSet',
                                 on_delete=models.SET_NULL,
                                 related_name='numerical_ability_test',
                                 null=True,
                                 blank=True,
                                 )
    # choice_type = (
    #     ('a', 'a'),
    #     ('b', 'b'),
    #     ('c', 'c'),
    #     ('d', 'd'),
    #     ('e', 'e'),
    #
    # )
    select_option = models.CharField(max_length=100,
                                     null=True,
                                     blank=True,
                                     )

    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user) + ", " + str(self.question) + ", " + str(self.select_option) + " ," + str(self.score)


class NumericalQuestionSet(models.Model):
    question_text = models.TextField(max_length=500, null=True, blank=True)
    question_type = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.question_text


class ChoiceNumericalQuestionSet(models.Model):
    question = models.ForeignKey(NumericalQuestionSet, on_delete=models.DO_NOTHING, related_name='options')
    option = models.CharField(max_length=2048, null=False, blank=False)
    option_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.question.question_text) + " ; " + str(self.option)


################################################
class ClosureAbilityTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.PositiveIntegerField(null=True,
                                              blank=True
                                              )
    z_score = models.DecimalField(max_digits=3,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  )
    test = models.ManyToManyField('ClosureAbilityTest',
                                  related_name='closure_ability_test_result',
                                  blank=True,
                                  )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.user)


class ClosureAbilityTest(models.Model):
    score = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('ClosureQuestionSet',
                                 on_delete=models.SET_NULL,
                                 related_name='closure_ability_test',
                                 null=True,
                                 blank=True

                                 )

    select_option = models.CharField(max_length=100,
                                     null=True,
                                     blank=True,
                                     )

    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.question) + " " + str(self.user)


class ClosureQuestionSet(models.Model):
    question_text = models.CharField(max_length=500, null=True, blank=True)
    question_type = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.question_text


class ChoiceClosureQuestionSet(models.Model):
    question = models.ForeignKey(ClosureQuestionSet, on_delete=models.DO_NOTHING, related_name='options')
    option = models.CharField(max_length=2048, null=False, blank=False)
    option_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.question.question_text) + " ; " + str(self.option)


################################################

class SpatialAbilityTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.PositiveIntegerField(null=True,
                                              blank=True
                                              )
    z_score = models.DecimalField(max_digits=3,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  )
    test = models.ManyToManyField('SpatialAbilityTest',
                                  related_name='spatial_ability_test_result',
                                  blank=True,
                                  )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.user)


class SpatialAbilityTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True)
    question = models.ForeignKey('SpatialQuestionSet',
                                 on_delete=models.SET_NULL,
                                 related_name='spatial_ability_test',
                                 null=True,
                                 blank=True

                                 )

    select_option = models.CharField(max_length=100,
                                     null=True,
                                     blank=True,
                                     )

    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.question) + " " + str(self.user)


class SpatialQuestionSet(models.Model):
    question_text = models.CharField(max_length=500, null=True, blank=True)
    question_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.question_text


class ChoiceSpatialQuestionSet(models.Model):
    question = models.ForeignKey(SpatialQuestionSet, on_delete=models.DO_NOTHING, related_name='options')
    option = models.CharField(max_length=2048, null=False, blank=False)
    option_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.question.question_text) + " ; " + str(self.option)


####################################################################


class MechanicalAbilityTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    total_score = models.PositiveIntegerField(null=True,
                                              blank=True
                                              )
    z_score = models.DecimalField(max_digits=3,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  )
    test = models.ManyToManyField('MechanicalAbilityTest',
                                  related_name='mechanical_ability_test_result',
                                  blank=True,
                                  )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.user)


class MechanicalAbilityTest(models.Model):
    score = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('MechanicalQuestionSet',
                                 on_delete=models.SET_NULL,
                                 related_name='spatial_ability_test',
                                 null=True,
                                 blank=True

                                 )

    select_option = models.CharField(max_length=100,
                                     null=True,
                                     blank=True,
                                     )

    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.question) + " " + str(self.user)


class MechanicalQuestionSet(models.Model):
    question_text = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='uploads', null=True, blank=True)
    question_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.question_text + "  ," + str(self.image)


class ChoiceMechanicalQuestionSet(models.Model):
    question = models.ForeignKey(MechanicalQuestionSet, on_delete=models.DO_NOTHING, related_name='options')
    option = models.CharField(max_length=2048, null=False, blank=False)
    option_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.question.question_text) + " ; " + str(self.option)


####################################################################

class ClericalAbilityTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.PositiveIntegerField(null=True,
                                              blank=True
                                              )
    z_score = models.DecimalField(max_digits=3,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  )
    test = models.ManyToManyField('ClericalAbilityTest',
                                  related_name='clerical_ability_test_result',
                                  blank=True,
                                  )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.user)


class ClericalAbilityTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True)
    question = models.ForeignKey('ClericalQuestionSet',
                                 on_delete=models.SET_NULL,
                                 related_name='clerical_ability_test',
                                 null=True,
                                 blank=True

                                 )

    select_option = models.CharField(max_length=100,
                                     null=True,
                                     blank=True,
                                     )

    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.question) + " " + str(self.user)


class ClericalQuestionSet(models.Model):
    question_text = models.CharField(max_length=500, null=True, blank=True)
    question_type = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.question_text


class ChoiceClericalQuestionSet(models.Model):
    question = models.ForeignKey(ClericalQuestionSet, on_delete=models.DO_NOTHING, related_name='options')
    option = models.CharField(max_length=2048, null=False, blank=False)
    option_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.question.question_text) + " ; " + str(self.option)


####################################################################

class ReasoningAbilityTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.PositiveIntegerField(null=True,
                                              blank=True
                                              )
    z_score = models.DecimalField(max_digits=3,
                                  decimal_places=2,
                                  null=True,
                                  blank=True,
                                  )
    test = models.ManyToManyField('ReasoningAbilityTest',
                                  related_name='reasoning_ability_test_result',
                                  blank=True,
                                  )
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.user)


class ReasoningAbilityTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True)
    question = models.ForeignKey('ReasoningQuestionSet',
                                 on_delete=models.SET_NULL,
                                 related_name='reasoning_ability_test',
                                 null=True,
                                 blank=True

                                 )

    select_option = models.CharField(max_length=100,
                                     null=True,
                                     blank=True,
                                     )

    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )
    updated_at = models.DateTimeField(null=True,
                                      blank=True,
                                      )

    def __str__(self):
        return str(self.question) + " " + str(self.user)


class ReasoningQuestionSet(models.Model):
    question_text = models.CharField(max_length=500, null=True, blank=True)
    question_type = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.question_text


class ChoiceReasoningQuestionSet(models.Model):
    question = models.ForeignKey(ReasoningQuestionSet, on_delete=models.DO_NOTHING, related_name='options')
    option = models.CharField(max_length=2048, null=False, blank=False)
    option_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.question.question_text) + " ; " + str(self.option)


####################################################################
class Question(models.Model):
    question = models.CharField(max_length=2048, null=False, blank=False)
    question_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.question)

#
#