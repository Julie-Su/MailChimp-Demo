# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 08:05:48 2020

@author: sherangagamwasam
"""
import mailchimp_python_function as mpf
import newsletter_template

# =============================================================================
# audience creation
# =============================================================================

audience_creation_dictionary = {
    "audience_name" : "demoAudience",
    "company" : "demoCompany",
    "address1" : "No.7 Aly. 24 Ln. 247",
    "city" :  "New Taipei City",
    "state" : "Xindian",
    "zip_code" : "231",
    "country" : "Taiwan", # FOR SRI LANKA : USE LK
    "from_name" : "YuanZhen",
    "from_email" : "yuanzhen.julie.su@gmail.com",
    "language" : "en"
}    
    
audience_creation = mpf.audience_creation_function(audience_creation_dictionary)

# =============================================================================
# add members to the existing audience 
# =============================================================================

audience_id = audience_creation['id']
# add the email list here
email_list = ['yuanzhen.julie.su@gmail.com',
              'darrell.wang@ematicsolutions.com',
              'luo-hsuan.ho@ematicsolutions.com']

mpf.add_members_to_audience_function(
    audience_id = audience_creation['id'],
    email_list = email_list)

# =============================================================================
# campaign creation
# =============================================================================

campaign_name = 'Demo Campaign'
from_name = 'YuanZhen'
reply_to = 'yuanzhen.julie.su@gmail.com' # test1@gmail.com

campaign = mpf.campaign_creation_function(campaign_name=campaign_name,
                                      audience_id=audience_creation['id'],
                                      from_name=from_name,
                                      reply_to=reply_to)

# =============================================================================
# news letter tempates creation
# =============================================================================

html_code = campaign_template.html_code           

mpf.customized_template(html_code=html_code, 
                    campaign_id=campaign['id'])

# =============================================================================
# send the mail campaign
# =============================================================================

mpf.send_mail(campaign_id=campaign['id'])  
mpf.get_campaign_info_funciton(campaign_id=campaign['id'])         
