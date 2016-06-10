# mode_python_pdf_download
This script allows users to download PDF's from email shared reports that include PDF


# Steps to use this script:

1.  Make sure your report has <a href="https://help.modeanalytics.com/articles/share-via-email/">email sharing enabled</a> and includes a PDF attachment in the report in the email. At least one PDF report needs to have been generated for this script to work.
2.  In Mode, generate API token (under Settings -> Organization Name -> API Tokens)
2.  Add token and password values to the python.properties file.
3.  In pdf.py, set the api_url organization_username and report_token values in the get_mode_json() method. 
4.  Run the script using python pdf.py
