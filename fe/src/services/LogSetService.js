import { apiClient } from './config';

const Service = {
  listByDatasetId(dataSetId) {
    const url = `/logs/${dataSetId}`;
    return apiClient.get(url);
  },
};

export default Service;
