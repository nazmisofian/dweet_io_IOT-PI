# dweet_io_IOT-PI
This is a repository to keep a sample of the functioning script for sending sensor information from the Raspberry Pi Sense-Hat to dweet.io dashboard.

In order to use the Google Dashboard, you will have to do an additional steps to obtain the links and modify the parameters slightly.

1. Prepare a form from google form template, it can be anything as long as you request for 'Short Answer' on the multiple dropdown choice

![Google Form Template](/Google_Form_Template.png)

2. Next you need to get the 'Get pre filled link' on the 3 dot menu next to the google profile

![Pre-Filled Link](/Pre_Filled_Link.png)

3. Then insert any values into the answer and submit, at the bottom left screen will popup a COPY LINK (This is important so make sure to copy down the link and paste onto a notepad)

![Pre-Filled insert](/Pre_Filled_insert.png)

![Get Copy Link from Pre-Filled Link](/Get_Copy_Link_from_Pre_Filled_Link.png)

Please remember to change viewForm change to formResponse, and add '&submit=Submit' when you get the link from google forms.

From this : https://docs.google.com/forms/d/e/1FAIpQLScyxjg-mIGo98LJrU_GfzrXDF2AaJD0BPCgdFisXeuAImaMcg/viewform?usp=pp_url&entry.462400853=123&entry.1250497753=456

to this : 'https://docs.google.com/forms/d/e/1FAIpQLScyxjg-mIGo98LJrU_GfzrXDF2AaJD0BPCgdFisXeuAImaMcg/formResponse?usp=pp_url&entry.462400853=' + variable + &entry.1250497753= + variable + '&submit=Submit'

A sample of the working dashboard is shown in the image below

![dweet_image](/Dweet_io-IOT-PI-2.png)
