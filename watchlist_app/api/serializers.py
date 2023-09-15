from watchlist_app.models import Movie
from rest_framework import serializers

# Model Serializer


class MovieSerializer(serializers.ModelSerializer):
    # custom serializers field
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['active']

    # custom serializer field method
    def get_len_name(self, object):
        length = len(object.name)
        return length

    # Field level validation
    def validate_name(self, value):
        print("Field level validation")
        if len(value) < 2:
            raise serializers.ValidationError("The name is too short!")
        return value

    # Object level validation
    def validate(self, data):
        print("Object level validation")
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name should not be same as description!")
        return data

# Serializer

# Validators
# def name_length(value):
#     print("Validators validation")
#     if len(value) < 2:
#         raise serializers.ValidationError("The name is too short!")
#     return value


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

    # Field level validation
    # def validate_name(self, value):
    #     print("Field level validation")
    #     if len(value) < 2:
    #         raise serializers.ValidationError("The name is too short!")
    #     return value

    # Object level validation
    # def validate(self, data):
    #     print("Object level validation")
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name should not be same as description!")
    #     return data
