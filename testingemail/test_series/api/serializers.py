from rest_framework import serializers
from ..models import PsychometricTest1, PsychometricQuestionSet1, PsychometricTestResult1, PsychometricProfile, \
    PsychometricTest2, PsychometricQuestionSet2, PsychometricTestResult2, PsychometricQuestionSet3, PsychometricTest3, \
    PsychometricTestResult3, PsychometricTestResult4, PsychometricTest4, PsychometricQuestionSet4, \
    PsychometricTestResult5, PsychometricTest5, PsychometricQuestionSet5, PsychometricQuestionSet6, PsychometricTest6, \
    PsychometricTestResult6, ChoiceQuestionSet1, VerbalAbilityQuestionSet1, ChoiceQuestionSet2, \
    VerbalAbilityQuestionSet2, ChoiceNumericalQuestionSet, ChoiceClericalQuestionSet, ChoiceReasoningQuestionSet, \
    ReasoningQuestionSet, ChoiceSpatialQuestionSet, SpatialQuestionSet, ChoiceMechanicalQuestionSet, \
    ChoiceClosureQuestionSet


class ChoiceQuestion1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceQuestionSet1
        fields = ['option', 'option_type']

    def to_representation(self, instance):
        data = {
            'label': instance.option,
            'values': instance.option,
        }
        return data


class VerbalQuestion1Serializer(serializers.ModelSerializer):
    options = ChoiceQuestion1Serializer(many=True, read_only=True)
    option_type = serializers.SerializerMethodField()

    class Meta:
        model = VerbalAbilityQuestionSet1
        fields = ['id', 'question_text', 'question_type', 'option_type', 'options', ]

    def get_label(self, obj):
        return obj.question_text

    def get_option_type(self, obj):
        return f'text'


class ChoiceQuestionSet2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceQuestionSet2
        fields = ['option', 'option_type']

    def to_representation(self, instance):
        data = {
            'label': instance.option,
            'values': instance.option,
        }
        return data


class VerbalQuestion2Serializer(serializers.ModelSerializer):
    options = ChoiceQuestionSet2Serializer(many=True, read_only=True)
    option_type = serializers.SerializerMethodField()
    question_type = serializers.SerializerMethodField()

    class Meta:
        model = VerbalAbilityQuestionSet2
        fields = ['id', 'question_text', 'question_type', 'option_type', 'options', ]

    def get_label(self, obj):
        return obj.question_text

    def get_question_type(self, obj):
        return f'text'

    def get_option_type(self, obj):
        return f'text'


class ChoiceNumericalQuestionSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceNumericalQuestionSet
        fields = ['option', 'option_type']

    def to_representation(self, instance):
        data = {
            'label': instance.option,
            'values': instance.option,
        }
        return data


class NumericalQuestionSetSerializer(serializers.ModelSerializer):
    options = ChoiceNumericalQuestionSetSerializer(many=True, read_only=True)
    option_type = serializers.SerializerMethodField()
    question_type = serializers.SerializerMethodField()

    class Meta:
        model = VerbalAbilityQuestionSet2
        fields = ['id', 'question_text', 'question_type', 'option_type', 'options', ]

    def get_label(self, obj):
        return obj.question_text

    def get_question_type(self, obj):
        return f'text'

    def get_option_type(self, obj):
        return f'text'


class ChoiceNumericalQuestionSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceNumericalQuestionSet
        fields = ['option', 'option_type']

    def to_representation(self, instance):
        data = {
            'label': instance.option,
            'values': instance.option,
        }
        return data


class NumericalQuestionSetSerializer(serializers.ModelSerializer):
    options = ChoiceNumericalQuestionSetSerializer(many=True, read_only=True)
    option_type = serializers.SerializerMethodField()
    question_type = serializers.SerializerMethodField()

    class Meta:
        model = VerbalAbilityQuestionSet2
        fields = ['id', 'question_text', 'question_type', 'option_type', 'options', ]

    def get_label(self, obj):
        return obj.question_text

    def get_question_type(self, obj):
        return f'text'

    def get_option_type(self, obj):
        return f'text'


class ChoiceClericalQuestionSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceClericalQuestionSet
        fields = ['option', 'option_type']

    def to_representation(self, instance):
        data = {
            'label': instance.option,
            'values': instance.option,
        }
        return data


class ClericalQuestionSetSerializer(serializers.ModelSerializer):
    options = ChoiceClericalQuestionSetSerializer(many=True, read_only=True)
    option_type = serializers.SerializerMethodField()
    question_type = serializers.SerializerMethodField()

    class Meta:
        model = VerbalAbilityQuestionSet2
        fields = ['id', 'question_text', 'question_type', 'option_type', 'options', ]

    def get_label(self, obj):
        return obj.question_text

    def get_question_type(self, obj):
        return f'text'

    def get_option_type(self, obj):
        return f'text'


class ChoiceReasoningQuestionSetSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceReasoningQuestionSet
        fields = ['option', 'option_type']

    def to_representation(self, instance):
        data = {
            'label': instance.option,
            'values': instance.option,
        }
        return data


class ReasoningQuestionSetSerializer(serializers.ModelSerializer):
    options = ChoiceReasoningQuestionSetSetSerializer(many=True, read_only=True)
    option_type = serializers.SerializerMethodField()

    # question_type = serializers.SerializerMethodField()

    class Meta:
        model = ReasoningQuestionSet
        fields = ['id', 'question_text', 'question_type', 'option_type', 'options', ]

    def get_label(self, obj):
        return obj.question_text

    # def get_question_type(self, obj):
    #     return f'text'

    def get_option_type(self, obj):
        return f'text'


class ChoiceSpatialQuestionSetSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceSpatialQuestionSet
        fields = ['option', 'option_type']

    def to_representation(self, instance):
        data = {
            'label': instance.option,
            'values': instance.option,
        }
        return data


class SpatialQuestionSetSetSerializer(serializers.ModelSerializer):
    options = ChoiceSpatialQuestionSetSetSerializer(many=True, read_only=True)
    option_type = serializers.SerializerMethodField()

    question_type = serializers.SerializerMethodField()

    class Meta:
        model = SpatialQuestionSet
        fields = ['id', 'question_text', 'question_type', 'option_type', 'options', ]

    def get_label(self, obj):
        return obj.question_text

    def get_question_type(self, obj):
        return f'text'

    def get_option_type(self, obj):
        return f'text'


class ChoiceMechanicalQuestionSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceMechanicalQuestionSet
        fields = ['option', 'option_type']

    def to_representation(self, instance):
        data = {
            'label': instance.option,
            'values': instance.option,

        }
        return data


class MechanicalQuestionSetSerializer(serializers.ModelSerializer):
    options = ChoiceMechanicalQuestionSetSerializer(many=True, read_only=True)
    option_type = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    # image = serializers.SerializerMethodField()
    # question_type = serializers.SerializerMethodField()

    class Meta:
        model = SpatialQuestionSet
        fields = ['id', 'question_text', 'image', 'question_type', 'option_type', 'options', ]

    def get_label(self, obj):
        return obj.question_text

    # def get_question_type(self, obj):
    #     return f'image'

    def get_option_type(self, obj):
        return f'text'

    def get_image(self, obj):
        return f'https:/192.168.1.52/media/{obj.image}'


class ChoiceClosureQuestionSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceClosureQuestionSet
        fields = ['option', 'option_type']

    def to_representation(self, instance):
        data = {
            'label': instance.option,
            'values': instance.option,

        }
        return data


class ClosureQuestionSetSerializer(serializers.ModelSerializer):
    options = ChoiceClosureQuestionSetSerializer(many=True, read_only=True)
    option_type = serializers.SerializerMethodField()


    # image = serializers.SerializerMethodField()
    # question_type = serializers.SerializerMethodField()

    class Meta:
        model = SpatialQuestionSet
        fields = ['id', 'question_text', 'question_type', 'option_type', 'options', ]

    def get_label(self, obj):
        return obj.question_text

    # def get_question_type(self, obj):
    #     return f'image'

    def get_option_type(self, obj):
        return f'text'

    # def get_image(self, obj):
    #     return f'https:/192.168.1.52/media/{obj.image}'
