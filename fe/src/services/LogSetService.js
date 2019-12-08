import { apiClient } from './config';

const Service = {
  listByDatasetId(dataSetId, page) {
    const url = `/logs/${dataSetId}/page/${page}`;
    return apiClient.get(url);
  },
};

export default Service;
