from rest_framework import serializers

from notes_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields =('id', 'email', 'name', 'password', 'is_staff')
        extra_kwargs= {
            'password': {
                'write_only': True,
            }
        }


    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )

        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
    

class NotesSerializer(serializers.ModelSerializer):
    """Serializes a note object"""

    class Meta:
        model = models.Note
        fields =('id', 'user_id', 'title', 'body', 'created_at', 'updated_at')

    def create(self, validated_data):
        """Create and return a new note"""
        user = models.Note.objects.create(
            title=validated_data['title'],
            body=validated_data['body'],
        )

        return user
    