import json
original_json = '''
<Date from the rc portal>
   
'''

# Load the JSON data
data = json.loads(original_json)
user_journey = data["user_journeys"][0]
def get_default_value(dictionary, key, default="NA"):
    return dictionary.get(key, default)


# Perform the transformation
transformed_data = {
     "GRADE": "BA1",
    "CATEGORY": "PartTime",
    "SALUTATION": "Mr.",
    "FIRST_NAME": data["journey"]["fullNameAsAadhaar"],
    "MIDDLE_NAME": "",
    "LAST_NAME": "NA",
    "FATHER_NAME": data["journey"]["fathersNameAsOnPAN"],
    "GENDER": data["journey"]["genderAsPerAadhaar"],
    "MARITAL_STATUS": data["journey"]["maritalStatus"],
    "BLOOD_GROUP": data["journey"]["bloodGroup"],
    "AADHAR_NUMBER": data["journey"]["aadhaarCardNumber"],
    "UAN": "NA",
    "PAN": data["journey"]["panNumber"],
    "COUNTRY_CODE": "+91",
    "MOBILE": user_journey["user"]["login_credential"].replace("+91-", ""),
    "ALTERNATEMOBILE": "NA",
    "DOB": data["journey"]["dateOfBirthOnDL"],
    "EMAIL": data["journey"]["email"],
    "CURRENT_LOCATION": data["journey"]["store"],
    "CURRENT_ADDRESS": (
        data["journey"]["permanentAddressOnAadhaar"]
        if data["journey"]["isThisYourCurrentAddress"].lower() == "yes"
        else data["journey"]["currentAddress"]
    ),
    "CURRENT_ADDRESS_CITY": (
        data["journey"]["permanentCityOnAadhaar"]
        if data["journey"]["isThisYourCurrentAddress"].lower() == "yes"
        else data["journey"]["currentCity"]
    ),
    "CURRENT_ADDRESS_STATE": (
        data["journey"]["permanentStateOnAadhaar"]
        if data["journey"]["isThisYourCurrentAddress"].lower() == "yes"
        else data["journey"]["currentState"]
    ),
    "CURRENT_ADDRESS_PIN": (
        data["journey"]["permanentPincodeOnAadhaar"]
        if data["journey"]["isThisYourCurrentAddress"].lower() == "yes"
        else data["journey"]["currentPincode"]
    ),

    "PERMANENT_ADDRESS": data["journey"]["permanentAddressOnAadhaar"],
    "PERMANENT_ADDRESS_CITY": data["journey"]["permanentCityOnAadhaar"],
    "PERMANENT_ADDRESS_STATE": data["journey"]["permanentStateOnAadhaar"],
    "PERMANENT_ADDRESS_PIN": data["journey"]["permanentPincodeOnAadhaar"],
    "REGION": data["journey"]["region"].replace(" ", "") if data["journey"]["region"] else None,
    #"REGION": data["journey"]["region"],
    "REFERRAL_NAME": "NA",
    "REFERRAL_ID": data["journey"]["referralId"],
    "RESUME_SOURCE": data["journey"]["joiningSource"],
    "MEDIA_NAME": "NA",
    "AGENCY": "NA",
    "OLD_EMPLOYEE_CODE": "NA",
    "DRIVING_LICENSE_DETAILS": {
        "LICENSE_NO": data["journey"]["idNumber"],
        "DATE_OF_ISSUE": data["journey"]["dateOfIssueOnDL"],
        "DATE_OF_EXPIRY": data["journey"]["dateOfExpiryOnDL"],
        "PLACE_OF_ISSUE": "NA"
    },
    "BANK_DETAILS": {
    "BANK_NAME": data["journey"]["bankName"],
    "IFSC_CODE": data["journey"]["ifscCode"],
    "ACCOUNT_NUMBER": data["journey"]["accountNumber"],
    "ACCOUNT_HOLDER_NAME": data["journey"]["fullNameOnBankAccount"]
  },
  "DOCURLS": [
    {
      "DOC_TYPE": "AADHAR_FRONT",
      "URL": data["journey"]["uploadAadhaarFirstPage"]
    },
    {
      "DOC_TYPE": "AADHAR_BACK",
      "URL": data["journey"]["uploadAadhaarLastPage"]
    },
    {
      "DOC_TYPE": "PAN",
      "URL": data["journey"]["uploadPANCard"]
    },
    {
      "DOC_TYPE": "DRIVING_LICENSE_FRONT",
      "URL": data["journey"]["uploadDrivingLicenseFront"]
    },
    {
      "DOC_TYPE": "DRIVING_LICENSE_BACK",
      "URL": data["journey"]["uploadDrivingLicenseBack"]
    },
    {
      "DOC_TYPE": "PASSPORT_PHOTO",
      "URL": data["journey"]["capturedImage"]
    }
  ],
  "METADATA": {
    "WORKING_STATE": data["journey"]["workingState"],
    "WORKING_CITY": data["journey"]["workingCity"],
    "STORE": data["journey"]["store"],
    "JOINING_SOURCE": data["journey"]["joiningSource"],
    "NOMINEE_NAME": data["journey"]["nomineeName"],
    "NOMINEE_RELATIONSHIP": data["journey"]["relationWithNominee"]
  }


    # Add more fields as needed
}
# Convert the result to JSON format
result_json = json.dumps(transformed_data, indent=2)
print(result_json)
