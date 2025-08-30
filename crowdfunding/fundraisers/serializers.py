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

    def update(self, instance, validated_data): #requires two parameters: an instance of your model, we will update the properties.
        instance.title = validated_data.get('title', instance.title) #we are trying to say if the data are not there, bring back the data rather than nil/dont replace it)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save() #calling a function to save
        return instance

        