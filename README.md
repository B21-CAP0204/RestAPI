# Cloud Student

- [Jonathan](https://github.com/jonathanka13)

- [Adinda](https://github.com/adindaarp)

# RestAPI

This API is for verfify validation number family card that exists in Disdukcapil’s database (but it is still dummy data because we don’t have any citizen’s data, so we just make verification for the family card number only, for future we also verify another parameter like name and address) and then compare with data that user input in form

If name and number family card already exist, it will response JSON with object kk:True, the opposite is false.

API: deploy in GCP using App Engine service

Framework: Python Flask

Endpoint: https://neat-coast-314213.et.r.appspot.com/api2?<value_no_kk>  ----> where no_kk depends on user input

# Cloud Architecture

![Cloud Architecture](https://drive.google.com/drive/u/4/my-drive)

# Cloud Storage and Database

We use cloud firestore as database to store user’s data that has been registered in the application, such as name, address, and family card number. 
Besides, we use cloud storage to store images about user's family card that have been uploaded. 
Both resources are created by Google Cloud Platform (GCP) and integrated into firebase for managing our android applications.
