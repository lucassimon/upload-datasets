import { apiClient } from './config';

const Service = {
  upload(data) {
    const url = '/uploads';
    return apiClient.post(url, data);
  },

  paginated(page) {
    const url = `/datasets/page/${page}`;
    return apiClient.get(url);
  },

  getById(id) {
    const url = `/datasets/${id}`;
    return apiClient.get(url);
  },
};

export default Service;
