import axios from 'axios';

const { REACT_APP_API_URL, NODE_ENV } = process.env;

const config = {
  test: {
    base: REACT_APP_API_URL || 'http://localhost:5000',
  },
  development: {
    base: REACT_APP_API_URL || 'http://localhost:5000',
  }
};

export const apiClient = axios.create({
  baseURL: `${config[NODE_ENV].base}`,
});

export default config;
