from .model import SparcPortalSearchParameters, SparcPortalTag, SparcPortalFile, SparcPortalDataset, SparcPortalModelCount, SparcPortalTerm, SparcPortalPaginatedDatasetResponse, SparcPortalPaginatedFileResponse

dataset1 = SparcPortalDataset(
    id=3,
    name="Fynn Blackwell's Dataset",
    description="This is a very interesting dataset",
    owner_name="Fynn Blackwell",
    organization_name="Blackfynn",
    license="Apache 2.0",
    tags=[SparcPortalTag("neurology")],
    version=1,
    size=10000,
    contributors=["Fynn Blackwell"],
    model_count=[
        SparcPortalModelCount(
            name="specimen",
            count=125
        )
    ],
    file_count=220,
    record_count=125,
    uri="s3://bucket/3/1",
    arn="arn:aws:s3:::bucket/3/1",
    status="PUBLISH_SUCCEEDED",
    doi="10.21397/giuz-iqq5",
    banner="https://discover.blackfynn.com/dataset-assets/3/1/banner.jpg",
    readme="https://discover.blackfynn.com/dataset-assets/3/1/readme.md",
    created_at="2019-06-21T16:04:16.348-04:00",
    updated_at="2019-06-21T16:04:16.348-04:00"
)

dataset2 = SparcPortalDataset(
    id=1,
    name="My Blackfynn Dataset",
    description="This description contains the word Parkinson's",
    owner_name="Fynn Blackwell",
    organization_name="Blackfynn",
    license="Apache 2.0",
    tags=[
        SparcPortalTag("research")
    ],
    version=1,
    size=10000,
    contributors=[
        "SpPqJyzHnJ9BCfU4eAIG",
        "MW1ByFPiZ9V55mxPl0Z5"
    ],
    model_count=[
        SparcPortalModelCount(
            name="Patient",
            count=10
        )
    ],
    file_count=55,
    record_count=10,
    uri="s3://bucket/3/1",
    arn="arn:aws:s3:::bucket/1/1",
    status="PUBLISH_SUCCEEDED",
    doi="10.21397/abcd-1234",
    banner="https://discover.blackfynn.com/dataset-assets/1/1/banner.jpg",
    readme="https://discover.blackfynn.com/dataset-assets/1/1/readme.md",
    created_at="2019-06-21T16:04:16.288-04:00",
    updated_at="2019-06-21T16:04:16.288-04:00"
)

file1 = SparcPortalFile(
    name="test.jpg",
    dataset_id=3,
    dataset_version=1,
    size=5555,
    file_type="JPG",
    uri="s3://bucket/3/1/packages/test.jpg",
    created_at="2019-06-21T16:51:04.453-04:00"
)

file2 = SparcPortalFile(
    name="brain.jpg",
    dataset_id=3,
    dataset_version=1,
    size=12345,
    file_type="JPG",
    uri="s3://bucket/3/1/packages/brain.jpg",
    created_at="2019-06-21T16:51:04.453-04:00"
)