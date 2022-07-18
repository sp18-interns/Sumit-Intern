from rest_framework import serializers
from watchlist.models import Movie


class MovieSerializers(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['name']
        # exclude = ['description', 'id', 'active']

    def get_len_name(self, object):
        length = len(object.name)
        return length


    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Name & description should be different')
    #     else:
    #         return data
    #
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is to Short')
    #     else:
    #         return value

#
#
# class MovieSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
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
#
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name & description should be different')
#         else:
#             return data
#
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is to Short')
#         else:
#             return value
