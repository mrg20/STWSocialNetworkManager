from  rest_framework.fields  import  CharField
from  rest_framework.relations  import  HyperlinkedRelatedField,  HyperlinkedIdentityField
from  rest_framework.serializers  import  HyperlinkedModelSerializer


class NetworkSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='boxes:networks')
    complements = HyperlinkedIdentityField(many=True, read_only=True,
                                           view_name='boxes:complements')