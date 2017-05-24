from  rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from  rest_framework.serializers import HyperlinkedModelSerializer

from SocialNetworkManagerApp.models import Network, Complement, Box


class NetworkSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='boxes:network-detail')

    class Meta:
        model = Network
        fields = ('url', 'name', 'description', 'network_url')


class ComplementSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='boxes:complement-detail')
    id_network = HyperlinkedRelatedField(view_name='boxes:network-detail', queryset=Network.objects.all())

    class Meta:
        model = Complement
        fields = ('uri', 'type', 'id_network', 'description')


class BoxSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='boxes:box-detail')
    complement = HyperlinkedRelatedField(view_name='boxes:complement-detail', queryset=Complement.objects.all())

    class Meta:
        model = Box
        fields = ('uri', 'box_num', 'complement', 'logged_into_network')
