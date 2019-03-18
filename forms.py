from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, RadioField, TextAreaField, DecimalField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Optional, InputRequired, Email
from flask_babel import gettext, ngettext, lazy_gettext
import random
import utility

#----------------------------------------------------------#
# LOGIN FORM FOR PARTIPICANT INFO COLLECTION
#----------------------------------------------------------#
class LoginForm(FlaskForm):
    informed_consent_data = lazy_gettext(u"""        
        During this experiment you will be asked to taste chocolate 
        (two small portions).

        By participating in this experiment, you confirm that you 
        do not have any impairments when consuming chocolate 
        (i.e. allergies or diabetes), neither an impairment 
        with your senses of taste, smell, or any problems with 
        your visual and hearing capabilities.

        For your safety, the personal information that you will here 
        provide will not be shared with anyone else, and it won't be 
        used  publicly.

        By clicking below, you confirm that you agree with the 
        aforementioned conditions, and you can start the experiment.

        Please keep in mind that you can stop participating in this experiment,
        at any time, without any consequences. If you require help, 
        or if you have inquiries, please do not hesitate to call any of 
        the present research assistants. 
        """)
    
    name = StringField(lazy_gettext('Name'), validators=[InputRequired()])
    email = StringField(lazy_gettext('Email (Optional)'), validators=[Optional(), Email()])
    age = IntegerField(lazy_gettext('Age'), validators=[InputRequired()])
    city = StringField(lazy_gettext('City or country of residence'), validators=[InputRequired()])    
    gender = SelectField(lazy_gettext('Gender'),
        choices=[('gender_male', lazy_gettext('Male')),
                 ('gender_female', lazy_gettext('Female')),
                 ('gender_other', lazy_gettext('Other'))], validators=[InputRequired()])

    consent_text = TextAreaField(lazy_gettext("Informed Consent"), default=informed_consent_data, render_kw={'readonly': True}, validators=[Optional()])   

    consent = RadioField('Consent', choices=[('agree', lazy_gettext('I agree')), ('disagree', lazy_gettext('I disagree'))], validators=[InputRequired()])    
    submit = SubmitField(lazy_gettext('Next'))
    
#----------------------------------------------------------#
class ScaleForm(FlaskForm):
    scale = RadioField('Dissonance', choices=[
                      ('SD', 'Strongly Dissonant'),
                      ('D', 'Dissonant'),
                      ('N', 'I don\'t know'),
                      ('C', 'Consonant'),
                      ('SC', 'Strongly Consonant')])
                      
    
    submit = SubmitField('Next')

#----------------------------------------------------------#
class SoundQuestionsForm(FlaskForm):
    question1_text = lazy_gettext("How sour was this chocolate's flavour ?")
    question1 = RadioField('Sour', choices=[
        ('1', lazy_gettext('1 - Not at all')),
        ('2', '2'), ('3', '3'), 
        ('4', lazy_gettext('4 - Moderate')),
        ('5', '5'), ('6', '6'),
        ('7', lazy_gettext('7 - Very sour'))], validators=[DataRequired()])

    question2_text = lazy_gettext("How much did you like this sound ?")
    question2 = RadioField('Sound', choices=[
        ('1', lazy_gettext('1 - Not at all')),
        ('2', '2'), ('3', '3'), 
        ('4', lazy_gettext('4 - Moderate')),
        ('5', '5'), ('6', '6'),
        ('7', lazy_gettext('7 - Very much'))], validators=[DataRequired()])
    
    question3_text = lazy_gettext("How much did you enjoy the flavour of this chocolate ?")
    question3 = RadioField('Flavour', choices=[
        ('1', lazy_gettext('1 - Not at all')),
        ('2', '2'), ('3', '3'), 
        ('4', lazy_gettext('4 - Moderate')),
        ('5', '5'), ('6', '6'),
        ('7', lazy_gettext('7 - Very much'))], validators=[DataRequired()])
    
    question4_text = lazy_gettext("How bitter was this chocolate's flavour ?")
    question4 = RadioField('Bitter', choices=[
        ('1', lazy_gettext('1 - Not at all')),
        ('2', '2'), ('3', '3'), 
        ('4', lazy_gettext('4 - Moderate')),
        ('5', '5'), ('6', '6'),
        ('7', lazy_gettext('7 - Very bitter'))], validators=[DataRequired()])
    
    question5_text = lazy_gettext("How sweet was this chocolate's flavour ?")
    question5 = RadioField('Sweet', choices=[
        ('1', lazy_gettext('1 - Not at all')),
        ('2', '2'), ('3', '3'), 
        ('4', lazy_gettext('4 - Moderate')),
        ('5', '5'), ('6', '6'),
        ('7', lazy_gettext('7 - Very sweet'))], validators=[DataRequired()])
    
    question6_text = lazy_gettext("How strong was this chocolate's flavour ?")
    question6 = RadioField('Strong', choices=[
        ('1', lazy_gettext('1 - Not at all')),
        ('2', '2'), ('3', '3'), 
        ('4', lazy_gettext('4 - Moderate')),
        ('5', '5'), ('6', '6'),
        ('7', lazy_gettext('7 - Very strong'))], validators=[DataRequired()])

    question7_text = lazy_gettext("How much do you think this song matches with this chocolate's flavour?")
    question7 = RadioField('Match', choices=[
        ('1', lazy_gettext('1 - Not at all')),
        ('2', '2'), ('3', '3'), 
        ('4', lazy_gettext('4 - Moderate')),
        ('5', '5'), ('6', '6'),
        ('7', lazy_gettext('7 - Very much'))], validators=[DataRequired()])
    
    question8_text = lazy_gettext("How was the texture of this chocolate?")
    question8 = RadioField('Texture', choices=[
        ('1', lazy_gettext('1 - Very hard')),
        ('2', '2'), ('3', '3'), 
        ('4', lazy_gettext('4 - Balanced')),
        ('5', '5'), ('6', '6'),
        ('7', lazy_gettext('7 - Very soft'))], validators=[DataRequired()])
    
    submit = SubmitField(lazy_gettext('Next'))   
    
#----------------------------------------------------------#
class ComparisonQuestions(FlaskForm):    
    question1_text = lazy_gettext("Which chocolate (between WD and TK) do you think is more expensive?")
    question1_choices = utility.randomize_choices([
                        ('WD', lazy_gettext('Chocolate WD')),
                        ('TK', lazy_gettext('Chocolate TK')),
                        ('Both', lazy_gettext('Both have the same price'))])  

    question1 = RadioField('Expensive', choices=question1_choices)

    
    question2_text = lazy_gettext("Would you pay more for a chocolate experience that comes with a song that is able to enhance its flavour? (Compared to the average price of a chocolate without any music?)")
    question2_choices = utility.randomize_choices([
                        ('yes', lazy_gettext('Yes')),
                        ('no', lazy_gettext('No'))])

    question2 = RadioField('PayMore', choices=question2_choices) 

    question3_text = lazy_gettext("How much would you pay for chocolate WD? (Answer in Euros and, as reference, assume 0.5 EUR as the approximate price average per unit)")
    question3 = DecimalField('Price')

    question4_text = lazy_gettext("Which chocolate did you prefer ?")
    question4_choices = utility.randomize_choices([
        ('Both', lazy_gettext('I like both equally')),
        ('None', lazy_gettext('None')),
        ('WD', lazy_gettext('Chocolate WD')),
        ('TK', lazy_gettext('Chocolate TK'))])

    question4 = RadioField('Prefer', choices= question4_choices)
    
    question5_text = lazy_gettext("Which experience did you prefer?")
    question5_choices = utility.randomize_choices([
        ('WD', lazy_gettext('With chocolate WD')),
        ('Both', lazy_gettext('Both equally')),
        ('TK', lazy_gettext('With chocolate TK'))])

    question5 = RadioField('XPPrefer', choices=question5_choices)
    
    question6_text = lazy_gettext("How much would you pay for chocolate TK? (Answer in Euros and, as reference, assume 0.5 EUR as the approximate price average per unit)")
    question6 = DecimalField('Price') 

    submit = SubmitField(lazy_gettext('Next'))  


   
    

#----------------------------------------------------------#


