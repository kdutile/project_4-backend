from .serializers_base import UserAccountSerializerBase
from items_api.serializers_base import ItemSerializerBase

class UserAccountSerializer(UserAccountSerializerBase):
    items = ItemSerializerBase(many=True, allow_null=True, required=False)

    class Meta(UserAccountSerializerBase.Meta):
        fields = UserAccountSerializerBase.Meta.fields + ('items',)

    # def create(self, validated_data):
    #     items_data = validated_data.pop('items')
    #     user = UserAccountSerializerBase.Meta.model.objects.create(**validated_data)
    #     for item_data in items_data:
    #         ItemSerializerBase.Meta.model.objects.create(useraccount=useraccount, **item_data)
    #     return useraccount
