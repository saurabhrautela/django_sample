from profiles import models
from rest_framework.serializers import ModelSerializer

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "name", "password")
        # Add extra property to a field e.g. add write only property to `password` field
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"}
            }
        }

        def create(self, validated_data):
            user = models.UserProfile.objects.create_user(
                email=validated_data["email"],
                name=validated_data["name"],
                password=validated_data["password"]
            )

            return user
