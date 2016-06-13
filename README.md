# mode_python_pdf_download
This script allows users to download PDF's from email shared reports that include PDF


# Steps to use this script:

1.  Make sure your report has <a href="https://help.modeanalytics.com/articles/share-via-email/">email sharing enabled</a> and includes a PDF attachment in the email or that you have a recent PDF export of your report. At least one PDF report needs to have been generated for this script to work.
2.  In Mode, generate API token (under Settings -> Your Name -> API Tokens).
3.  Add the token and password values to the python.properties file.
4.  Run the script using `python pdf.py -org={{organization_username}} -report={{report_token}}`

For example, for this report https://modeanalytics.com/modeanalytics/reports/eb7e7c23e72f I would run:

`python pdf.py -org=modeanalytics -report=123456abcdef`

