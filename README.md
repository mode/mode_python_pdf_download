# mode_python_pdf_download
This script allows users to download PDF's from email shared reports that include PDF


# Steps to use this script:

1.  Make sure your report has <a href="https://help.modeanalytics.com/articles/share-via-email/">email sharing enabled</a> and includes a PDF attachment in the email or that you have a recent PDF export of your report. At least one PDF report needs to have been generated for this script to work.
2.  In Mode, generate API token (under Settings -> Organization Name -> API Tokens) for the organization in which your report resides.
3.  Add the token and password values to the python.properties file.
4.  Run the script using `python pdf.py -org={{organization_username}} -report={{report_token}}`

For example, for this report https://modeanalytics.com/modeanalytics/reports/287cb906e6bd I would run:

`python pdf.py -org=modeanalytics -report=287cb906e6bd`

