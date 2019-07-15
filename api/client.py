import requests
from urllib.parse import urlparse
import abc

from .model import SparcPortalSearchParameters, SparcPortalTag, SparcPortalFile, SparcPortalDataset, SparcPortalModelCount, SparcPortalTerm, SparcPortalPaginatedDatasetResponse, SparcPortalPaginatedFileResponse
from .fixtures import dataset1, dataset2, file1, file2

class BaseSparcPortalApiClient(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_datasets(self, params):
        # type: (SparcPortalSearchParameters) -> SparcPortalPaginatedDatasetResponse
        pass

    @abc.abstractmethod
    def search_files(self, params):
        # type: (SparcPortalSearchParameters) -> SparcPortalPaginatedFileResponse
        pass

    @abc.abstractmethod
    def retrieve_featured_datasets(self):
        # type: () -> List[SparcPortalDataset]
        pass

    @abc.abstractmethod
    def retrieve_dataset(self, id):
        # type: (int) -> SparcPortalDataset
        pass

class MockSparcPortalApiClient(BaseSparcPortalApiClient):
    def retrieve_featured_datasets(self):
        return [dataset1, dataset2, dataset1, dataset2]

    def retrieve_dataset(self, id):
        return dataset1

    def search_datasets(self, params):
        print(params)

        return SparcPortalPaginatedDatasetResponse(
            limit=params.limit,
            offset=params.offset,
            datasets=[dataset1, dataset2],
            total_count=10
        )

    def search_files(self, params):
        print(params)

        return SparcPortalPaginatedFileResponse(
            limit=params.limit,
            offset=params.offset,
            files=[file1, file2],
            total_count=100
        )