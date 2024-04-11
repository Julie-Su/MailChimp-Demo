# MailChimp-Demo

- app.py: Main python file that runs. Includes the parameters needed.
- mailchimp-python-funciton.py: The API functions needed. Includes "audience_creation_function", "add_members_to_audience_function", "campaign_creation_function", "customized_template", "send_mail", "get_campaign_info_funciton". It links to configure.py for MailChimp API key and username.
- configure.py: Stores MailChimp API key and username.
- campaign_template.py: Stores the campaign content with html. Linked to app.py.
- template.html: Same as campaign_template.py.
