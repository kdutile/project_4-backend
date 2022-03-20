from .serializers_base import ItemSerializerBase
from auth_api.serializers_base import UserAccountSerializerBase

class ItemSerializer(ItemSerializerBase):
    user = UserAccountSerializerBase()
    class Meta(ItemSerializerBase.Meta):
        fields = ItemSerializerBase.Meta.fields + ('user',)
