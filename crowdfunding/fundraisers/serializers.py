from rest_framework import serializers
from django.apps import apps

class FundraiserSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.id') #getting the "id" from the relationship
    
    class Meta:
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'

class PledgeSerializer(serializers.ModelSerializer):

    supporter = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = apps.get_model('fundraisers.Pledge')
        fields = '__all__'

class FundraiserDetailSerializer(FundraiserSerializer): #copying/inheriting same function with already existed one
    pledges = PledgeSerializer(many=True, read_only=True) #defining that we will have many items

