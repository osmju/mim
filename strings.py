from flask_babel import gettext, ngettext, lazy_gettext

#----------------------------------------------------------#
experiment_instructions = lazy_gettext(u"""
        Dear participant, 
        <br/>
        <br/>

        In this experiment, you will taste two chocolates and evaluate your
        experience by answering a survey.
        <br/>
        <br/>

        This is a comparative exercise. Please follow the instructions 
        carefully.
    """
    )
#----------------------------------------------------------#

instructions_sound1 = lazy_gettext(u"""
        Drink some water to rinse your mouth. Afterwards, put on the
        headphones.<br/>
        <br/>

        Now, taste the chocolate <b>WD</b> while you listen to the 
        following soundtrack. You must click on the "play" button in 
        order for the sound to start playing.<br/>
        <br/>

        Once you start hearing the sound, put the chocolate inside your mouth
        and start tasting it.<br/>
        <br/>

        <h3>DO NOT CHEW THE CHOCOLATE IMMEDIATELY !</h3>
        <br/>
        
        Let it melt inside your mouth, so you can feel the details of its
        flavour. You can also close your eyes for better concentration.
        <br/>
        <br/>

        <i>When the soundtrack is over, go to the next page and start answering
        the questions.</i>
    """)
#----------------------------------------------------------#

instructions_sound2 = lazy_gettext(u"""
        Drink some water to rinse your mouth. Afterwards, put on the
        headphones.<br/>
        <br/>

        Now, taste the chocolate <b>TK</b> while you listen to the 
        following soundtrack. You must click on the "play" button in 
        order for the sound to start playing.<br/>
        <br/>

        Once you start hearing the sound, put the chocolate inside your mouth
        and start tasting it.<br/>
        <br/>

        <h3>DO NOT CHEW THE CHOCOLATE IMMEDIATELY !</h3>
        <br/>
        
        Let it melt inside your mouth, so you can feel the details of its
        flavour. You can also close your eyes for better concentration.
        <br/>
        <br/>

        <i>When the soundtrack is over, go to the next page and start answering
        the questions.</i>
    """)
#----------------------------------------------------------#
thanks = lazy_gettext(u"""        
        If you entered your email at the begining of the experiment, 
        you will receive detailled informations about the goals of this work
        in the upcoming weeks.
        <br/>
        <br/>

        The protocol for this experiment was validated by the 
        Ethical Comitee of the Katholieke Universiteit Leuven.
        <br/>
        <br/>

        If you have any questions, please send them to
        f.reinosoc@uniandes.edu.com.
        <br/>
        <br/> 

        We kindly ask you to keep this experience for yourself and not
        sharing it such that the next participants can enjoy the full
        experience.
        <br/>
        <br/>

        For more informations about our work, please visit        
        the blog http://sonictaste.weebly.com, 
        our twitter page (@sonictaste), or come visit us at the 
        Katholieke Universiteit Leuven.
        <br/>
        <br/>

        We hope that you enjoyed this new way of tasting Belgian chocolate !
    """)
#----------------------------------------------------------#

