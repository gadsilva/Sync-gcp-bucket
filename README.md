# README
I've been doing some work with [Pulumi](https://www.pulumi.com) lately, so I figured I'd make a repo that does what my [Medium article](https://medium.com/@glen.yu/diy-google-cloud-storage-replication-using-cloud-functions-51ae3a7124a7) talks about.


## Prerequisites
- `pulumi`
- `python` (3.7)
- `npm`

Service account used needs to have the `roles/storage.objectAdmin` role added. 


## Setup
- install packages
```
npm install
```

- authenticate to GCP
```
gcloud auth application-default login
```

