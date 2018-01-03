from character_builder.models import Class, Skill, Proficiency, SavingThrow
from character_builder.serializers import ClassSerializer, ProficiencySerializer, SavingThrowSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class_ = Class.objects.create(class_name='Ranger',
                              hit_die=10,
                              from_skills_choose=3)



Skill.objects.create(class_name=class_,
                     skill='Animal Handling')

Skill.objects.create(class_name=class_,
                     skill='Athletics')

Skill.objects.create(class_name=class_,
                     skill='Insight')

Skill.objects.create(class_name=class_,
                     skill='Investigation')

Skill.objects.create(class_name=class_,
                     skill='Nature')

Skill.objects.create(class_name=class_,
                     skill='Perception')

Skill.objects.create(class_name=class_,
                     skill='Stealth')

Skill.objects.create(class_name=class_,
                     skill='Survival')

Proficiency.objects.create(class_name=class_,
                           proficiency='Light Armor',
                           proficiency_type='Armor')

Proficiency.objects.create(class_name=class_,
                           proficiency='Medium Armor',
                           proficiency_type='Armor')

Proficiency.objects.create(class_name=class_,
                           proficiency='Shields',
                           proficiency_type='Armor')

Proficiency.objects.create(class_name=class_,
                           proficiency='Simple Weapons',
                           proficiency_type='Weapon')

Proficiency.objects.create(class_name=class_,
                           proficiency='Martial Weapons',
                           proficiency_type='Weapon')

SavingThrow.objects.create(class_name=class_,
                           short_name='STR',
                           long_name='Strength')

SavingThrow.objects.create(class_name=class_,
                           short_name='DEX',
                           long_name='Dexterity')

ranger_class_serializer = ClassSerializer(instance=class_)
ranger_class_serializer.data