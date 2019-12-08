import React from 'react';
import { Container, Grid, Header } from 'semantic-ui-react';

import DataSetService from '../../../services/DataSetService';

import List from '../../Logs/';

class Detail extends React.Component {
  state = { dataset: null, logs: [] }

  componentDidMount() {
    this.fetch();
  }

  fetch = async () => {
    const { match: { params: { id } } } = this.props;
    try {
      const response = await DataSetService.getById(id);
      const { data } = response.data;
      this.setState({ dataset: data });
    } catch (error) {
      console.log(error);
    }
  }

  render() {
    const { match: { params: { id } } } = this.props;
    const { dataset } = this.state;
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
                <List datasetId={id} />
              </Grid.Column>
            </Grid.Row>
          </Grid>
        </Container>
      </div>
    );
  }
}

export default Detail;
