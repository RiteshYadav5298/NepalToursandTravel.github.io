from django import forms

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES=(
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    hotel_name = (
        ('Hotel Average', 'Hotel Average'),
        ('Hotel Plaza', 'Hotel Plaza'),
        ('Hotel Angel', 'Hotel Angel'),
        ('Hotel GreenOrchid', 'Hotel GreenOrchid'),
    )
    hotel_name = forms.ChoiceField(choices=hotel_name, required=True)
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateField(
        required=True, input_formats=["%Y-%m-%d",])
    check_out = forms.DateField(
        required=True, input_formats=["%Y-%m-%d", ])