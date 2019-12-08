import React from 'react';
import axios from 'axios';
import { Container, Grid, Header } from 'semantic-ui-react';

import DataSetService from '../../../services/DataSetService';
import LogService from '../../../services/LogSetService';

import List from '../../Logs/List/index';

class Detail extends React.Component {
  state = { dataset: null, logs: [] }

  componentDidMount() {
    const { match: { params: { id } } } = this.props;

    axios.all([
      DataSetService.getById(id),
      LogService.listByDatasetId(id),
    ]).then(axios.spread((datasetRes, logsRes) => {
      const { data: datasetData } = datasetRes.data;
      const { data: logsData } = logsRes.data;

      if (datasetData) {
        this.setState({ dataset: datasetData });
      } else {
        this.setState({ dataset: null });
      }
      if (logsData) {
        this.setState({ logs: logsData });
      }
    })).catch(error => console.log(error));
  }

  render() {
    const { dataset, logs } = this.state;
    if (dataset === null) { return null; }
    return (
      <div style={{ marginTop: '7em' }}>
        <Container>
          <Grid>
            <Grid.Row>
              <Grid.Column>
                <Header>{dataset.filename}</Header>
              </Grid.Column>
            </Grid.Row>
            <Grid.Row>
              <Grid.Column>
                <Header>Logs:</Header>
                <List logs={logs} />
              </Grid.Column>
            </Grid.Row>
          </Grid>
        </Container>
      </div>
    );
  }
}

export default Detail;
