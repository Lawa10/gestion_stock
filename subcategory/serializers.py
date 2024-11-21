from rest_framework import serializers
from rest_framework.utils.representation import serializer_repr

from stock.subcategory.models import SubCategory


class SubSerializers(serializers.ModelSerializer):
      class Meta:
          model = SubCategory
          field = '__all__'
