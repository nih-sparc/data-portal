class SparcPortalRecordProperty:
    def __init__(self, key, value):
        # type (str, str) -> SparcPortalRecordProperty
        self.key = key
        self.value = value

class SparcPortalDataTableHeader:
    def __init__(self, key, label, sortable):
        # type: (str, str, bool) -> SparcPortalDataTableSort
        self.key = key
        self.label = label
        self.sortable = sortable

class SparcPortalDataTableAction:
    def __init__(self, key, label):
        # type: (str, str) -> SparcPortalDataTableAction
        self.key = key
        self.label = label

class SparcPortalDataTableSort:
    def __init__(self, column, descending):
        # type: (str, bool) -> SparcPortalDataTableSort
        self.column = column
        self.descending = descending

class SparcPortalDataTable:
    def __init__(self, headers, default_sort, data):
        # type: (List[SparcPortalDataTableHeader], SparcPortalDataTableSort, List[List[any]]) -> SparcPortalDataTable
        self.headers = headers
        self.default_sort = default_sort
        self.data = data

class SparcPortalRecordSection:
    def __init__(self, title, data):
        # type: (str, SparcPortalDataTable) -> SparcPortalRecordSection
        self.title = title
        self.data = data

class SparcPortalRecord:
    def __init__(self, title, properties, sections):
        # type: (str, List[SparcPortalRecordProperty], List[SparcPortalRecordSection]) -> SparcPortalRecord
        self.title = title
        self.properties = properties
        self.sections = sections

class SparcPortalTerm:
    def __init__(self, term):
        # type: (str) -> SparcPortalTerm
        self.term = term

class SparcPortalTag:
    def __init__(self, tag):
        # type: (str) -> SparcPortalTag
        self.tag = tag

class SparcPortalSearchParameters:
    def __init__(self, limit, offset, terms, tags):
        # type: (int, int, List[SparcPortalTerm], List[SparcPortalTag]) -> SparcPortalSearchParameters
        self.limit = limit
        self.offset = offset
        self.terms = terms
        self.tags = tags

class SparcPortalModelCount:
    def __init__(self, name, count):
        # type: (str, int) -> SparcPortalModelCount
        self.model_name = name
        self.count = count

class SparcPortalPaginatedDatasetResponse:
    def __init__(self, limit, offset, datasets, total_count):
        # type: (int, int, List[SparcPortalDataset], int) -> SparcPortalPaginatedDatasetResponse
        self.limit = limit
        self.offset = offset
        self.datasets = datasets
        self.total_count = total_count

class SparcPortalPaginatedFileResponse:
    def __init__(self, limit, offset, files, total_count):
        # type: (int, int, List[SparcPortalFile], int) -> SparcPortalPaginatedFileResponse
        self.limit = limit
        self.offset = offset
        self.files = files
        self.total_count = total_count

class SparcPortalFile:
    def __init__(self, name, dataset_id, dataset_version, size, file_type, uri, created_at):
        self.name = name
        self.dataset_id = dataset_id
        self.dataset_version = dataset_version
        self.size = size
        self.file_type = file_type
        self.uri = uri
        self.created_at = created_at

class SparcPortalDataset:
    def __init__(
            self,
            id,
            name,
            description,
            owner_name,
            organization_name,
            license,
            tags,
            version,
            size,
            contributors,
            model_count,
            file_count,
            record_count,
            uri,
            arn,
            status,
            doi,
            banner,
            readme,
            created_at,
            updated_at
    ):
        # type: (int, str, str, str, str, str, List[SparcPortalTag], int, int, List[String], List[SparcPortalModelCount], int, int, str, str, str, str, str, str, str, str)
        self.id = id
        self.name = name
        self.description = description
        self.owner_name = owner_name
        self.organization_name = organization_name
        self.license = license
        self.tags = tags
        self.version = version
        self.size = size
        self.contributors = contributors
        self.model_count = model_count
        self.file_count = file_count
        self.record_count = record_count
        self.uri = uri
        self.arn = arn
        self.doi = doi
        self.banner = banner
        self.readme = readme
        self.created_at = created_at
        self.updated_at = updated_at